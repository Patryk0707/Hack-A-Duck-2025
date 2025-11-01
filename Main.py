from pynput import keyboard
from time import perf_counter
import winsound,time
# Collect events until released
startTime = 0 #start time of when spacebar was pressed
pressed = False #if spacebar is pressed
morseVariable = 0 #lenth of spacebar being pressed
letter="" #letter variable used letter to store morsecode
dotMs=120#length of the beep in ms for dot
dashMs=120*3 #length of the beep in ms for dash
freq=800 #frequence of the beep
wordDone=False
morse_dictionary = {
    "a": ".-", "b": "-...", "c": "-.-.",
    "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-",
    "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..","0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",".": ".-.-.-",",": "--..--", "?": "..--.." 
}# dictionary of letters,numbers and symbols translated to morse code

z = 0
x = []
y=[]
finalWord = [] #final word being printed at the end
finalTranslation = []
def on_press(key):#when key(spacebar) is pressed it checks whether its the spacebar and that it hasnt been pressed yet.
    global startTime, pressed #global variables used
    if key == keyboard.Key.space and not pressed:
        startTime = perf_counter() #starts the timer since the button has been pressed
        pressed = True #updates pressed to be True
            
def on_release(key): #when key(spacebar) is released and pressed is true, it subracts perf_counter() by startTime to get the time the spacebar was held
    global startTime, pressed, holdtime,letter,wordDone
    if key == keyboard.Key.space and pressed:
        holdtime = perf_counter() - startTime
        morseVariable = holdtime
        if morseVariable <= 0.25: #if spacebar was held for less than 0.25 seconds then a "." is assigned and printed
            dotOrDash = "."
            print(dotOrDash)
            x.append(dotOrDash)#adds the dot into the list called x
            letter = ''.join(x)   #morsecode is added into variable called letter
            winsound.Beep(freq,dotMs)#when its a dot it makes a beep sound that uses freq and dotMs to know how long the frequency and length of the sound is
        elif morseVariable >= 0.25: #if spacebar is held for more than or equal to 0.25 seconds then a "-" is assigned and printed
            dotOrDash = "-" 
            print(dotOrDash)
            x.append(dotOrDash)#adds the dash into the list called x
            letter = ''.join(x)#morsecode is added into variable called letter
            winsound.Beep(freq,dashMs)#when its a dash it makes a longer beep sound that uses freq and dashMs to know how long the frequency and length of the sound is
        print(letter)
        pressed = False #pressed goes back to False
        startTime = 0 #resets startTime
    if key == keyboard.Key.esc:#pressing escape will then get the code to compare the morse code generated to the dictionary to see what letter its equilevent to
        for key, value in morse_dictionary.items():#uses the morse dictionary for a comparision to see what letter the morse code is 
            if value == letter:  #if the morse code matches any morsecode in the dictionary then that letter will be added to final world
                y.append(letter) #letter is stored in y
                x.clear() #x is cleared for a new entry
                finalWord.append(key) #letter is stored 
                print(key)
                break
        for i in letter:
            if i==".":
                winsound.Beep(freq,dotMs) #for every dot a beep is produced that is short
            elif i=="-":
                winsound.Beep(freq,dashMs) #for every dash a longer beep is produced
            time.sleep(dotMs/1000.0)#between every letter a gap of silence is given
        #return False returns false when its finished
    elif key== keyboard.Key.enter:
        if not x and not letter:
            return
        wordDone=True
        pressed=False
        startTime=0
        return False
print("Welcome to the Morse Code Translator!")
choice = input(f"Do you want to 1.) Translate English to Morse Code 2.) Translate Morse Code to English? ")#gives user the choice whether they want to go from english to morse code or morse code to english
while choice == "1":
    userText = str(input("What word would you like to translate? "))
    morse_code = "".join(morse_dictionary[letter] for letter in userText)#it gets every letter in the word, checks where it is in the dictonary and gets the morse code equilevent
    print(morse_code)#prints morse code equilevent
    for wordMorseCode in morse_code: #for every dot and dash in the morse code translation a shorter and longer beep is produced
        for s in wordMorseCode:
            if s==".": 
                winsound.Beep(freq,dotMs)
            elif s=="-":
                winsound.Beep(freq,dashMs)
            time.sleep(dotMs/1000.0)
    enterAgain=input("want to translate another word into morse code? ")
    if enterAgain == "y" or enterAgain == "yes":
        choice="1"
    else:
        choice="0"
if choice == "2":
        while z==0:
            with keyboard.Listener(     #starts to listen for spacebar presses
                    on_press = on_press,
                    on_release = on_release) as listener:
                listener.join()
            if wordDone:
                wordDone=False
                print(''.join(finalWord))
                for code in y:
                    for s in code:
                        if s == '.':
                            winsound.Beep(freq,dotMs)
                        elif s == '-':
                            winsound.Beep(freq,dashMs)
                        time.sleep(dotMs/1000.0)
                x.clear();y.clear();finalWord.clear();letter="";pressed=False;startTime=0
                _=input()
                goAgain = input("Another Word? (y/n)") #if user wants to go again z will be 0 meaning the loop will continue
                if goAgain == "y" or goAgain == "yes":
                    z=0
                else:
                    z=1