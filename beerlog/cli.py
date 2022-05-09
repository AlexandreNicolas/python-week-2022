from beerlog.core import add_beer_to_database, get_beers_from_database
from typing import Optional
import typer
import warnings
from sqlalchemy.exc import SAWarning
from rich.table import Table
from rich.console import Console
# from sqlmodel.sql.expression import Select, SelectOfScalar
warnings.filterwarnings("ignore", category=SAWarning)
# SelectOfScalar.inherit_cache = True
# Select.inherit_cache = True


main = typer.Typer(help="Beer Management Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer in database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
