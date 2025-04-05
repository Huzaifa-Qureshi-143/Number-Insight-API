from fastapi import FastAPI, Path
from typing import Annotated
from number import Number


app = FastAPI()

@app.get('/get-insights/{number}')
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
    number = Number()
    