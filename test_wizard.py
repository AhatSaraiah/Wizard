import pytest
from wizard import Wizard 

def test_create_phase():
    wizard = Wizard()
    wizard.create_phase(1)
    assert len(wizard.phases) == 1
    assert wizard.phases[0].num_phase == 1


def test_prev_or_next():
    wizard = Wizard()
    wizard.create_phase(1)
    wizard.create_phase(2)

    # Simulate choosing "1" for Next
    wizard.prev_or_next(1)
    assert wizard.phases[-1].num_phase == 2

    # Simulate choosing "2" for Prev
    wizard.prev_or_next(2)
    assert wizard.phases[-1].num_phase == 1


def test_start_wizard():
    wizard = Wizard()
    wizard.start_wizard()


