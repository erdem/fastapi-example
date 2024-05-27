import pytest


class TestPDFCheckerEndpoint:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.endpoint = "/api/pdf-checker"

    def test_response_success(self, client):
        payload = {"file_name": "healthinc.pdf", "company_name": "HealthInc"}
        response = client.post(self.endpoint, json=payload)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["fields"]
        assert response_data["missing_in_db"]
        assert response_data["missing_in_extracted"]

    def test_company_not_found(self, client):
        payload = {"file_name": "healthinc.pdf", "company_name": "ManuCorp"}
        response = client.post(self.endpoint, json=payload)

        assert response.status_code == 404
        response_data = response.json()
        assert response_data["detail"] == "Company not found in database"

    def test_service_not_found(self, client):
        payload = {"file_name": "retailco.pdf", "company_name": "HealthInc"}
        response = client.post(self.endpoint, json=payload)

        assert response.status_code == 404
        response_data = response.json()
        assert response_data["detail"] == "File not found in PDFService"
