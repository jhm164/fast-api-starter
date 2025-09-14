# Setup Instructions

## 1. Install Poetry

```powershell
Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing | Invoke-Expression
```

## 2. Set Environment Variable

```powershell
$env:Path += ";C:\Users\saura\AppData\Roaming\Python\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
```

## 3. Install Packages

```bash
poetry add fastapi uvicorn[standard]
```

## 4. Run the Application

```bash
poetry run uvicorn main:app --reload
```