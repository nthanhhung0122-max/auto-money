"""
====================================================================
  🏆 BOT ĐUA TOP XẾP HẠNG TELEGRAM: @kiemtien6789_bot (TÀI KHOẢN 1)
  🎯 Mục tiêu: 
      - Tự động nhận diện nhiệm vụ đã hoàn thành ➔ Bỏ qua ngay
      - Không chờ đợi cooldown nếu đã làm đủ 10 lần
      - Nhập sạch sẽ toàn bộ 26 GiftCode TelePet (~130,000 Xu)
      - Ngủ đến 00:00 GMT+7 thức dậy cày tiếp ngày mới
====================================================================
"""

import time
import random
import requests
import urllib.parse
import re
from datetime import datetime, timezone, timedelta
from colorama import Fore, Style, init

init(autoreset=True)

# ─────────────────────────────────────────────────────────────────
#  CẤU HÌNH HỆ THỐNG - TÀI KHOẢN 1 (@hungzai22)
# ─────────────────────────────────────────────────────────────────

API_URL = "https://kien.kiemtienngay.us/public/api.php"

INIT_DATA = (
    "query_id=AAHXiZRNAwAAANeJlE2H47ZQ"
    "&user=%7B%22id%22%3A7744031191%2C%22first_name%22%3A%22uv%E1%BB%B7ctctccc%22%2C"
    "%22last_name%22%3A%22Gochifi%22%2C%22username%22%3A%22hungzai22%22%2C"
    "%22language_code%22%3A%22vi%22%2C%22allows_write_to_pm%22%3Atrue%2C"
    "%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2F"
    "Zmiju56Xdg-UDWFdmDQaUJbLaUx3f7I4_rH3UQWwoh_acL4656EtBRjrDDLSPb-B.svg%22%7D"
    "&auth_date=1793107270"
    "&signature=hpWdv18dYB0b5W11aLe8J2O5Mgyu_YTg5NqTupigiv1_pzNCyM3Atx47qjkFXIR5j7cx4QU88NP9Y9eCUP3mBg"
    "&hash=729fbba3ca0c5ba330e7ae79313580bc4d4016ea8d8b8da7b765584c406d0999"
)

HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "WebKit/537.36 (KHTML, like Gecko) "
        "Chrome/155.0.0.0 Safari/537.36"
    ),
    "origin": "https://kien.kiemtienngay.us",
    "referer": "https://kien.kiemtienngay.us/public/index.php",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "accept": "*/*",
}

EXTRA_TASKS = [
    "task6", "task9", "task10", "task11", "task12", "task13", "task14", "task15",
    "task16", "task17", "task18", "task19", "task20", "task21", "task22", "task23",
    "task24", "task25", "task26", "task27", "task28", "task29", "task30", "task31",
    "task32", "task33", "task34", "task35", "task36", "task37"
]

progress = {
    "feed": 0, "chest": 0, "quiz": 0,
    "task1": 0, "task2": 0, "task3": 0,
    "feed_done": False, "chest_done": False, "quiz_done": False,
    "task1_done": False, "task2_done": False, "task3_done": False,
    "giftcode_done": False,
}

web_session = requests.Session()
WEB_USER = "hungzai_bot2026"
WEB_PASS = "Pass123456@"

def log(icon, msg, color=Fore.WHITE):
    t = datetime.now().strftime("%H:%M:%S")
    print(f"[{t}] {icon} {color}{msg}{Style.RESET_ALL}", flush=True)

def api_call(action, extra=None):
    payload = {"action": action, "init_data": INIT_DATA}
    if extra:
        payload.update(extra)
    try:
        r = requests.post(API_URL, headers=HEADERS, data=payload, timeout=12)
        return r.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}

def refresh_profile():
    res = api_call("me")
    if res.get("ok"):
        return res.get("user")
    return None

def do_feed_tasks():
    global progress
    if progress["feed_done"]:
        return
    log("🦴", "Kiểm tra nhiệm vụ Cho ăn...", Fore.CYAN)
    for i in range(progress["feed"], 10):
        api_call("tap_boost")
        time.sleep(1)
        res = api_call("tap")
        if res.get("ok"):
            progress["feed"] += 1
            log("⚡", f"Cho ăn lần {progress['feed']}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
        else:
            err = res.get("error", "")
            log("ℹ️", f"Cho ăn: {err} ➔ Đánh dấu xong!", Fore.YELLOW)
            progress["feed_done"] = True
            break
        time.sleep(1.5)
    if progress["feed"] >= 10:
        progress["feed_done"] = True

def do_chest_tasks():
    global progress
    if progress["chest_done"]:
        return
    log("📦", "Kiểm tra nhiệm vụ Mở rương...", Fore.CYAN)
    for i in range(progress["chest"], 10):
        res = api_call("chest")
        if res.get("ok"):
            progress["chest"] += 1
            log("🎁", f"Mở rương lần {progress['chest']}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
        else:
            err = res.get("error", "")
            log("ℹ️", f"Mở rương: {err} ➔ Đánh dấu xong!", Fore.YELLOW)
            progress["chest_done"] = True
            break
        time.sleep(1.5)
    if progress["chest"] >= 10:
        progress["chest_done"] = True

def solve_math(q):
    m = re.search(r"(\d+)\s*([\+\-\*])\s*(\d+)", q)
    if m:
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
    return None

def do_quiz_tasks():
    global progress
    if progress["quiz_done"]:
        return
    log("❓", "Kiểm tra nhiệm vụ Trả lời câu hỏi...", Fore.CYAN)
    for i in range(progress["quiz"], 10):
        q_res = api_call("quiz_get")
        if not q_res.get("ok"):
            err = q_res.get("error", "")
            log("ℹ️", f"Câu hỏi: {err} ➔ Đánh dấu xong!", Fore.YELLOW)
            progress["quiz_done"] = True
            break
        q_text = q_res.get("question", "")
        opts = q_res.get("options", [])
        correct_ans = solve_math(q_text)
        selected_idx = 0
        if correct_ans is not None:
            for idx, opt in enumerate(opts):
                if str(correct_ans) in str(opt):
                    selected_idx = idx
                    break
        a_res = api_call("quiz_answer", {"selected": selected_idx})
        if a_res.get("ok"):
            progress["quiz"] += 1
            log("🧠", f"Câu hỏi {progress['quiz']}/10: Chọn {opts[selected_idx]} ✅ (+{a_res.get('earned', 0)} coin)", Fore.GREEN)
        else:
            err = a_res.get("error", "")
            log("ℹ️", f"Trả lời: {err} ➔ Đánh dấu xong!", Fore.YELLOW)
            progress["quiz_done"] = True
            break
        time.sleep(1.5)
    if progress["quiz"] >= 10:
        progress["quiz_done"] = True

def do_monetag_tasks():
    global progress
    for task_name, task_key, done_key in [
        ("Nhiệm vụ 1 (Monetag)", "task1", "task1_done"),
        ("Nhiệm vụ 2 (Monetag)", "task2", "task2_done"),
        ("Nhiệm vụ 3 (Monetag)", "task3", "task3_done"),
    ]:
        if progress[done_key]:
            continue
        curr_count = progress[task_key]
        if curr_count >= 10:
            progress[done_key] = True
            continue
        res = api_call(f"task_monetag_{task_key[-1]}")
        if res.get("ok"):
            progress[task_key] += 1
            log("🎬", f"{task_name} lần {progress[task_key]}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
            if progress[task_key] >= 10:
                progress[done_key] = True
        else:
            err = res.get("error", "")
            # NẾU ĐÃ HẾT LƯỢT HOẶC ĐẠT TỐI ĐA ➔ ĐÁNH DẤU XONG NGAY LẬP TỨC
            if "tối đa" in err.lower() or "hết" in err.lower() or "10 lần" in err.lower():
                log("✅", f"{task_name}: Đã đạt tối đa 10/10 lần hôm nay ➔ Bỏ qua!", Fore.GREEN)
                progress[done_key] = True
                progress[task_key] = 10
            elif "chờ" in err.lower() or "10 phút" in err.lower():
                log("⏳", f"{task_name}: Đang trong thời gian Cooldown.", Fore.LIGHTBLACK_EX)
        time.sleep(1)

def do_extra_smartlinks():
    for task in EXTRA_TASKS:
        api_call(task)
        time.sleep(0.3)

def init_web_account():
    try:
        r = web_session.post("https://kiemtienngay.us/login.php", data={"username": WEB_USER, "password": WEB_PASS}, timeout=8)
        if "Tài khoản:" not in r.text and "Đăng xuất" not in r.text:
            web_session.post("https://kiemtienngay.us/register.php", data={
                "username": WEB_USER,
                "password": WEB_PASS,
                "confirm_password": WEB_PASS,
                "referrer": ""
            }, timeout=8)
            web_session.post("https://kiemtienngay.us/login.php", data={"username": WEB_USER, "password": WEB_PASS}, timeout=8)
        return True
    except Exception as e:
        log("❌", f"Lỗi đăng nhập web kiemtienngay.us: {e}", Fore.RED)
        return False

def auto_claim_and_redeem_giftcodes():
    print(f"\n{Fore.MAGENTA}══════════════════════════════════════════════════════════════════{Style.RESET_ALL}")
    log("🎁", "BẮT ĐẦU BẺ KHÓA & TỰ ĐỘNG NẠP GIFTCODE TELEPET VÀO VÍ...", Fore.YELLOW)
    print(f"{Fore.MAGENTA}══════════════════════════════════════════════════════════════════{Style.RESET_ALL}")

    if not init_web_account():
        return 0

    try:
        r_home = web_session.get("https://kiemtienngay.us/index.php", timeout=8)
        task_links = re.findall(r'href=[\'"]([^\'"]*giftcode\.php\?task_id=\d+)[\'"]', r_home.text)
        task_ids = sorted(list(set([re.search(r'task_id=(\d+)', l).group(1) for l in task_links])), key=lambda x: int(x))
    except Exception as e:
        log("❌", f"Không lấy được danh sách task: {e}", Fore.RED)
        return 0

    log("📋", f"Tìm thấy {len(task_ids)} nhiệm vụ GiftCode. Đang tiến hành bẻ khóa và nhập tự động...", Fore.CYAN)

    total_coins_earned = 0
    success_count = 0

    headers_telepet = {
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://kien.kiemtienngay.us',
        'referer': 'https://kien.kiemtienngay.us/public/nhiemvu.php',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for round_num in [1, 2]:
        for tid in task_ids:
            url = f"https://kiemtienngay.us/nbk222/giftcode.php?task_id={tid}"
            try:
                r = web_session.get(url, allow_redirects=False, timeout=8)
                loc = r.headers.get("Location", "")
                if not loc:
                    continue

                parsed = urllib.parse.urlparse(loc)
                target_url = urllib.parse.parse_qs(parsed.query).get("url", [None])[0]
                if not target_url:
                    continue

                headers_gift = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Referer': target_url
                }
                r_claim = web_session.post(target_url, data="confirm_gift=1", headers=headers_gift, timeout=8)
                data = r_claim.json()

                if data.get("status") == "ok":
                    code = data.get("code")
                    reward_str = str(data.get("reward", "5000")).replace(",", "")
                    reward_val = int(reward_str) if reward_str.isdigit() else 5000

                    redeem_data = {
                        "action": "giftcode",
                        "code": code,
                        "init_data": INIT_DATA
                    }
                    r_tele = requests.post(API_URL, headers=headers_telepet, data=redeem_data, timeout=8)
                    res_tele = r_tele.json()

                    if res_tele.get("ok"):
                        earned = res_tele.get("amount", reward_val)
                        total_coins_earned += earned
                        success_count += 1
                        log("🎉", f"Task #{tid} (Lượt {round_num}): Mã [{code}] ➔ +{earned:,} Xu đã nạp thành công!", Fore.GREEN)
                    else:
                        log("⚠️", f"Task #{tid}: Mã [{code}] ➔ {res_tele.get('error', 'Lỗi nhập')}", Fore.YELLOW)
            except:
                pass
            time.sleep(1)

    log("🏁", f"TỔNG KẾT GIFTCODE: Nhập thành công {success_count} mã | Tổng thu về: +{total_coins_earned:,} Xu!", Fore.GREEN)
    return total_coins_earned

def is_all_ranking_tasks_completed():
    return (
        progress["feed_done"] and
        progress["chest_done"] and
        progress["quiz_done"] and
        progress["task1_done"] and
        progress["task2_done"] and
        progress["task3_done"]
    )

def get_seconds_until_midnight_vn():
    vn_tz = timezone(timedelta(hours=7))
    now_vn = datetime.now(vn_tz)
    tomorrow = now_vn.date() + timedelta(days=1)
    midnight = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 5, tzinfo=vn_tz)
    return int((midnight - now_vn).total_seconds())

def print_dashboard(user):
    coins = user.get("coins", 0) if user else 0
    print(f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════════════════╗
║  📊 BẢNG TIẾN ĐỘ NHIỆM VỤ XẾP HẠNG TRONG NGÀY                     ║
╠══════════════════════════════════════════════════════════════════╣
║  🦴 Cho ăn (Boost+Đào)  : {progress['feed']:>2}/10  {'✅ Xong' if progress['feed_done'] else '⏳ Đang làm'}
║  📦 Mở rương            : {progress['chest']:>2}/10  {'✅ Xong' if progress['chest_done'] else '⏳ Đang làm'}
║  ❓ Trả lời câu hỏi     : {progress['quiz']:>2}/10  {'✅ Xong' if progress['quiz_done'] else '⏳ Đang làm'}
║  🎬 Nhiệm vụ 1 (Monetag): {progress['task1']:>2}/10  {'✅ Xong' if progress['task1_done'] else '⏳ Đang làm'}
║  🎬 Nhiệm vụ 2 (Monetag): {progress['task2']:>2}/10  {'✅ Xong' if progress['task2_done'] else '⏳ Đang làm'}
║  🎬 Nhiệm vụ 3 (Monetag): {progress['task3']:>2}/10  {'✅ Xong' if progress['task3_done'] else '⏳ Đang làm'}
║  🎁 Nhập toàn bộ Giftcode:      {'✅ Đã nhập sạch' if progress.get('giftcode_done') else '⏳ Chờ xong 10/10'}
╠══════════════════════════════════════════════════════════════════╣
║  💰 Số dư hiện tại      : {coins:>10,} Coins (~{coins*0.02:,.2f} VNĐ)
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

def reset_daily_progress():
    global progress
    progress = {
        "feed": 0, "chest": 0, "quiz": 0,
        "task1": 0, "task2": 0, "task3": 0,
        "feed_done": False, "chest_done": False, "quiz_done": False,
        "task1_done": False, "task2_done": False, "task3_done": False,
        "giftcode_done": False,
    }
    log("🌅", "ĐÃ SANG NGÀY MỚI (00:00 GMT+7)! RESET BẢNG TIẾN ĐỘ ĐỂ ĐUA TOP!", Fore.GREEN)

def main():
    print(f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════════════════╗
║  🏆 BOT ĐUA TOP XẾP HẠNG 24/7 - FILE GỐC (@hungzai22)            ║
║  📌 Mục tiêu: Hoàn tất 10 lần Cho ăn, Rương, Quiz, NV 1-2-3     ║
║  🎁 Xong 10/10 ➔ Tự động bẻ khóa và nhập sạch 26 GiftCode      ║
║  🌙 Hoàn tất ➔ Ngủ đến 00:00 GMT+7 thức dậy chạy tiếp            ║
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)

    u = refresh_profile()
    if not u:
        log("❌", "Token INIT_DATA không hợp lệ hoặc đã hết hạn!", Fore.RED)
        return

    log("👤", f"Tài khoản: {u.get('name')} (@{u.get('username')})", Fore.GREEN)

    while True:
        # 1. Chạy Cho ăn
        do_feed_tasks()

        # 2. Chạy Mở rương
        do_chest_tasks()

        # 3. Chạy Trả lời câu hỏi
        do_quiz_tasks()

        # 4. Chạy Nhiệm vụ 1, 2, 3 (Monetag)
        do_monetag_tasks()

        # 5. Cày phụ Smartlinks trong lúc rảnh
        do_extra_smartlinks()

        # Cập nhật số dư & In bảng điều khiển
        curr_u = refresh_profile()
        print_dashboard(curr_u)

        # 6. KIỂM TRA ĐÃ HOÀN THÀNH 10/10 TẤT CẢ CHƯA
        if is_all_ranking_tasks_completed():
            print("\n" + "="*66)
            log("🎉", "CHÚC MỪNG! ĐÃ HOÀN THÀNH 10/10 TẤT CẢ NHIỆM VỤ XẾP HẠNG HÔM NAY!", Fore.GREEN)
            print("="*66)

            # 👉 SAU KHI LÀM HẾT TẤT CẢ NHIỆM VỤ ➔ BẮT ĐẦU ĐI NHẬP HẾT TOÀN BỘ GIFTCODE
            if not progress.get("giftcode_done"):
                auto_claim_and_redeem_giftcodes()
                progress["giftcode_done"] = True
                curr_u = refresh_profile()
                print_dashboard(curr_u)

            sec_to_midnight = get_seconds_until_midnight_vn()
            hrs, rem = divmod(sec_to_midnight, 3600)
            mins, secs = divmod(rem, 60)

            log("🌙", f"Đã xong nhiệm vụ + nhập sạch Giftcode! Cho bot ngủ đến 00:00:05 GMT+7 ngày mai (còn {hrs}h {mins}m {secs}s)...", Fore.MAGENTA)
            print("="*66 + "\n")

            time.sleep(sec_to_midnight)
            reset_daily_progress()
            continue

        log("⏳", "Chờ 10 phút hồi Cooldown của Nhiệm Vụ 1-2-3 để làm lượt tiếp theo...", Fore.LIGHTBLACK_EX)
        for remaining in range(600, 0, -10):
            mins, secs = divmod(remaining, 60)
            print(f"\r{Fore.CYAN}⏰ Lượt tiếp theo sẽ chạy sau: {mins:02d}:{secs:02d}... {Style.RESET_ALL}", end="", flush=True)
            time.sleep(10)
        print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⛔ Đã dừng bot.{Style.RESET_ALL}")
