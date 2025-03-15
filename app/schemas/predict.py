from typing import Any, List, Optional

from pydantic import BaseModel


class PredictionResults(BaseModel):
    # errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]

class DataInputSchema(BaseModel):
    # PassengerId: Optional[int]
    # Pclass: Optional[int]
    # Name: Optional[str]
    # Sex: Optional[str]
    # Age: Optional[float]
    # SibSp: Optional[int]
    # Parch: Optional[int]
    # Ticket: Optional[str]
    # Cabin: Optional[str]
    # Embarked: Optional[str]
    # Fare: Optional[int]
    dteday: Optional[Any]
    season: Optional[str]
    hr: Optional[str]
    holiday: Optional[str]
    weekday: Optional[str]
    workingday: Optional[str]
    weathersit: Optional[str]
    temp: Optional[float]
    atemp: Optional[float]
    hum: Optional[float]
    windspeed: Optional[float]
    casual: Optional[int]
    registered: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

