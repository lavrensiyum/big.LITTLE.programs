import psutil, time, pyuac, ctypes, os, threading
import screen_brightness_control as sbc

main_brightness = sbc.get_brightness()

process_list = []

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

def monitor_processes():
    global process_list
    
    while True:
        try:
            current_processes = [proc.info['name'] for proc in psutil.process_iter(['name']) if proc.info['name']]
            process_list = current_processes
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

def brightness_control(target_brightness):
    current_brightness = sbc.get_brightness()
    str_num = ''.join(map(str, current_brightness))
    current_brightness = int(str_num)

    str_num2 = ''.join(map(str, target_brightness))
    target_brightness = int(str_num2)
    
    if current_brightness % 10 < 5:
        current_brightness = (current_brightness // 10) * 10  # Alt sınır
    else:
        current_brightness = (current_brightness // 10 + 1) * 10  # Üst sınır

    if current_brightness > target_brightness:
        for i in range(current_brightness):
            current_brightness -= 10
            sbc.set_brightness(current_brightness)
            time.sleep(0.4)
            print(sbc.get_brightness())
            if current_brightness == target_brightness:
                break
    else:
        while current_brightness < target_brightness:
            current_brightness += 10
            sbc.set_brightness(current_brightness)
            time.sleep(0.4)
            print(sbc.get_brightness())
            if current_brightness == target_brightness:
                break

def lock_screen_handler():
    global main_brightness
    time.sleep(5)

    while True:
        time.sleep(1)
        
        if "LogonUI.exe" in process_list:
            print("Lock screen triggered")
            time.sleep(2)
            trigger_screensaver()
            brightness_control([0])
            
            while True:
                if "WPXSCR~1.SCR" not in process_list:
                    print("Screen saver breaked")
                    brightness_control(main_brightness)
                    break
                else:
                    time.sleep(1)

        #print("Lock screen not triggered")
        time.sleep(1)
        main_brightness = sbc.get_brightness()
        #print("Current brightness: ", sbc.get_brightness())
        #print("Main brightness: ", main_brightness)


# Main fonksiyon
if __name__ == "__main__":
    process_list = []

    process_thread = threading.Thread(target=monitor_processes)
    process_thread.daemon = True
    process_thread.start()

    lock_screen_thread = threading.Thread(target=lock_screen_handler)
    lock_screen_thread.daemon = True
    lock_screen_thread.start()

    lock_screen_thread.join()
    process_thread.join()
