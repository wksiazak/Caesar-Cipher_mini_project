import os

import pytest

from database import DbHandler


@pytest.fixture
def test_db():
    path = "test_db.db"
    db = DbHandler(path)
    # db clear
    yield db


def test_if_table_was_created(test_db):
    test_db.create_table()
    cursor = test_db.con.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Ciphers';"
    )
    table_exists = cursor.fetchone()
    assert table_exists is not None, "Table 'Ciphers' was not created"


def test_add_data_to_table_ciphers(test_db):
    # Define test data
    given_text = "test_text"
    output = "test_output"

    # Add data to the table
    test_db.add_to_ciphers(given_text, output)

    # Retrieve the data from the table
    cursor = test_db.con.cursor()
    cursor.execute("SELECT * FROM Ciphers WHERE given_text=?", (given_text,))
    result = cursor.fetchone()

    # Check if the data was inserted correctly
    assert result is not None, "Data was not inserted into the 'Ciphers' table"
    assert result[0] == given_text, f"Expected '{given_text}' but found '{result[0]}'"
    assert result[1] == output, f"Expected '{output}' but found '{result[1]}'"

    test_db.con.execute("DELETE FROM Ciphers WHERE given_text=?", (given_text,))
    test_db.con.commit()


def test_export_data_to_file(test_db):
    given_text = "test_text"
    output = "test_output"

    # Add data to the table
    test_db.add_to_ciphers(given_text, output)

    # Export the data
    export_file = "exported_data.txt"
    test_db.export_all_ciphers("Ciphers", export_file)

    # Check if the file was created and contains the expected data
    assert os.path.exists(export_file), "Export file was not created"
    with open(export_file, "r") as file:
        exported_data = file.readlines()
        assert len(exported_data) == 1, "Exported data does not match expected"
        assert (
            str((given_text, output)) in exported_data[0]
        ), "Exported data does not match expected"

    # Clean up - remove the export file
    os.remove(export_file)
