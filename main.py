from morse_code_translator.translator import translate_to_morse

codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...=",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " "
}


def morse(txt):
    code = ""

    for char in text:
        code += codes[char]
    return code


def supported(txt):
    for char in txt:
        if char not in codes:
            return False
    return True


text = input("Enter a string you wish to convert into Morse Code: ").lower()


# if supported(text):
#     print(f"The morse code for {text} is {morse(text)}")
# else:
#     print("Sorry, some characters in your string are not supported. Please try again.")

print(translate_to_morse(text))