import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from bike_sharing_model import __version__ as model_version
from bike_sharing_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()



example_input = {
    "inputs": [
        {
    'dteday': '2011-07-13',
    'season': 'fall',
    'hr': '4am',
    'holiday': 'No',
    'weekday': 'Wed',
    'workingday': 'Yes',
    'weathersit': 'Clear',
    'temp': 26.78,
    'atemp': 28.9988,
    'hum': 58.0,
    'windspeed': 16.9979,
    'casual': 0,
    'registered': 5,
    'cnt': 0,
        }
    ]
}


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleDataInputs = Body(..., example=example_input)) -> Any:
    """
    Survival predictions with the bikeshare_model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    # if results["errors"] is not None:
    #     raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    return results

