

import pytest
import re

from wizard import Wizard  
from phase import Phase


phase = Phase(4)
functions =phase.validation_functions

# test validation of all inputs i the phses ,
# once with valid input ,another with invalid input

@pytest.mark.parametrize("user_input,func,expected_output", [
    ("ahat aa",functions["Name"], "ahat aa"),
    ("a a",functions["Name"], "Invalid input"),
        ("ahat@gmail.com",functions["Email"], "ahat@gmail.com"),
    ('a a',functions["Email"], "Invalid input"),
        ("01/02/96",functions["Birth Date"], "01/02/96"),
    ('//22/3',functions["Birth Date"], "Invalid input"),
        ("ramleh",functions["City"], "ramleh"),
    ('112',functions["City"], "Invalid input"),
        ("levi",functions["Street"],"levi"),
    ("11",functions["Street"],"Invalid input"),
        ("3",functions["Number"], "3"),
    ('aa',functions["Number"], "Invalid input"),
        ("http://facebook.com/ahat",functions["Social Media"], "http://facebook.com/ahat"),
    ('aa',functions["Social Media"], "Invalid input"),
        ("yes",functions["Happy"], "yes"),
    ('a',functions["Happy"], "Invalid input"),
        ("no",functions["Skydiving"], "no"),
    ('a',functions["Skydiving"], "Invalid input"),
        ("no",functions["One Dollar"], "no"),
    ('a',functions["One Dollar"], "Invalid input"),
])
def test_input_validation(user_input,func,expected_output):

    result = phase.check_input(user_input,func)
    assert result == expected_output




# test updating with valid and invalid inputs
@pytest.mark.parametrize("choice,phase_attributes,user_input", [
    ("Name", ["Name", "Email", "Birth Date"],"ahat aaaaaa"),
    ("Nam", ["Name", "Email", "Birth Date"],"ahat aaaaaa"),
    ("City",["City","Street","Number"],"Lod"),
    ("Happy",["City","Street","Number"],"Lod"),

])
def test_update(choice,phase_attributes,user_input):
    # phase = Phase(1)
    wizard = Wizard()
    # Example of updating a field
    phase.update_phase_field(wizard, choice, phase_attributes,user_input)
    assert wizard.details[choice] == user_input



