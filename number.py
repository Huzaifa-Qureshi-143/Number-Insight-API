from math import isqrt

class Number:
    def __init__(self, number: int):
        """Constructor"""
        self.number = number
        self.__absolute_number = abs(self.number)

        self.__sum_of_digits: int = 0
        self.__total_digits: int = 0

        self.__digits_logic()
    
    def __digits_logic(self):
        """Calculates total digits and their sum"""
        temp_num = self.__absolute_number

        if temp_num == 0:
            self.__total_digits = 1
            return
        
        while temp_num != 0:
            #extract last digit and add to total
            self.__sum_of_digits += temp_num % 10
            #remove last digit
            temp_num //= 10
            self.__total_digits += 1

    def is_even(self)->bool:
        """Checks if number is even or not"""
        return self.number % 2 == 0

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
            for i in range(3, isqrt(self.number)+1, 2):
                if self.number % i == 0:
                    return False
            return True

    def binary_representation(self)->str:
        """Returns binary version of number"""

        if self.number == 0:
            return '0'
        
        bin_str = bin(self.__absolute_number)
        #omit 0b prefix
        if self.number < 0:
            return '-' + bin_str[2:]
        else:
            return bin_str[2:]
        
    def is_palindrome(self)->bool:
        """Checks if number is palindrome or not: ignores negative sign"""

        #ignore negative sign
        num = self.__absolute_number

        reversed_num = 0
        original_num = num

        while num != 0:
            #extract last digit and add to reversed number
            reversed_num = (reversed_num * 10) + (num % 10)
            #remove last digit
            num //= 10

        #check if original number is equal to its reversed version
        return original_num == reversed_num
    
    def is_armstrong(self)->bool:
        """Checks if number is Armstrong or not: ignores negative sign"""

        #ARMSTRONG NUMBER:
        # 153: (1**3) + (5**3) + (3**3) == 153 (True)
        
        temp_num = self.__absolute_number
        armstrong_sum = 0

        while temp_num != 0:
            armstrong_sum += (temp_num%10)**(self.__total_digits)
            temp_num //= 10
        
        return armstrong_sum == self.__absolute_number