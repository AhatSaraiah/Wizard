import pytest
from unittest.mock import patch
from splash import splashscreen  

def test_splashscreen_start():
    with patch("builtins.input", return_value="start"):
        assert splashscreen() == True

def test_splashscreen_invalid_input():
    with patch("builtins.input", return_value="invalid_input"):
        assert splashscreen() is None


        

