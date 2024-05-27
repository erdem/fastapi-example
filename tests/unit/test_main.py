from unittest import mock


@mock.patch("src.main.get_database_csv")
def test_get_database_csv(mock_database_csv, test_csv_data):
    from src.main import get_database_csv

    mock_database_csv.return_value = test_csv_data
    csv_data = get_database_csv()
    assert len(csv_data) == 2
