from pynput import keyboard
from time import perf_counter
# Collect events until released
startTime=0
pressed=False
def on_press(key):
    global startTime,pressed
    if key==keyboard.Key.space and not pressed:
        startTime=perf_counter()
        pressed=True
            
            

def on_release(key):
    global startTime,pressed
    if key==keyboard.Key.space and pressed:
        holdtime=perf_counter()-startTime
        print(holdtime)
        pressed=False
        startTime=0
    if key == keyboard.Key.esc:
        # Stop listener
        return False
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
