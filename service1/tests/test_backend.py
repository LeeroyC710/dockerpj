import pytest
from application.routes import random_number

def test_randnum():
    assert random_number == 2
