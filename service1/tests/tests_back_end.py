import pytest
from application.routes import random_number

def test_randnum():
    assert type(random_number()) == dict
