# =====================================================================
#  CỤM XỬ LÝ GIFTCODE: BẺ KHÓA LINK -> CÀO MÃ -> NẠP -> TỰ NGẮT
# =====================================================================

SCAN_INTERVAL_SECONDS = 60  # 1 phút quét 1 lần

def extract_giftcode_target_url(loc, session):
    """Bẻ khóa tất cả các dạng link rút gọn để lấy link giftcode gốc"""
    if not loc:
        return None
    if "giftcode.php?key=" in loc:
        return loc

    # Link rút gọn chứa ?url=...
    try:
        parsed = urllib.parse.urlparse(loc)
        target = urllib.parse.parse_qs(parsed.query).get("url", [None])[0]
        if target and "giftcode.php?key=" in target:
            return target
    except:
        pass

    # Link rút gọn qua trang trung gian (Traffictop, Link4m...)
    try:
        r = session.get(loc, headers=DEFAULT_WEB_HEADERS, timeout=8, allow_redirects=True)
        m_orig = re.search(r"var\s+originalUrl\s*=\s*['\"]([^'\"]+)['\"]", r.text)
        if m_orig:
            return m_orig.group(1)
        m_url = re.search(r"https?://(?:kien\.)?kiemtienngay\.us/giftcode\.php\?key=[a-zA-Z0-9]+", r.text)
        if m_url:
            return m_url.group(0)
    except:
        pass
    return None


def process_single_task(session, tid, round_num, acc_tag=""):
    """Thực hiện 1 task: Bẻ khóa -> Lấy mã -> Nạp vào TelePet"""
    global CURRENT_INIT_DATA, REDEEMED_CODES_TODAY
    url = f"https://kiemtienngay.us/nbk222/giftcode.php?task_id={tid}"
    try:
        r = session.get(url, allow_redirects=False, timeout=8)
        if r.status_code == 200 and "BẠN ĐÃ LẤY GIFTCODE NÀY RỒI" in r.text:
            return 0

        loc = r.headers.get("Location", "")
        target_url = extract_giftcode_target_url(loc, session)
        if not target_url:
            return 0

        # Xác nhận lấy mã
        headers_gift = {'Content-Type': 'application/x-www-form-urlencoded', 'Referer': target_url}
        r_claim = session.post(target_url, data="confirm_gift=1", headers=headers_gift, timeout=8)
        data = r_claim.json()

        if data.get("status") == "ok":
            code = data.get("code")
            if not code or code in REDEEMED_CODES_TODAY:
                return 0

            # Nạp mã trực tiếp vào TelePet
            redeem_data = {"action": "giftcode", "code": code, "init_data": CURRENT_INIT_DATA}
            res_tele = requests.post(API_URL, headers=HEADERS_TELEPET, data=redeem_data, timeout=8).json()

            if res_tele.get("ok"):
                earned = res_tele.get("amount", 5000)
                REDEEMED_CODES_TODAY.add(code)
                log("GIFT", f"{acc_tag}Task #{tid}: Mã [{code}] -> +{earned:,} Xu đã nạp!", Fore.GREEN)
                return earned
            else:
                err_msg = str(res_tele.get("error", ""))
                # 👉 NẾU BỊ SERVER CHẶN LIMIT -> TRẢ VỀ -999 ĐỂ NGẮT NGAY
                if any(k in err_msg.lower() for k in ["chào cậu", "hi chào", "giới hạn", "tối đa"]):
                    log("LIMIT", f"Đã chạm ngưỡng tối đa Giftcode hôm nay! Server báo: '{err_msg}'", Fore.RED)
                    return -999
                REDEEMED_CODES_TODAY.add(code)
    except:
        pass
    return 0


def scan_and_redeem_giftcodes():
    """Điều phối quét mã từ web và nạp vào tài khoản"""
    # Kiểm tra trước: nếu nick đã locked=2 thì ngắt luôn
    u = refresh_profile()
    if u and u.get("locked") == 2:
        return -999

    total_coins = 0

    # 1. Quét tài khoản chính
    if init_web_account():
        coins, _ = scan_account_tasks(web_session, "Chính")
        if coins == -999:
            return -999
        total_coins += coins

    # 2. Xoay vòng tài khoản web phụ (Auto-Farm)
    if AUTO_FARM_ROTATION:
        s_fresh, fresh_user = create_fresh_web_session()
        if s_fresh and fresh_user:
            f_coins, _ = scan_account_tasks(s_fresh, f"Farm-{fresh_user[4:]}")
            if f_coins == -999:
                return -999
            total_coins += f_coins

    return total_coins


# =====================================================================
#  VÒNG LẶP CHÍNH: 1 PHÚT / LẦN & TỰ NGẮT KHI HẾT LƯỢT
# =====================================================================
def run_loop():
    while True:
        status = scan_and_redeem_giftcodes()

        u = refresh_profile()
        if u:
            log("COIN", f"Số dư hiện tại: {u.get('coins'):,} Xu", Fore.CYAN)

        # 👉 TỰ ĐỘNG NGẮT DỪNG BOT KHI BỊ CHẶN HOẶC HẾT LƯỢT
        if status == -999 or (u and u.get("locked") == 2):
            log("STOP", "Tài khoản đã đạt giới hạn GiftCode hôm nay (locked=2)! Dừng bot hoàn toàn.", Fore.RED)
            break

        log("SLEEP", f"Nghỉ {SCAN_INTERVAL_SECONDS}s (1 phút) trước khi quét chu kỳ tiếp...", Fore.WHITE)
        time.sleep(SCAN_INTERVAL_SECONDS)
