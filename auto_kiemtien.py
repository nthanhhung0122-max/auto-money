



"""
====================================================================
  🏆 BOT ĐUA TOP XẾP HẠNG TELEGRAM: @kiemtien6789_bot (TÀI KHOẢN 1)
  🚀 TÍNH NĂNG ĐỘT PHÁ:
      - TỰ ĐỘNG LẤY INIT_DATA MỚI BẰNG TELETHON (Không bao giờ hết hạn)
      - Cho ăn (Boost+Đào 10/10)
      - Mở rương (10/10)
      - Trả lời câu hỏi (10/10)
      - Nhiệm vụ 1, 2, 3 (Monetag)
      - SAU KHI LÀM HẾT ➔ TỰ BẺ KHÓA VÀ NẠP SẠCH 26 GIFTCODE TELEPET
      - Tự động ngủ đến 00:00:05 GMT+7 mỗi ngày
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
# ─────────────────────────────────────────────────────────────────
#  CẤU HÌNH HỆ THỐNG - TÀI KHOẢN 1 (@hungzai22)
# ─────────────────────────────────────────────────────────────────
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
