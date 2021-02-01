from pydantic import BaseModel
class Iris(BaseModel):
    petallength: float
    sepallength: float
    sepalwidth: float
    petalwidth: float