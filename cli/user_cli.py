import typer
from services.user_service import create_user as svc_create_user, list_users as svc_list_users

user_app = typer.Typer()

@user_app.command()
def create_user(name: str = typer.Argument(..., help="Name of the user."), email: str = typer.Argument(..., help="Email address of the user.")):
    """Create a new user with the given name and email."""
    if not name.strip():
        typer.echo("❌ Name cannot be empty.")
        raise typer.Exit(code=1)
    if "@" not in email or "." not in email:
        typer.echo("❌ Please provide a valid email address.")
        raise typer.Exit(code=1)
    svc_create_user(name, email)
    typer.echo(f"👤 User '{name}' with email '{email}' created!")

@user_app.command()
def list():
    """List all users in the system."""
    svc_list_users()