from fastapi import FastAPI
from beerlog.core import get_beers_from_database


api = FastAPI(title="Beerlog")


@api.get("/beers/")
def list_beers():
    beers = get_beers_from_database()
    return beers
