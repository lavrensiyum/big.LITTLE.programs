import os
import psutil
import time
import requests

api_battery_notifier = "https://api.telegram.org/bot------/sendMessage?chat_id=------&text="
api_url = "https://api.telegram.org/bot--------"

def get_data(ram_usage, ram_usage_gb):
        message = f"☁️ RAM kullanımı çok yüksek! RAM kullanımı: {ram_usage}%, {ram_usage_gb}"
        message = api_battery_notifier + message
        r = requests.get(message)
        return r.status_code
    
while True:
    # RAM kullanımını al
    ram_usage = psutil.virtual_memory().percent
    print(f"Current RAM usage is: {ram_usage}%, {psutil.virtual_memory().used / (1024 ** 3):.1f}GB")
    
    if ram_usage > 10:
        print("RAM usage is too high! Restarting the system...")
        ram_usage_gb = f"{psutil.virtual_memory().used / (1024 ** 3):.1f} GB"
        
        get_data(ram_usage, ram_usage_gb)
        
        # Sistem yeniden başlat
        #os.system("reboot")
        time.sleep(10)
    
    # 10 saniye bekleyin
    time.sleep(10)