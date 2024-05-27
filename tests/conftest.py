from os import path

import pandas as pd
import pytest
from dotenv import find_dotenv, load_dotenv
from fastapi.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def load_env():
    # override env variables with

    env_file = find_dotenv(".env.tests")
    load_dotenv(env_file)


def get_test_csv_data():
    from src.config import settings

    df = pd.read_csv(path.join(settings.BASE_DIR, "tests/fixtures/test_database.csv"))
    return df.to_dict(orient="records")


@pytest.fixture
def test_csv_data():
    return get_test_csv_data()


def get_test_pdf_service_client():
    from src.config import settings
    from src.pdf_service import PdfService

    class TestPdfService(PdfService):
        def extract(self, file_path: str):
            if file_path == "assets/healthinc.pdf":
                return {
                    "Company Name": "HealthInc",
                    "Industry": "Healthcare",
                    "Market Capitalization": 3000,
                    "Revenue (in millions)": 1000,
                    "EBITDA (in millions)": 250,
                    "Net Income (in millions)": 80,
                    "Debt (in millions)": 150,
                    "Equity (in millions)": 666,
                    "Enterprise Value (in millions)": 3150,
                    "P/E Ratio": 15,
                    "Revenue Growth Rate (%)": 12,
                    "EBITDA Margin (%)": 40,
                    "Net Income Margin (%)": 8,
                    "ROE (Return on Equity) (%)": 13.33,
                    "ROA (Return on Assets) (%)": 10,
                    "Debt to Equity Ratio": 0.25,
                    "Location": "New York, NY",
                    "CEO": "Jane Smith",
                    "Number of Employees": 3000,
                }
            raise FileNotFoundError("Cannot extract data. Invalid file provided.")

    return TestPdfService(settings.PDF_SERVICE_API_KEY)


@pytest.fixture
def test_app():
    from src.main import create_app, get_database_csv, get_pdf_service_client

    app = create_app()
    app.dependency_overrides[get_database_csv] = get_test_csv_data
    app.dependency_overrides[get_pdf_service_client] = get_test_pdf_service_client
    return app


@pytest.fixture
def client(test_app):
    client = TestClient(test_app)
    return client
