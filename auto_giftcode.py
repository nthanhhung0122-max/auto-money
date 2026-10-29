{Fore.MAGENTA}====================================================================
|  TOOL QUET & BE KHOA GIFTCODE TELEPET 24/7 (TOI UU NANG CAO)     |
|  Tai khoan: @hungzai22 (ID: 7744031191)                          |
|  - Chu ky quet: {SCAN_INTERVAL_SECONDS} giay / lan                             |
|  - Che do Auto-Farm vo han: {'BAT' if AUTO_FARM_ROTATION else 'TAT'}                                 |
|  - Tu dong lay token init_data tu Telegram                       |
|  - Tu dong be khoa moi link rut gon & nap xu truc tiep          |
|  - Tu dong ngat bot khi bi chan hoac cham gioi han ngay         |
===================================================================={Style.RESET_ALL}
    """)
    # 1. Lay token khoi dong
    get_fresh_init_data_sync()
    curr_u = refresh_profile()
    if curr_u:
        log("LOGIN", f"Ket noi: {curr_u.get('name')} (@{curr_u.get('username')}) | Xu: {curr_u.get('coins'):,}", Fore.GREEN)
        # Tự ngắt ngay từ đầu nếu nick đã chạm ngưỡng khóa hôm nay
        if curr_u.get("locked") == 2:
            log("LIMIT", "Tai khoan da cham gioi han GiftCode trong ngay (locked=2)! Tu dong ngat bot.", Fore.YELLOW)
            return
    else:
        log("ERR", "Khong the xac thuc Telegram WebApp!", Fore.RED)
        return
    last_refresh_time = time.time()
    while True:
        # Kiem tra neu sang ngay moi thi reset ma da nap
        if get_seconds_until_midnight_vn() <= 10:
            REDEEMED_CODES_TODAY.clear()
            log("RESET", "DA SANG NGAY MOI! Reset danh sach ma va lay init_data moi...", Fore.GREEN)
            get_fresh_init_data_sync()
            time.sleep(15)
        # Tu dong lam moi token Telethon moi 2 tieng de khong bao gio bi timeout
        if time.time() - last_refresh_time > 7200:
            get_fresh_init_data_sync()
            last_refresh_time = time.time()
        # Quet va nap giftcode
        status = scan_and_redeem_giftcodes()
        u = refresh_profile()
        if u:
            log("COIN", f"So du hien tai: {u.get('coins'):,} Coins", Fore.CYAN)
        # 👉 TỰ ĐỘNG NGẮT HOÀN TOÀN KHI KHÔNG THỂ NHẬP NỮA:
        if status == -999 or (u and u.get("locked") == 2):
            log("STOP", "Tai khoan da dat gioi han toi da GiftCode (locked=2)! Tu dong ngat bot hoan toan.", Fore.RED)
            break
        else:
            log("SLEEP", f"Nghi {SCAN_INTERVAL_SECONDS}s (1 phut) truoc khi quet chu ky tiep theo...", Fore.WHITE)
            time.sleep(SCAN_INTERVAL_SECONDS)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[STOP] Da dung bot quet GiftCode.{Style.RESET_ALL}")
