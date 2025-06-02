import typer
import matplotlib.pyplot as plt
import csv
from models.entry import Entry
from database.setup import SessionLocal

analytics_app = typer.Typer()

@analytics_app.command()
def summary(user_id: int = typer.Argument(..., help="User ID to summarize entries for.")):
    """Generate a summary report for a user's entries."""
    session = SessionLocal()
    entries = session.query(Entry).filter(Entry.user_id == user_id).all()
    total_entries = len(entries)
    typer.echo(f"📊 User {user_id} has {total_entries} entries recorded.")
    session.close()

@analytics_app.command()
def export_csv(
    user_id: int = typer.Argument(..., help="User ID to export entries for."),
    output: str = typer.Option("entries.csv", help="Output CSV file name.")
):
    """Export user's entries to CSV."""
    session = SessionLocal()
    entries = session.query(Entry).filter(Entry.user_id == user_id).all()
    with open(output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Date", "Food", "Calories", "User ID"])
        for entry in entries:
            writer.writerow([
                entry.id,
                entry.date,
                getattr(entry, 'food', ''),
                getattr(entry, 'calories', ''),
                entry.user_id
            ])
    typer.echo(f"✅ Exported to {output}")
    session.close()

@analytics_app.command()
def show_chart(user_id: int = typer.Argument(..., help="User ID to show entry chart for.")):
    """Display a chart of user's entry data count over time."""
    session = SessionLocal()
    entries = session.query(Entry).filter(Entry.user_id == user_id).all()
    if not entries:
        typer.echo("No data available.")
        return
    dates = [entry.date.strftime("%Y-%m-%d") for entry in entries]
    date_counts = {}
    for d in dates:
        date_counts[d] = date_counts.get(d, 0) + 1
    x = list(date_counts.keys())
    y = list(date_counts.values())
    plt.bar(x, y)
    plt.xlabel("Date")
    plt.ylabel("Entries")
    plt.title(f"Entries for User {user_id}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    session.close()