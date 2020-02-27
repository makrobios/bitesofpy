from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

@pytest.mark.parametrize('rgb,expected',[
    [[255,255,255], "#FFFFFF" ],
    [[235, 64, 52], "#EB4034" ],
    [[59, 54, 54], "#3B3636" ],
    ]) 
@patch("color.sample")
def test_gen_hex_color(mock_sample, gen, rgb, expected):
    mock_sample.return_value = rgb 
    assert next(gen) == expected 
    mock_sample.assert_called_with(range(0,256),3)
