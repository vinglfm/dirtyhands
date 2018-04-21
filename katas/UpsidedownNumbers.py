class UpsideDownNumbers():
    def __init__(self):
        self.allowed_digits = set('01689')
        self.map_digits = {'6': '9', '9': '6'}

    def count(self, from_number, to_number):
        accepted = 0
        for number in range(from_number, to_number):
            if self.is_upside_down(number):
                accepted += 1
        return accepted

    def is_upside_down(self, number):
        number_str = str(number)
        for idx, digit in enumerate(number_str):
            if digit not in self.allowed_digits or self.map_digits.get(digit, digit) != number_str[-idx-1]:
                return False
        return True
