# Health Simplified CLI

A command-line tool to help users track daily food intake, set nutrition goals, and plan weekly meals. Built with Python, SQLAlchemy, and Typer.

## Features
- User management (create, list)
- Food entry tracking (add, list)
- Nutrition goals (set, list)
- Weekly meal planning (create, update, list)
- Analytics and reporting (summary, export to CSV, chart)

## Installation

1. Clone the repository:
   ```powershell
   git clone <your-repo-url>
   cd health-simplified-cli
   ```
2. Install dependencies:
   ```powershell
   pip install .
   ```

## Usage

Initialize the database (run once):
```powershell
python -m cli.main init-db
```

### User Management
- Create a user:
  ```powershell
  python -m cli.main user create-user Alice alice@example.com
  ```
- List users:
  ```powershell
  python -m cli.main user list
  ```

### Food Entries
- Add a food entry:
  ```powershell
  python -m cli.main entry add Alice Banana 100 2025-06-01
  ```
- List entries for a user (by user ID):
  ```powershell
  python -m cli.main entry list 1
  ```

### Goals
- Set daily and weekly goals:
  ```powershell
  python -m cli.main goal set Alice 2000 14000
  ```
- List goals for a user:
  ```powershell
  python -m cli.main goal list Alice
  ```

### Meal Planning
- Create a meal plan:
  ```powershell
  python -m cli.main plan-meal plan-meal Alice 23 --description "Low-carb week"
  ```
- Update a meal plan:
  ```powershell
  python -m cli.main plan-meal update 1 --description "High-protein week"
  ```
- List all meal plans:
  ```powershell
  python -m cli.main plan-meal list
  ```
- List meal plans for a user:
  ```powershell
  python -m cli.main plan-meal list --user Alice
  ```

### Analytics & Reporting
- Show summary for a user (by user ID):
  ```powershell
  python -m cli.main analytics summary 1
  ```
- Export entries to CSV:
  ```powershell
  python -m cli.main analytics export-csv 1 --output alice_entries.csv
  ```
- Show entry chart:
  ```powershell
  python -m cli.main analytics show-chart 1
  ```

## Testing
Run all tests:
```powershell
python -m pytest
```

## Contributing
- Fork the repo and create a feature branch.
- Submit a pull request with your changes.

## License
MIT