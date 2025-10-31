from pynput import keyboard
from time import perf_counter
# Collect events until released
startTime = 0
pressed = False
morseVariable = 0
morse_dictionary = {
    "a": ".-", "b": "-...", "c": "-.-.",
    "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-",
    "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
}

x = []

def on_press(key):
    global startTime, pressed
    if key == keyboard.Key.space and not pressed:
        startTime = perf_counter()
        pressed = True
            
def on_release(key):
    global startTime, pressed, holdtime
    if key == keyboard.Key.space and pressed:
        holdtime = perf_counter() - startTime
        morseVariable = holdtime
        if morseVariable < 0.25:
            dotOrDash = "."
            print(dotOrDash)
            x.append(dotOrDash)
        elif morseVariable > 0.25:
            dotOrDash = "-"
            print(dotOrDash)
            x.append(dotOrDash)
        #print(holdtime)
        letter = ''.join(x)
        print(letter)
        pressed = False
        startTime = 0
    if key == keyboard.Key.esc:
        # Stop listener
        return False

        
with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()

