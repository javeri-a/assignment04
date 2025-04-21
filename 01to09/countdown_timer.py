import time

def countdown_timer():
    seconds = int(input("Enter the time in seconds: "))

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

countdown_timer()
