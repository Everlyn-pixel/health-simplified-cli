import typer
from services.entry_service import add_entry as svc_add_entry
from models.entry import Entry
from sqlalchemy.orm import Session
from database.setup import get_db

entry_app = typer.Typer()

@entry_app.command("add")
def add_entry(
    user: str = typer.Argument(..., help="Name of the user."),
    food: str = typer.Argument(..., help="Food item consumed."),
    calories: int = typer.Argument(..., help="Calories for the food item."),
    date: str = typer.Argument(..., help="Date of entry in YYYY-MM-DD format.")
):
    """Add a food entry for a user."""
    if not user.strip():
        typer.echo("❌ User name cannot be empty.")
        raise typer.Exit(code=1)
    if not food.strip():
        typer.echo("❌ Food cannot be empty.")
        raise typer.Exit(code=1)
    if calories < 0:
        typer.echo("❌ Calories must be a positive integer.")
        raise typer.Exit(code=1)
    try:
        from datetime import datetime
        datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        typer.echo("❌ Date must be in YYYY-MM-DD format.")
        raise typer.Exit(code=1)
    svc_add_entry(user, food, calories, date)
    typer.echo(f"🍎 Entry added for {user}: {food}, {calories} kcal on {date}")

@entry_app.command("list")
def list_entries(user_id: int = typer.Argument(..., help="User ID to list entries for.")):
    """List all entries for a user by user ID."""
    db: Session = next(get_db())
    entries = db.query(Entry).filter(Entry.user_id == user_id).all()
    if not entries:
        typer.echo("❌ No entries found for this user.")
        return
    for e in entries:
        typer.echo(f"📘 {e.date} - {getattr(e, 'food', getattr(e, 'data', ''))} ({getattr(e, 'calories', '')} kcal)")