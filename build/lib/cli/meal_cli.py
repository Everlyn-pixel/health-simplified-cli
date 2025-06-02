import typer

meal_app = typer.Typer()

@meal_app.command("plan-meal")
def plan_meal(user: str, week: int):
    """Generate meal plan for a user for a given week."""
    typer.echo(f"📅 Planning meals for user: {user} in week {week}")

@meal_app.command("update")
def update_meal(id: int):
    """Update an existing meal plan by ID."""
    typer.echo(f"✏️ Updating meal plan with ID: {id}")
