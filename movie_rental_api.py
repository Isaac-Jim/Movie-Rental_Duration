from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class RentalFeatures(BaseModel):
    amount:float
    release_year:float
    rental_rate :float
    length : float
    replacement_cost :float    
    NC_17: int
    PG            : int
    PG_13      :int
    R: int
    amount_2:float
    length_2 : float
    rental_rate_2 :  float
    deleted_scenes :    int
    behind_the_scenes :int

@app.post("/predict")

def make_predictions(data:RentalFeatures):
    features = [[data.amount,
                 data.release_year,
                 data.rental_rate,
                 data.length,
                 data.replacement_cost,
                 data.NC_17,
                 data.PG,
                 data.PG_13,
                 data.R,
                 data.amount_2,
                 data.length_2,
                 data.rental_rate_2,
                 data.deleted_scenes,
                 data.behind_the_scenes ]]
    model_movie = joblib.load('dvd_model.pkl')

    y_pred = model_movie.predict(features)[0]

    return {"prediction":f"{y_pred}"}