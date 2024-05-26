import logging
from typing import Callable, List, Dict

import pandas as pd
from fastapi import FastAPI

from .config import settings
from .pdf_service import PdfService


logging.basicConfig(level=settings.LOGGING_LEVEL)
logger = logging.getLogger(__name__)

_app_init_hooks: list[Callable[[FastAPI], None]] = []
app_init_hook = _app_init_hooks.append


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
    for f in _app_init_hooks:
        f(app)
    return app


app = create_app()


@app_init_hook
def _validate_pdf_service_credentials(app: FastAPI) -> None:
    try:
        PdfService(settings.PDF_SERVICE_API_KEY)
    except AssertionError as e:
        raise RuntimeError("Invalid PDF service credentials") from e


def get_pdf_service() -> PdfService:
    return PdfService(settings.PDF_SERVICE_API_KEY)


def get_database_csv() -> List[Dict[str, str]]:
    df = pd.read_csv("data/database.csv")
    data = df.to_dict(orient="records")
    return data
