"""
====================================================================
  ðŸ† BOT ÄUA TOP Xáº¾P Háº NG TELEGRAM: @kiemtien6789_bot (TÃ€I KHOáº¢N 1)
  ðŸš€ TÃNH NÄ‚NG Äá»˜T PHÃ:
      - Tá»° Äá»˜NG Láº¤Y INIT_DATA Má»šI Báº°NG TELETHON (KhÃ´ng bao giá» háº¿t háº¡n)
      - Cho Äƒn (Boost+ÄÃ o 10/10)
      - Má»Ÿ rÆ°Æ¡ng (10/10)
      - Tráº£ lá»i cÃ¢u há»i (10/10)
      - Nhiá»‡m vá»¥ 1, 2, 3 (Monetag)
      - SAU KHI LÃ€M Háº¾T âž” Tá»° Báºº KHÃ“A VÃ€ Náº P Sáº CH 26 GIFTCODE TELEPET
      - Tá»± Ä‘á»™ng ngá»§ Ä‘áº¿n 00:00:05 GMT+7 má»—i ngÃ y
====================================================================
"""

import time
import random
import requests
import urllib.parse
import re
import os
import base64
import asyncio
from datetime import datetime, timezone, timedelta
from colorama import Fore, Style, init

from telethon import TelegramClient
from telethon.tl.functions.messages import RequestWebViewRequest

init(autoreset=True)

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#  Cáº¤U HÃŒNH Há»† THá»NG - TÃ€I KHOáº¢N 1 (@hungzai22)
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

API_ID = 39182276
API_HASH = "f02b155d895a3a3fbf8a1cbe810b5338"
SESSION_PATH = "telepet_acc1"

API_URL = "https://kien.kiemtienngay.us/public/api.php"
CURRENT_INIT_DATA = ""

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

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#  HÃ€M Tá»° Äá»˜NG XIN TELEGRAM Cáº¤P INIT_DATA Má»šI TOANH
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
async def fetch_fresh_init_data():
    global CURRENT_INIT_DATA
    log("ðŸ”‘", "Äang káº¿t ná»‘i Telegram Ä‘á»ƒ tá»± Ä‘á»™ng láº¥y init_data má»›i toanh...", Fore.CYAN)
    
    # KhÃ´i phá»¥c file session tá»« Secret náº¿u cháº¡y trÃªn GitHub Actions
    session_secret = os.getenv("TELEGRAM_SESSION_B64")
    if session_secret and not os.path.exists(f"{SESSION_PATH}.session"):
        try:
            with open(f"{SESSION_PATH}.session", "wb") as f:
                f.write(base64.b64decode(session_secret))
        except Exception as e:
            log("âš ï¸", f"KhÃ´ng thá»ƒ khÃ´i phá»¥c session tá»« Secret: {e}", Fore.YELLOW)

    client = TelegramClient(SESSION_PATH, API_ID, API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        log("âŒ", "Session chÆ°a Ä‘Æ°á»£c xÃ¡c thá»±c hoáº·c thiáº¿u file session!", Fore.RED)
        await client.disconnect()
        return None
    
    bot = await client.get_input_entity("kiemtien6789_bot")
    web_view = await client(RequestWebViewRequest(
        peer=bot,
        bot=bot,
        platform="android",
        from_bot_menu=False,
        url="https://kien.kiemtienngay.us/public/"
    ))
    await client.disconnect()

    fragment = urllib.parse.urlparse(web_view.url).fragment
    params = urllib.parse.parse_qs(fragment)
    CURRENT_INIT_DATA = params.get("tgWebAppData", [None])[0]
    log("âœ…", "ÄÃ£ láº¥y thÃ nh cÃ´ng init_data tÆ°Æ¡i má»›i tá»« Telegram!", Fore.GREEN)
    return CURRENT_INIT_DATA

def get_fresh_init_data_sync():
    return asyncio.run(fetch_fresh_init_data())

def api_call(action, extra=None):
    global CURRENT_INIT_DATA
    payload = {"action": action, "init_data": CURRENT_INIT_DATA}
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
    log("ðŸ¦´", "Kiá»ƒm tra nhiá»‡m vá»¥ Cho Äƒn...", Fore.CYAN)
    for i in range(progress["feed"], 10):
        api_call("tap_boost")
        time.sleep(1)
        res = api_call("tap")
        if res.get("ok"):
            progress["feed"] += 1
            log("âš¡", f"Cho Äƒn láº§n {progress['feed']}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
        else:
            err = res.get("error", "KhÃ´ng nháº­n Ä‘Æ°á»£c xu")
            log("âœ…", f"Cho Äƒn: {err} âž” Coi nhÆ° Ä‘Ã£ Ä‘á»§ 10 láº§n hÃ´m nay, xong!", Fore.YELLOW)
            progress["feed_done"] = True
            break
        time.sleep(1.5)
    progress["feed_done"] = True

def do_chest_tasks():
    global progress
    if progress["chest_done"]:
        return
    log("ðŸ“¦", "Kiá»ƒm tra nhiá»‡m vá»¥ Má»Ÿ rÆ°Æ¡ng...", Fore.CYAN)
    for i in range(progress["chest"], 10):
        res = api_call("chest")
        if res.get("ok"):
            progress["chest"] += 1
            log("ðŸŽ", f"Má»Ÿ rÆ°Æ¡ng láº§n {progress['chest']}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
        else:
            err = res.get("error", "KhÃ´ng nháº­n Ä‘Æ°á»£c xu")
            log("âœ…", f"Má»Ÿ rÆ°Æ¡ng: {err} âž” Coi nhÆ° Ä‘Ã£ Ä‘á»§ 10 láº§n hÃ´m nay, xong!", Fore.YELLOW)
            progress["chest_done"] = True
            break
        time.sleep(1.5)
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
    log("â“", "Kiá»ƒm tra nhiá»‡m vá»¥ Tráº£ lá»i cÃ¢u há»i...", Fore.CYAN)
    for i in range(progress["quiz"], 10):
        q_res = api_call("quiz_get")
        if not q_res.get("ok"):
            err = q_res.get("error", "KhÃ´ng láº¥y Ä‘Æ°á»£c cÃ¢u há»i")
            log("âœ…", f"CÃ¢u há»i: {err} âž” Coi nhÆ° Ä‘Ã£ Ä‘á»§ 10 láº§n hÃ´m nay, xong!", Fore.YELLOW)
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
            log("ðŸ§ ", f"CÃ¢u há»i {progress['quiz']}/10: Chá»n {opts[selected_idx]} âœ… (+{a_res.get('earned', 0)} coin)", Fore.GREEN)
        else:
            err = a_res.get("error", "Lá»—i tráº£ lá»i")
            log("âœ…", f"Tráº£ lá»i: {err} âž” Coi nhÆ° Ä‘Ã£ Ä‘á»§ 10 láº§n hÃ´m nay, xong!", Fore.YELLOW)
            progress["quiz_done"] = True
            break
        time.sleep(1.5)
    progress["quiz_done"] = True

def do_monetag_tasks():
    global progress
    for task_name, task_key, done_key in [
        ("Nhiá»‡m vá»¥ 1 (Monetag)", "task1", "task1_done"),
        ("Nhiá»‡m vá»¥ 2 (Monetag)", "task2", "task2_done"),
        ("Nhiá»‡m vá»¥ 3 (Monetag)", "task3", "task3_done"),
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
            log("ðŸŽ¬", f"{task_name} láº§n {progress[task_key]}/10: +{res.get('earned', 0)} coin", Fore.GREEN)
            if progress[task_key] >= 10:
                progress[done_key] = True
        else:
            err = res.get("error", "KhÃ´ng nháº­n Ä‘Æ°á»£c xu")
            log("âœ…", f"{task_name}: {err} âž” Coi nhÆ° Ä‘Ã£ hoÃ n thÃ nh 10/10 láº§n, Bá»Ž QUA!", Fore.GREEN)
            progress[done_key] = True
            progress[task_key] = 10
        time.sleep(1)

def do_extra_smartlinks():
    for task in EXTRA_TASKS:
        api_call(task)
        time.sleep(0.3)

def init_web_account():
    try:
        r = web_session.post("https://kiemtienngay.us/login.php", data={"username": WEB_USER, "password": WEB_PASS}, timeout=8)
        if "TÃ i khoáº£n:" not in r.text and "ÄÄƒng xuáº¥t" not in r.text:
            web_session.post("https://kiemtienngay.us/register.php", data={
                "username": WEB_USER,
                "password": WEB_PASS,
                "confirm_password": WEB_PASS,
                "referrer": ""
            }, timeout=8)
            web_session.post("https://kiemtienngay.us/login.php", data={"username": WEB_USER, "password": WEB_PASS}, timeout=8)
        return True
    except Exception as e:
        log("âŒ", f"Lá»—i Ä‘Äƒng nháº­p web kiemtienngay.us: {e}", Fore.RED)
        return False

def auto_claim_and_redeem_giftcodes():
    print(f"\n{Fore.MAGENTA}â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•{Style.RESET_ALL}")
    log("ðŸŽ", "Báº®T Äáº¦U Báºº KHÃ“A & Tá»° Äá»˜NG Náº P GIFTCODE TELEPET VÃ€O VÃ...", Fore.YELLOW)
    print(f"{Fore.MAGENTA}â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•{Style.RESET_ALL}")

    if not init_web_account():
        return 0

    try:
        r_home = web_session.get("https://kiemtienngay.us/index.php", timeout=8)
        task_links = re.findall(r'href=[\'"]([^\'"]*giftcode\.php\?task_id=\d+)[\'"]', r_home.text)
        task_ids = sorted(list(set([re.search(r'task_id=(\d+)', l).group(1) for l in task_links])), key=lambda x: int(x))
    except Exception as e:
        log("âŒ", f"KhÃ´ng láº¥y Ä‘Æ°á»£c danh sÃ¡ch task: {e}", Fore.RED)
        return 0

    log("ðŸ“‹", f"TÃ¬m tháº¥y {len(task_ids)} nhiá»‡m vá»¥ GiftCode. Äang tiáº¿n hÃ nh báº» khÃ³a vÃ  nháº­p tá»± Ä‘á»™ng...", Fore.CYAN)

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
                        "init_data": CURRENT_INIT_DATA
                    }
                    r_tele = requests.post(API_URL, headers=headers_telepet, data=redeem_data, timeout=8)
                    res_tele = r_tele.json()

                    if res_tele.get("ok"):
                        earned = res_tele.get("amount", reward_val)
                        total_coins_earned += earned
                        success_count += 1
                        log("ðŸŽ‰", f"Task #{tid} (LÆ°á»£t {round_num}): MÃ£ [{code}] âž” +{earned:,} Xu Ä‘Ã£ náº¡p thÃ nh cÃ´ng!", Fore.GREEN)
                    else:
                        log("âš ï¸", f"Task #{tid}: MÃ£ [{code}] âž” {res_tele.get('error', 'Lá»—i nháº­p')}", Fore.YELLOW)
            except:
                pass
            time.sleep(1)

    log("ðŸ", f"Tá»”NG Káº¾T GIFTCODE: Nháº­p thÃ nh cÃ´ng {success_count} mÃ£ | Tá»•ng thu vá»: +{total_coins_earned:,} Xu!", Fore.GREEN)
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
{Fore.YELLOW}â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘  ðŸ“Š Báº¢NG TIáº¾N Äá»˜ NHIá»†M Vá»¤ Xáº¾P Háº NG TRONG NGÃ€Y                     â•‘
â• â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•£
â•‘  ðŸ¦´ Cho Äƒn (Boost+ÄÃ o)  : {progress['feed']:>2}/10  {'âœ… Xong' if progress['feed_done'] else 'â³ Äang lÃ m'}
â•‘  ðŸ“¦ Má»Ÿ rÆ°Æ¡ng            : {progress['chest']:>2}/10  {'âœ… Xong' if progress['chest_done'] else 'â³ Äang lÃ m'}
â•‘  â“ Tráº£ lá»i cÃ¢u há»i     : {progress['quiz']:>2}/10  {'âœ… Xong' if progress['quiz_done'] else 'â³ Äang lÃ m'}
â•‘  ðŸŽ¬ Nhiá»‡m vá»¥ 1 (Monetag): {progress['task1']:>2}/10  {'âœ… Xong' if progress['task1_done'] else 'â³ Äang lÃ m'}
â•‘  ðŸŽ¬ Nhiá»‡m vá»¥ 2 (Monetag): {progress['task2']:>2}/10  {'âœ… Xong' if progress['task2_done'] else 'â³ Äang lÃ m'}
â•‘  ðŸŽ¬ Nhiá»‡m vá»¥ 3 (Monetag): {progress['task3']:>2}/10  {'âœ… Xong' if progress['task3_done'] else 'â³ Äang lÃ m'}
â•‘  ðŸŽ Nháº­p toÃ n bá»™ Giftcode:      {'âœ… ÄÃ£ nháº­p sáº¡ch' if progress.get('giftcode_done') else 'â³ Äang chá»...'}
â• â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•£
â•‘  ðŸ’° Sá»‘ dÆ° hiá»‡n táº¡i      : {coins:>10,} Coins (~{coins*0.02:,.2f} VNÄ)
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•{Style.RESET_ALL}""")

def reset_daily_progress():
    global progress
    progress = {
        "feed": 0, "chest": 0, "quiz": 0,
        "task1": 0, "task2": 0, "task3": 0,
        "feed_done": False, "chest_done": False, "quiz_done": False,
        "task1_done": False, "task2_done": False, "task3_done": False,
        "giftcode_done": False,
    }
    log("ðŸŒ…", "ÄÃƒ SANG NGÃ€Y Má»šI (00:00 GMT+7)! RESET Báº¢NG TIáº¾N Äá»˜ Äá»‚ ÄUA TOP!", Fore.GREEN)

def main():
    print(f"""
{Fore.YELLOW}â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘  ðŸ† BOT ÄUA TOP Xáº¾P Háº NG 24/7 - Tá»° Äá»˜NG Láº¤Y INIT_DATA             â•‘
â•‘  ðŸ“Œ TÃ i khoáº£n: @hungzai22                                        â•‘
â•‘  ðŸ”‘ Auto láº¥y init_data má»›i toanh tá»« Telegram má»—i chu ká»³           â•‘
â•‘  ðŸŽ Sau Ä‘Ã³: Tá»± Ä‘á»™ng báº» khÃ³a vÃ  náº¡p sáº¡ch 26 GiftCode TelePet      â•‘
â•‘  ðŸŒ™ HoÃ n táº¥t âž” Ngá»§ Ä‘áº¿n 00:00 GMT+7 thá»©c dáº­y cháº¡y tiáº¿p            â•‘
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•{Style.RESET_ALL}
    """)

    # 1. Tá»± Ä‘á»™ng láº¥y init_data má»›i tá»« Telegram Client
    get_fresh_init_data_sync()

    curr_u = refresh_profile()
    if curr_u:
        log("ðŸ‘¤", f"ÄÄƒng nháº­p thÃ nh cÃ´ng: {curr_u.get('name')} (@{curr_u.get('username')}) | Sá»‘ dÆ°: {curr_u.get('coins'):,} Coins", Fore.GREEN)
    else:
        log("âŒ", "KhÃ´ng thá»ƒ xÃ¡c thá»±c vá»›i mÃ¡y chá»§ TelePet!", Fore.RED)
        return

    while True:
        # 1. Cháº¡y Cho Äƒn
        do_feed_tasks()

        # 2. Cháº¡y Má»Ÿ rÆ°Æ¡ng
        do_chest_tasks()

        # 3. Cháº¡y Tráº£ lá»i cÃ¢u há»i
        do_quiz_tasks()

        # 4. Cháº¡y Nhiá»‡m vá»¥ 1, 2, 3 (Monetag)
        do_monetag_tasks()

        # 5. CÃ y phá»¥ Smartlinks
        do_extra_smartlinks()

        # In báº£ng Ä‘iá»u khiá»ƒn
        curr_u = refresh_profile()
        print_dashboard(curr_u)

        # ðŸ‘‰ SAU KHI LÃ€M XONG TOÃ€N Bá»˜ CÃC BÆ¯á»šC TRÃŠN âž” Láº¬P Tá»¨C ÄI CÃ€O VÃ€ NHáº¬P 26 GIFTCODE
        if not progress.get("giftcode_done"):
            auto_claim_and_redeem_giftcodes()
            progress["giftcode_done"] = True
            curr_u = refresh_profile()
            print_dashboard(curr_u)

        # TÃNH THá»œI GIAN NGá»¦ Äáº¾N 00:00 GMT+7
        sec_to_midnight = get_seconds_until_midnight_vn()
        hrs, rem = divmod(sec_to_midnight, 3600)
        mins, secs = divmod(rem, 60)

        print("\n" + "="*66)
        log("ðŸŽ‰", "Táº¤T Cáº¢ NHIá»†M Vá»¤ & GIFTCODE TRONG NGÃ€Y ÄÃƒ HOÃ€N Táº¤T!", Fore.GREEN)
        log("ðŸŒ™", f"Cho bot ngá»§ Ä‘áº¿n 00:00:05 GMT+7 ngÃ y mai (cÃ²n {hrs}h {mins}m {secs}s)...", Fore.MAGENTA)
        print("="*66 + "\n")

        time.sleep(sec_to_midnight)
        reset_daily_progress()
        # Sang ngÃ y má»›i tá»± Ä‘á»™ng xin cáº¥p init_data má»›i toanh
        get_fresh_init_data_sync()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}â›” ÄÃ£ dá»«ng bot.{Style.RESET_ALL}")
