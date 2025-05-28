import typer

goal_app = typer.Typer()

@goal_app.command()
def create_goal(name: str):
    typer.echo(f"🎯 Goal '{name}' created!")