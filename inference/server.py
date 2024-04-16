from contextlib import asynccontextmanager

import fastapi
from starlette.requests import Request

from inference import loading
from inference.structs import Prediction, PredictionInput


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    model_dir = "/repository"
    app = loading.load_model(app=app, model_dir=model_dir)
    yield


app = fastapi.FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return "Running"


@app.post("/predict")
def prediction(prediction_input: PredictionInput, request: Request) -> Prediction:
    ml: loading.ML = request.app.ml
    encoded_input = ml.tokenizer(prediction_input.text, return_tensors="pt")
    output_ids = ml.model.generate(**encoded_input, max_new_tokens=20)
    output = ml.tokenizer.batch_decode(output_ids)[0]
    return {"response": output}
