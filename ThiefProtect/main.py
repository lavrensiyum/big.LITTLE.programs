import os, time, psutil, ctypes, requests, cv2

chat_id = "test"

api_battery_notifier = "api.telegram.com // ... text=❗PC Şarjdan Çıkarıldı!"

api_url = "https://api.telegram.org/bot...."

def get_data():
        r = requests.get(api_battery_notifier)
        return r.status_code

def get_camera_picture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow("Görüntü", frame)
    cv2.waitKey(0)
    cv2.imwrite("goruntu.jpg", frame)

def sendPhoto(file):
    method = "sendPhoto"
    params = {'chat_id': chat_id}
    files = {'photo': file}
    resp = requests.post(api_url + method, params, files=files)
    return resp

while(True):

    time.sleep(2) 
    print("Battery percentage : ", psutil.sensors_battery().percent)

    if not hasattr(psutil, "sensors_battery"):
       print("platform not supported")

    batt = psutil.sensors_battery()

    if batt is None:
        print("no battery is installed")

    if batt.power_plugged:
        continue
    else:
        print("plugged in: no")
        get_data()  # Şarjdan çıkarıldı, telegrama mesaj atılıyor...
        time.sleep(3)

        