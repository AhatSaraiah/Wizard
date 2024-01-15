import pytest
from wizard import Wizard  
from phase import Phase

def test_input_validation():
    phase = Phase(1)
    
    # Example of valid input
    assert phase.input_validation("ahat saa", phase.validation_functions["Name"]) == "ahat saa"
    
    # Example of invalid input
    with pytest.raises(ValueError):
        phase.input_validation("Invalid Name", phase.validation_functions["Name"])


def test_run_phase():
    wizard = Wizard()
    phase = Phase(1)
    
    # Example of running phase 1
    phase.run_phase(wizard)
    assert wizard.details["Name"] is not None
    assert wizard.details["Email"] is not None
    assert wizard.details["Birth Date"] is not None


def test_update():
    wizard = Wizard()
    phase = Phase(1)
    wizard.details = {"Name": "ahat saa", "Email": "ahat.saa@gmail.com", "Birth Date": "05/12/1996"}

    # Example of updating a field
    phase.update(wizard)
    assert wizard.details["Name"] is not None

    # Example of updating an invalid field
    with pytest.raises(ValueError):
        phase.update_phase_field(wizard, "Invalid Field", ["Name", "Email", "Birth Date"])


