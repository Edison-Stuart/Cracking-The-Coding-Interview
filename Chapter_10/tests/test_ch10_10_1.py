from ..ch10_10_1 import merge, ArraySizeError
import pytest

@pytest.mark.parametrize('arr1, arr2, expected', [
    (
    [5,7,9,27.5,31,None,None,None,None,None,None,None,None,None],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,5,6,7,7,8,9,9,27.5,31]
    ),
    (
    [5,7,9,11,15,27.5,31,None,None,None,None,None,None,None,None,None,None],
    [1,1.5,2,3,4,5,6,7,8,9],
    [1,1.5,2,3,4,5,5,6,7,7,8,9,9,11,15,27.5,31]
    )
])
def test_merge(arr1, arr2, expected):
    assert merge(arr1, arr2) == expected
    
@pytest.mark.parametrize('arr1, arr2', [
    (
    [5,7,9,27.5,31,None,None,None,None,None,None,None,None],
    [1,2,3,4,5,6,7,8,9]
    ),
    (
    [5,7,9,11,15,27.5,31,None,None,None,None],
    [1,1.5,2,3,4,5,6,7,8,9],
	)
])
def test_merge_fail(arr1, arr2):
    with pytest.raises(ArraySizeError):
        merge(arr1, arr2)
