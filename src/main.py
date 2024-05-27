import logging
from os import path
from typing import Callable

import pandas as pd
from fastapi import FastAPI

from src.config import settings
from src.pdf_service import PdfService

logging.basicConfig(
    level=settings.LOGGING_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

_app_init_hooks: list[Callable[[FastAPI], None]] = []
app_init_hook = _app_init_hooks.append


def create_app() -> FastAPI:
    from src.api.routes import router as api_router

    app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
    app.include_router(api_router)
    for f in _app_init_hooks:
        f(app)
    return app


@app_init_hook
def _validate_pdf_service_credentials(app: FastAPI) -> None:
    try:
        PdfService(settings.PDF_SERVICE_API_KEY)
        logger.info("Successfully established connection with PDF Service.")
    except AssertionError as e:
        raise RuntimeError("Invalid PDF service credentials") from e


def get_pdf_service_client() -> PdfService:
    return PdfService(settings.PDF_SERVICE_API_KEY)


def get_database_csv() -> list[dict]:
    df = pd.read_csv(path.join(settings.BASE_DIR, "data/database.csv"))
    return df.to_dict(orient="records")


app = create_app()
