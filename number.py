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
        return len(str(abs(self.number)))
    
    #for sum of digits
    def sum_of_digits():
        pass