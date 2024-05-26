from typing import List, Dict, Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from src.api import schemas
from src.api.services import PdfExtractorService, CompanyService
from src.config import settings
from src.utils.pdf_data_comparer import compare_data
from src.api.repositories import CompanyRepository


router = APIRouter(prefix="/api")


@router.post(
    "/pdf-checker",
    response_model=schemas.PDFCheckerResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        422: {"model": schemas.ErrorResponse, "description": "Invalid request body."},
    },
)
def upload_file(
    payload: schemas.PDFCheckerRequest,
    company_service: CompanyService = Depends(CompanyService),
    pdf_service: PdfExtractorService = Depends(PdfExtractorService),
):
    pdf_file_path = f"{settings.ASSETS_DIR}/{payload.file_name}"
    extracted_data = pdf_service.extract_file_data(pdf_file_path)
    if extracted_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found in PDFService"
        )
    db_data = company_service.get_company_by_name(payload.company_name)
    if db_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Company not found in database"
        )
    comparison_summary = compare_data(db_data, extracted_data)
    return comparison_summary
