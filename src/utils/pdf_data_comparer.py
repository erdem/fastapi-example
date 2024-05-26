from collections import defaultdict


def compare_data(db_data: dict, extracted_data: dict) -> dict:
    """
    Compares two dictionaries (db_data and extracted_data) and returns a summary of the comparison.

    :param db_data: Dictionary containing data from the database.
    :param extracted_data: Dictionary containing data extracted from the PDF.
    :return: A dictionary summarizing the comparison between the db data and the extracted data.
    """
    summary = defaultdict(list)

    # Find all keys from both dictionaries
    all_keys = db_data.keys() | extracted_data.keys()

    for key in all_keys:
        db_value = db_data.get(key)
        extracted_value = extracted_data.get(key)
        is_missing_in_db = False
        is_missing_in_extracted = False

        if key not in db_data:
            is_missing_in_db = True
            summary["missing_in_db"].append({"field": key, "extracted_value": extracted_value})

        if key not in extracted_data:
            is_missing_in_extracted = True
            summary["missing_in_extracted"].append({"field": key, "db_value": db_value})

        field_summary = {
            "field": key,
            "db_value": db_value,
            "extracted_value": extracted_value,
            "match": db_value == extracted_value,
            "is_missing_in_db": is_missing_in_db,
            "is_missing_in_extracted": is_missing_in_extracted,
        }
        summary["fields"].append(field_summary)

    return summary
