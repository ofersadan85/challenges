numerals = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


class RomanNumerals:
    def to_roman(val):
        result = ""
        while val > 0:
            largest = max(key for key in numerals if val >= key)
            result += numerals[largest]
            val -= largest
        return result

    def from_roman(roman_num):
        inverted = {v: k for k, v in numerals.items()}
        doubles = sorted(
            [v for v in numerals.values() if len(v) == 2],
            key=lambda x: inverted[x],
            reverse=True,
        )
        normals = sorted(
            [v for v in numerals.values() if len(v) == 1],
            key=lambda x: inverted[x],
            reverse=True,
        )
        order = doubles + normals
        val = 0
        for symbol in order:
            val += inverted[symbol] * roman_num.count(symbol)
            roman_num = roman_num.replace(symbol, '')
        return val
