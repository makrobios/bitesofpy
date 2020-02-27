THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def check_int(self, integer):

        if integer < 0:
            sign= THUMBS_DOWN
        elif integer == 0:
            raise ValueError("Specify a number")
        else:
            sign = THUMBS_UP

        return sign, abs(integer)
    
    def __mul__(self, integer):

        sign, integer = self.check_int(integer) 
        if integer > 3:
           return f"{sign} ({integer}x)" 
        else:
            return sign * integer

    def __rmul__(self, integer):

        sign, integer = self.check_int(integer) 

        if abs(integer) > 3:
           return f"{sign} ({integer}x)" 
        else:
            return sign * integer

