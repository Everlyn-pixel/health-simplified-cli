import typer
from services.meal_service import add_meal_plan, update_meal_plan, list_meal_plans

meal_app = typer.Typer()

@meal_app.command("plan-meal")
def plan_meal(
    user: str = typer.Argument(..., help="Name of the user."),
    week: int = typer.Argument(..., help="Week number (1-52)."),
    description: str = typer.Option(None, help="Meal plan description.")
):
    """Generate meal plan for a user for a given week."""
    if week < 1 or week > 52:
        typer.echo("❌ Week must be between 1 and 52.")
        raise typer.Exit(code=1)
    add_meal_plan(user, week, description)

@meal_app.command("update")
def update_meal(
    id: int = typer.Argument(..., help="Meal plan ID to update."),
    description: str = typer.Option(None, help="Meal plan description.")
):
    """Update an existing meal plan by ID."""
    update_meal_plan(id, description)

@meal_app.command("list")
def list_meals(user: str = typer.Option(None, help="User name to filter by.")):
    """List all meal plans, or filter by user name."""
    list_meal_plans(user)
