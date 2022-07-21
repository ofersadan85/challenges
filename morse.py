easy = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
hard = "0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000"

MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "&",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@",
    "...---...": "SOS",
}


def time_units(bits, check="1"):
    other = "0" if check == "1" else "1"
    bits = bits.strip("0")
    items = [b for b in bits.split(other) if b]
    try:
        min_items = len(min(items, key=len))
    except ValueError:
        min_items = 0
    try:
        max_items = len(max(items, key=len))
    except ValueError:
        max_items = 0
    return min_items, max_items


def decode_bits(bits):
    bits = bits.strip("0")
    unit = time_units(bits)[0]
    result = ""
    words = bits.split("0" * 7 * unit)
    for w in words:
        chars = w.split("0" * 3 * unit)
        for c in chars:
            c = c.replace("1" * 3 * unit, "-")
            c = c.replace("1" * unit, ".")
            result += c.replace("0", "") + " "
        result += "   "
    return result


def decode_morse(morse_code):
    result = []
    for word in morse_code.split("   "):
        new_word = ""
        for letter in word.split():
            new_word += MORSE_CODE[letter]
        result.append(new_word)
    return " ".join(result).strip()


if __name__ == "__main__":
    print(time_units(easy))
    print(time_units(hard))
    print(decode_morse(decode_bits(easy)))
    # print(decode_morse(decode_bits(hard)))
