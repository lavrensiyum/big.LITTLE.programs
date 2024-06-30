import psutil, time, pyuac, ctypes, os

import screen_brightness_control as sbc
from pynput.keyboard import Listener

main_brightness = sbc.get_brightness()

if not pyuac.isUserAdmin():
    print("Re-launching as admin")
    pyuac.runAsAdmin()

def clear():
    if os.name == 'nt':
        os.system('cls')

def trigger_screensaver():
    WM_SYSCOMMAND = 0x0112
    SC_SCREENSAVE = 0xF140
    HWND_BROADCAST = 0xFFFF

    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_SCREENSAVE, 0)

def brightness_control(target_brightness):

    current_brightness = sbc.get_brightness()
    str_num = ''.join(map(str, current_brightness))
    current_brightness = int(str_num)

    str_num2 = ''.join(map(str, target_brightness))
    target_brightness = int(str_num2)

    if current_brightness > target_brightness:
        for i in range(current_brightness):
            current_brightness-=10
            sbc.set_brightness(current_brightness)
            time.sleep(0.4)

            print(sbc.get_brightness())

            if current_brightness == target_brightness:
                break
    else:
        while current_brightness < target_brightness:
            current_brightness+=10
            sbc.set_brightness(current_brightness)
            time.sleep(0.4)

            print(sbc.get_brightness())

            if current_brightness == target_brightness:
                break

def on_press(key):
    listener.stop()
    
time.sleep(5)

while True:
    time.sleep(1)
    
    try:
    
        for proc in psutil.process_iter():
            #clear()

            if(proc.name() == "LogonUI.exe"):
                print ("Lock screen triggered")

                time.sleep(2)
                trigger_screensaver()

                brightness_control([0])

                with Listener(on_press=on_press) as listener:
                    listener.join()
                    brightness_control(main_brightness)

                brightness = sbc.get_brightness()

                time.sleep(1)
                
    except Exception as e:
        print(f'Error: {e}')
        time.sleep(1)
        continue

    print ("Lock screen not triggered")
    time.sleep(1)
    
    main_brightness = sbc.get_brightness()

    print("Current brightness: ", sbc.get_brightness())
    print("Main brightness: ", main_brightness)