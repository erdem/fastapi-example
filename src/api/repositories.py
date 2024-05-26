from typing import List, Optional, Union

from fastapi import Depends

from src.main import get_database_csv


class CompanyRepository:
    def __init__(self, csv_data=Depends(get_database_csv)):
        self.csv_data: List[dict] = csv_data

    def get_company_or_none(self, name: str) -> Union[dict, None]:
        db_data = [record for record in self.csv_data if record["Company Name"] == name]
        if not db_data:
            return None
        return db_data[0]

    def get_all_companies_data(self):
        return self.csv_data
