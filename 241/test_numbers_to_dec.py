import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize('arg, expected', [
     ([1,2,3], 123)
    ,([1,0,3], 103)
    ,([0,1,1], 11 )
    ,([0,1,2], 12 )])
def test_list_to_decimal(arg, expected):
    actual = list_to_decimal(arg)
    assert actual == expected
    
@pytest.mark.parametrize('arg', [
     (['4',5,3,1], pytest.raises(TypeError) )
    ,([1,2,True], pytest.raises(TypeError) )   ])
def test_check_type(arg):
    with pytest.raises(TypeError):
        assert list_to_decimal(arg)
        
        
@pytest.mark.parametrize('arg', [
      ([10,2,2] )
     ,([11,10,-10,0])
    ,([-3, 0, 1] )
    ,([10]) ])
def test_check_value(arg):
    with pytest.raises(ValueError):
        assert list_to_decimal(arg)
    with pytest.raises(ValueError):
        assert list_to_decimal([12])