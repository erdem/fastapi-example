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

# Data discrepancy checker

This task mirrors a system we recently built internally, and will give you an
idea of the problems we need to solve.

Every quarter, new company data is provided to us in PDF format. We need to use
an external service to extract this data from the PDF, and then validate it
against data we have on file from another source.

Complete the API so that:

A user can provide a PDF and a company name data is extracted from the PDF via
the external service and compared to the data stored on file a summary of the
data is returned, containing all fields from both sources, noting which fields
did not match.

A selection of example PDFs have been uploaded, and the PDF
extraction service has been mocked for use in `src/pdf_service.py` - DO NOT
EDIT THIS FILE. There is simple documentation of the service in
`PDF_SERVICE_DOCS.md`. You can treat this as just another microservice.

The existing data we have on file is available in the `data/database.csv` file.

Treat this code as if it will be deployed to production, following best
practices where possible.

## Setup using Poetry

The easiest way to set up the repository is to use `python-poetry`. The lock file
was generated using version `1.8.3`

1. Ensure `poetry` is installed
2. Run `make install`

## Setup without Poetry

Alternatively it's possible to `pip install` directly using the
`pyproject.toml` or `requirements.txt`.
