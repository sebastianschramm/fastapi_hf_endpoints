from pydantic import BaseModel


class PredictionInput(BaseModel):
    text: str


class Prediction(BaseModel):
    response: str
