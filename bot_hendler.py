import requests
from cinfig_manager import set_system_status

token = "YOUR TELEGRAM BOT TOKEN HERE"
chat_id = "YOUR TELEGRAM CHAT_ID HERE"
last_update_id = 0

def send_telegram_msg(msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    try:
        # Timeout 5 second ka hai, fast response dega
        requests.get(url, timeout=5)
        print("Telegram Msg: Sent")
    except:
        print("Telegram Msg: Timeout/Failed")

def send_telegram_photo(photo_path):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    try:
        with open(photo_path, 'rb') as photo:
            requests.post(url, data={'chat_id': chat_id}, files={'photo': photo}, timeout=10)
        print("Telegram Photo: Sent")
    except:
        print("Telegram Photo: Timeout/Failed")

def check_telegram_for_reset():
    global last_update_id
    url = f"https://api.telegram.org/bot{token}/getUpdates?offset={last_update_id+1}"
    try:
        response = requests.get(url,timeout=5).json()
        if response["result"]:
            for update in response["result"]:
                last_update_id = update["update_id"]
                msg_text = update["message"]["text"].lower().strip()
                if msg_text == "ok":
                    print("telegram command received: ok. Resetting status")
                    set_system_status("open")
    except Exception as e:
        print(f"error checking Telegram: {e}")
    return False
    
