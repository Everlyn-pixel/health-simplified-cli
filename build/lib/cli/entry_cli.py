import typer
from sqlalchemy.orm import Session
from database.setup import get_db
from models.entry import Entry

entry_app = typer.Typer()

@entry_app.command("list")
def list_entries(user_id: int):
	"""List all entries for a user."""
	db: Session = next(get_db())
	entries = db.query(Entry).filter(Entry.user_id == user_id).all()
	if not entries:
		typer.echo("❌ No entries found for this user.")
		return
	for e in entries:
		typer.echo(f"📘 {e.date} - {e.data}")