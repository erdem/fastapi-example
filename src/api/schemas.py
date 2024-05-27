from typing import List, Optional, Union

from pydantic import BaseModel


class PDFCheckerRequest(BaseModel):
    file_name: str
    company_name: str


class FieldComparisonItem(BaseModel):
    field: str
    db_value: Optional[Union[str, int, float]]
    extracted_value: Optional[Union[str, int, float]]
    match: bool
    is_missing_in_db: bool
    is_missing_in_extracted: bool


class MissingInDBItem(BaseModel):
    field: str
    extracted_value: Optional[Union[str, int, float]]


class MissingInExtractedItem(BaseModel):
    field: str
    db_value: Optional[Union[str, int, float]]


class PDFCheckerResponse(BaseModel):
    missing_in_db: List[MissingInDBItem]
    missing_in_extracted: List[MissingInExtractedItem]
    fields: List[FieldComparisonItem]


class ErrorResponse(BaseModel):
    type: str
    title: str
    detail: str
