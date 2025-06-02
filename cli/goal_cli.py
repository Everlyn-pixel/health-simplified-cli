import typer
from services.goal_service import set_goal, list_goals

goal_app = typer.Typer()

@goal_app.command()
def create_goal(name: str):
    typer.echo(f"🎯 Goal '{name}' created!")

@goal_app.command()
def set(
    user: str = typer.Argument(..., help="Name of the user."),
    daily: int = typer.Argument(..., help="Daily calorie goal."),
    weekly: int = typer.Argument(..., help="Weekly calorie goal.")
):
    """Set daily and weekly calorie goals for a user."""
    if daily < 0 or weekly < 0:
        typer.echo("❌ Goals must be positive integers.")
        raise typer.Exit(code=1)
    set_goal(user, daily, weekly)
    typer.echo(f"🎯 Set goals for {user}: daily={daily}, weekly={weekly}")

@goal_app.command()
def list(user: str = typer.Argument(..., help="Name of the user to list goals for.")):
    """List all goals for a user."""
    list_goals(user)