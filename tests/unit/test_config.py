def test_settings():
    from src.config import settings

    assert settings.ENV == "testing"
    assert not settings.is_production
