import time
import requests
from flask import Flask

# رابطك
LINK = "https://sprlv.link/lala54321"

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running! Your link: " + LINK

def run_bot():
    print("بدأ البوت...")
    while True:
        try:
            r = requests.get(LINK, timeout=10)
            print(f"تمت الزيارة - الحالة: {r.status_code}")
        except Exception as e:
            print(f"خطأ: {e}")
        time.sleep(60) # يزور كل دقيقة

# لتشغيل البوت والخادم مع بعض
import threading
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
