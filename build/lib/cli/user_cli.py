import typer

user_app = typer.Typer()

@user_app.command()
def create_user(name: str):
    typer.echo(f"👤 User '{name}' created!")