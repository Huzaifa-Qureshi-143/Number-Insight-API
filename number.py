from math import sqrt

class Number:
    def __init__(self, number: int):
        self.number = number
        self.__sum_of_digits: int = 0
        self.__total_digits: int = 0

        self.__digits_logic()
    
    def __digits_logic(self):
        """Calculates total digits and their sum"""
        temp_num = abs(self.number)

        while temp_num != 0:
            #extract last digit and add to total
            self.__sum_of_digits += temp_num % 10
            #remove last digit
            temp_num //= 10
            self.__total_digits += 1

    def is_even(self)->bool:
        """Checks if number is even or not"""

        if self.number%2 == 0:
            return True
        else:
            return False

    def digit_count(self)->int:
        """Returns number of digits in number: ignoring negative sign"""

        return self.__total_digits
    
    def sum_of_digits(self)->int:
        """Returns sum of digits of number: ignoring negative sign"""

        return self.__sum_of_digits
    
    def is_prime(self)->bool:
        """Checks if number is prime number or not"""
        #PRIME NUMBER:
        #numbers > 1 and divisible by 1 and itself only

        if self.number <= 1:
            return False
        elif self.number == 2:
            return True
        elif self.number % 2 == 0:
            return False
        else:
            for i in range(3, sqrt(self.number)+1, 2):
                if self.number % i:
                    return False
            return True

    def binary_representation(self)->str:
        """Returns binary version of number"""

        bin_str = bin(abs(self.number))
        #omit 0b prefix
        if self.number < 0:
            return '-' + bin_str[2:]
        else:
            return bin_str[2:]
        
    