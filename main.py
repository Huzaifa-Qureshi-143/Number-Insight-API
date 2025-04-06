from fastapi import FastAPI, Path
from typing import Annotated
from number import Number
from schema import NumberInsightResponse

app = FastAPI()

@app.get('/get-insights/{number}', response_model=NumberInsightResponse)
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
    ]
):
    num = Number(number)

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