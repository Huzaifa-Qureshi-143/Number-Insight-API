class Number:
    def __init__(self, number: int):
        self.number = number
    
    #for even odd
    def is_even(self):
        if self.number%2 == 0:
            return True
        else:
            return False

    #for total digit count  
    def digit_count(self):
        count = 0
        while self.number != 0:
            self.number //= 10
            count += 1
        return count   