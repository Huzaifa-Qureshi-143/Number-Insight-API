from fastapi import FastAPI, Path, Query
from typing import Annotated
from number import Number
from schema import NumberInsightResponse
from insight_enum import SpecificInsight

app = FastAPI()

@app.get('/get-insights/{number}/', response_model=NumberInsightResponse | dict)
def insights(
    number: Annotated[
        int,
        Path(
            title='Number',
            ge=-9999,
            le=9999,
            description='The number to calculate insights for',
            example=45
        )
    ],
    specific: SpecificInsight | None = None
):
    num = Number(number)

    if specific: #query applied
        if specific == SpecificInsight.is_even:
            return {"is_even": num.is_even()}
        elif specific == SpecificInsight.is_prime:
            return {"is_prime": num.is_prime()}
        elif specific == SpecificInsight.digit_count:
            return {"digit_count": num.digit_count()}
        elif specific == SpecificInsight.sum_of_digits:
            return {"sum_of_digits": num.sum_of_digits()}
        elif specific == SpecificInsight.bin_rep:
            return {"binary_representation": num.binary_representation()}
        elif specific == SpecificInsight.is_palindrome:
            return {"is_palindrome": num.is_palindrome()}
        elif specific == SpecificInsight.is_armstrong:
            return {"is_armstrong": num.is_armstrong()}
        
    return NumberInsightResponse(
        number= num.number,
        is_even= num.is_even(),
        is_prime= num.is_prime(),
        digit_count= num.digit_count(),
        sum_of_digits= num.sum_of_digits(),
        binary_representation= num.binary_representation(),
        is_palindrome= num.is_palindrome(),
        is_armstrong= num.is_armstrong()
    )