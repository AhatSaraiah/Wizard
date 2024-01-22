import pytest
from unittest.mock import patch
from splash import splashscreen  

def test_splashscreen_start():
    '''
    Test the behavior of splashscreen when the user provides input 'start'.

    This test uses the unittest.mock.patch to temporarily replace the built-in input
    function and simulate user input of 'start'. It then asserts that the splashscreen
    function returns True, indicating that it handled the input correctly.

    '''
    with patch("builtins.input", return_value="start"):
        assert splashscreen() == True

def test_splashscreen_invalid_input():
    '''
    Test the behavior of splashscreen when the user provides an invalid input.

    This test uses the unittest.mock.patch to simulate user input of 'invalid_input'.
    It asserts that the splashscreen function returns None, indicating that it handled
    the invalid input correctly.
    
    '''
    with patch("builtins.input", return_value="invalid_input"):
        assert splashscreen() is None




