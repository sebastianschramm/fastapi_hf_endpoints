from typing import Any

import fastapi
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer


class ML(BaseModel):
    model: Any
    tokenizer: Any


def load_model(app: fastapi.FastAPI, model_dir: str) -> fastapi.FastAPI:
    ml = ML(
        model=AutoModelForCausalLM.from_pretrained(model_dir),
        tokenizer=AutoTokenizer.from_pretrained(model_dir),
    )
    app.ml = ml
    return app
