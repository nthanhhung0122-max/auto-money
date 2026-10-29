name: Auto Giftcode (Acc 1)

on:
  schedule:
    - cron: '*/5 * * * *'  # Quét liên tục mỗi 5 phút
  workflow_dispatch:

concurrency:
  group: giftcode-acc1
  cancel-in-progress: false

jobs:
  farm-giftcodes:
    runs-on: ubuntu-latest
    timeout-minutes: 350
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests telethon colorama beautifulsoup4

      - name: Chay Bot Giftcode Acc 1 (Tu dong bat lai sau 1 phut neu tat)
        env:
          TELEGRAM_SESSION_B64_ACC1: ${{ secrets.TELEGRAM_SESSION_B64_ACC1 }}
        run: |
          while true; do
            python auto_giftcode.py
            echo "Bot vua ket thuc, nghi 60 giay roi tu dong khoi dong lai..."
            sleep 60
          done
