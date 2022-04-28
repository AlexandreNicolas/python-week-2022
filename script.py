from sqlmodel import Session, select
from beerlog.models import Beer
from beerlog.database import engine

with Session(engine) as session:
    beer = Beer(name="Two Chefs 2", style="QPA", flavor=5, image=6, cost=6)
    session.add(beer)
    session.commit()

with Session(engine) as session:
    sql = select(Beer)
    results = session.exec(sql)
    for beer in results:
        print(beer.name)
