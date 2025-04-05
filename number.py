class Number:
    def __init__(self, number: int):
        self.number = number
        self.__sum_of_digits: int = 0
        self.__total_digits: int = 0

        self.__digits_logic()
    
    def __digits_logic(self):
        temp_num = abs(self.number)

        while temp_num != 0:
            #extract last digit and add to total
            self.__sum_of_digits += temp_num % 10
            #remove last digit
            temp_num //= 10
            self.__total_digits += 1

    def is_even(self):
        """Checks if number is even or not"""
        if self.number%2 == 0:
            return True
        else:
            return False

    def digit_count(self):
        """Returns number of digits in number: ignoring negative sign"""
        return self.__total_digits
    
    def sum_of_digits(self):
        """Returns sum of digits of number: ignoring negative sign"""
        return self.__sum_of_digits