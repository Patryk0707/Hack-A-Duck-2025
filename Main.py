from pynput import keyboard
from time import perf_counter
# Collect events until released
startTime = 0
pressed = False
morseVariable = 0
letter=""
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

z = 0
x = []
finalWord = []
finalTranslation = []
def on_press(key):
    global startTime, pressed
    if key == keyboard.Key.space and not pressed:
        startTime = perf_counter()
        pressed = True
            
def on_release(key):
    global startTime, pressed, holdtime,letter
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
            letter = ''.join(x)
        print(letter)
        pressed = False
        startTime = 0
    if key == keyboard.Key.esc:# Stop listener
        for key, value in morse_dictionary.items():
            if value == letter:
                x.clear()
                finalWord.append(key)
                print(key)
                break
        return False
choice = input(f"Do you want to 1.) Translate English to Morse Code 2.) Translate Morse Code to English")
if choice == "1":
    userText = str(input("What word would you like to translate"))
    morse_code = "".join(morse_dictionary[letter] for letter in userText)
    print(morse_code)
elif choice == "2":
    while z == 0:
        goAgain = input("Another letter? (Y/N)")
        if goAgain == "y":
            z = 0
        else:
            z = 1
            print(''.join(finalWord))
        with keyboard.Listener(
                on_press = on_press,
                on_release = on_release) as listener:
            listener.join()
    else:
        print("Please enter a valid selection")
