# Setup
 
1. Clone the repository and navigate to the root folder in your terminal.
```bash
git clone git@github.com:erdem/python-coding-test.git
```

2. Create a .env file (git ignored) by copying the [.env.example](.env.example) file.

3. Install the project dependencies with poetry via call `make install` command.

```shell
make install
```

4. The project uses pre-commit to enforce code formatting and run linters before every commit. The pre-commit hooks configuration is stored in the .pre-commit-config.yaml file. Install the hooks before making any commit.

```bash
pre-commit install
```

5. Run FastAPI dev server to explore the API

```
make dev
```


# Usage

```shell
curl --request POST \
  --url http://localhost:8000/api/pdf-checker \
  --header 'Content-Type: application/json' \
  --data '{
      "file_name": "retailco.pdf",
      "company_name": "RetailCo"
    }
'
```

# FastAPI PDF Data Checker

This project demonstrates a FastAPI application that compares company data extracted from PDFs against existing records. It's designed to simulate a common business task: verifying information from multiple sources.

## What it does

1. Extracts data from PDFs using a mocked external service
2. Compares the extracted data with records stored in a CSV file
3. Returns a summary of all fields, noting any discrepancies

## Key components

- FastAPI for the API framework
- A mocked PDF extraction service (`src/pdf_service.py`)
- CSV file for storing existing company data (`data/database.csv`)
- Data comparison and reporting logic

## Technical aspects

- Integration with an external service (simulated)
- Data processing and comparison
- Error handling and input validation

This project serves as an example of using FastAPI to process data and generate comparison reports. It's structured following good coding practices.

