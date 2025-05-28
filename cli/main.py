import typer
from cli.goal_cli import goal_app as goal_app
from cli.entry_cli import entry_app as entry_app
from cli.user_cli import user_app as user_app
from cli.analytics_cli import analytics_app 
from database.setup import Base, engine

app = typer.Typer()

app.add_typer(goal_app, name="goal")
app.add_typer(entry_app, name="entry")
app.add_typer(user_app, name="user")
app.add_typer(analytics_app, name="analytics")  

@app.command()
def init_db():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)
    typer.echo("✅ Database initialized.")

if __name__ == "_main_":  
    app()