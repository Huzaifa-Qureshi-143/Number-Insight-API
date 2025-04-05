from pydantic import BaseModel

class NumberInsightResponse(BaseModel):
    number: int
    
    is_even: bool
    is_prime: bool
    digit_count: int
    sum_of_digits: int
    is_perfect: bool
    binary_representation: str
    is_palindrome: bool
    is_armstrong: bool