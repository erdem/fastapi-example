from typing import Union

from fastapi import Depends

from src.api.repositories import CompanyRepository
from src.main import get_pdf_service_client
from src.pdf_service import PdfService


class PdfExtractorService:

    def __init__(self, client=Depends(get_pdf_service_client)):
        self.client: PdfService = client

    def extract_file_data(self, filename: str) -> Union[dict, None]:
        try:
            return self.client.extract(filename)
        except FileNotFoundError:
            return None


class CompanyService:
    def __init__(self, company_repo=Depends(CompanyRepository)):
        self.company_repo: CompanyRepository = company_repo

    def get_company_by_name(self, name: str):
        return self.company_repo.get_company_or_none(name)
