import typer
from cli.goal_cli import goal_app as goal_app
from cli.entry_cli import entry_app as entry_app
from cli.user_cli import user_app as user_app
from cli.analytics_cli import analytics_app 
from database.setup import Base, engine
from cli.meal_cli import meal_app

app = typer.Typer()

app.add_typer(goal_app, name="goal")
app.add_typer(entry_app, name="entry")
app.add_typer(user_app, name="user")
app.add_typer(analytics_app, name="analytics")
app.add_typer(meal_app, name="plan-meal")  

@app.command()
def init_db():
    """Create database tables."""
    # Ensure all models are imported so SQLAlchemy can create all tables
    import models.user, models.entry, models.goal, models.meal_plan
    from models.base import Base
    Base.metadata.create_all(bind=engine)
    typer.echo("✅ Database initialized.")

if __name__ == "__main__":  
    app()