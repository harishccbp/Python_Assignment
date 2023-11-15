class IntegerToRoman:
    def __init__(self):
        self.numeral_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert(self, num):
        if not isinstance(num, int) or not 0 < num < 4000:
            raise ValueError("Input must be an integer between 1 and 3999")

        result = ''
        for value, numeral in self.numeral_map.items():
            while num >= value:
                result += numeral
                num -= value

        return result

# Example usage:
try:
    number = int(input("Enter an integer (1 to 3999): "))
    converter = IntegerToRoman()
    roman_numeral = converter.convert(number)
    print(f"The Roman numeral for {number} is: {roman_numeral}")
except ValueError as e:
    print(f"Error: {e}")
