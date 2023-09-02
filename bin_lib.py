BinAlike = "Bin | int | list"

class Bin():
    def __init__(self, definition: BinAlike, length: int = -1):
        if not isinstance(length, int):
            raise TypeError(f"Invalid type in 'length'. Expected int, got {type(length).__name__} instead.")
        self.length = length

        if isinstance(definition, Bin): 
            self.value = definition.value
        elif isinstance(definition, int):
            self.value = definition
        elif isinstance(definition, list):
            definition.reverse()
            self.value = sum(int(bool(number)) * 2**index for index, number in enumerate(definition))
        else:
            raise TypeError(f"Invalid type in 'definition'. Expected Bin, int or list, got {type(definition).__name__} instead.")

        if self.value > 2 ** length - 1 and length >= 0:
            raise OverflowError(f"Value is too big. Maximum value: {bin(2 ** length - 1)}, got {bin(self.value)} instead.")

    def get_bit(self, a: "int", b: "int" = -1):
        if not isinstance(a, int) and not isinstance(b, int):
            raise TypeError(f"Invalid type in 'pos'. Expected int(s).")
        if a < 0:
            raise ValueError(f"invalid value of 'pos'. Expected unsigned integer, got negative integer instead.")
        if a >= self.length > 0 or b >= self.length > 0:
            raise OverflowError(f"Position is too big. Maximum value: {self.length - 1}.")

        if a > b and b > -1:
            a, b = b, a
        
        if b < 0:
            return (self.value >> a) & 1
        else: #Returns bits from a to b
            return [(self.value >> i) & 1 for i in range(b, a - 1, -1)]

    def __add__(self, other: BinAlike):
        if not isinstance(other, Bin):
            other = Bin(other)
        length = -1
        
        #The length of the sum is the biggest of the lengths of the summands
        if min(self.length, other.length) > 0:
            length = max(self.length, other.length)

        return Bin(self.value + other.value, length)

    def __repr__(self):
        return bin(self.value)[2:].rjust(self.length, '0')

    def __str__(self):
        return self.__repr__()

    def __int__(self):
        return int(self.value)
    
    def __eq__(self, other: BinAlike):
        if isinstance(other, list):
            other = Bin(other)
        return self.value == other
    
    def __neq__(self, other: BinAlike):
        return not self.__eq__(other)
    
    def __lt__(self, other: BinAlike):
        if isinstance(other, list):
            other = Bin(other)
        return self.value < other
    
    def __le__(self, other: BinAlike):
        return self.__lt__(other) or self.__eq__(other) 

    def __gt__(self, other: BinAlike):
        return not self.__le__(other)

    def __ge__(self, other: BinAlike):
        return not self.__lt__(other)