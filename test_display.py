import pytest
import unittest
from unittest.mock import patch
from wizard import Wizard  



from display import (
    display_summary,
    show_phase,
    print_items,
    get_reset,
    rest_data,
    show_wizards_history,
)

@pytest.fixture
def example_details():
    return {
        "Name": "ahat saa",
        "Email": "ahat.saa@gmail.com",
        "Birth Date": "05/12/1996",
        "City": "Ramleh",
        "Street": "Street St.",
        "Number": "123",
        "Social Media": "https://www.facebook.com/ahats",
        "Hobbies": "Chess",
        "Happy": "Yes",
        "Skydiving": "No",
        "One Dollar": "Yes",
    }

def test_display_summary(example_details,capsys):
    with patch("builtins.input", return_value="1"):
        display_summary(example_details)
        captured = capsys.readouterr()

    assert captured 

def test_show_phase(example_details, capsys):
    show_phase(1, example_details)
    captured = capsys.readouterr()
    assert captured

def test_print_items(example_details, capsys):
    print_items(1, example_details, 0, 3)
    captured = capsys.readouterr()
    assert captured

def test_get_reset():
    assert get_reset() is False

def test_rest_data():
    details = {"Name": "ahat saa", "Email": "ahat.saa@gmail.com"}
    rest_data(details)
    assert all(value is None for value in details.values())




def setUp(self):
    # Set up a Wizard instance with some sample data for testing
    self.wizard = Wizard()
    self.wizard.users = [
        {"Name": "ahat saa", "Email": "ahat.saa@gmail.com", "Birth Date": "05/12/1996"},
        {"Name": "sam saa", "Email": "sam.saa@gmail.com", "Birth Date": "02/02/1995"},
    ]



# # Simulate user input, "1" to sort by Name
# @patch("builtins.input", side_effect=["1"]) 
# def test_show_wizards_history_sort_by_name(self, mock_input):
#     with patch("builtins.print") as mock_print:
#         show_wizards_history(self.wizard)

# # Simulate user input, "2" to sort by Email
# @patch("builtins.input", side_effect=["2"]) 
# def test_show_wizards_history_sort_by_email(self, mock_input):
#     with patch("builtins.print") as mock_print:
#         show_wizards_history(self.wizard)    
