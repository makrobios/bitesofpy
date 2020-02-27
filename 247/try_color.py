from random import sample
import pytest
from unittest.mock import patch



def gen_hex_color():
    while True:
        r, g, b = sample(range(0, 256), 3)
        yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()

@pytest.fixture()
def gen():
    return gen_hex_color()

@patch("color_test.sample")
def test_gen_hex_color(mock, gen):
    mock.return_value=(255,255,255)
    assert next(gen) != type(float)
    mock.assert_called_with(range(0,256),3)

