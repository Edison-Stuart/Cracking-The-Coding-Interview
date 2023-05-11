from ..ch10_10_2 import sort_anagram_list, sort_anagrams_by_proximity, create_string_map
import pytest

@pytest.mark.parametrize("my_list, expected", [
    (
    ['hank', 'apples', 'abcdefghijklmnopqrstuvwxyz',
      ')l:hloe', 'oranges', 'hello:)', 'grapes', 'papesl',
      'rngesoa', 'ppesla', 'psgera'
    ],
    ['hank', 'apples', 'papesl', 'ppesla', 'abcdefghijklmnopqrstuvwxyz',
     ')l:hloe', 'hello:)', 'oranges', 'rngesoa', 'grapes', 'psgera'
    ]
    )
])
def test_sort_anagram_list(my_list, expected):
    assert sort_anagram_list(my_list) == expected

def test_create_string_map_invalid():
    with pytest.raises(TypeError):
        create_string_map(['string','string',4,'string','string'])

def test_sort_anagrams_by_proximity_invalid():
    my_arr = ['hams', 'eggs', 'bacon', 'onion', 'apples']
    string_map = create_string_map(my_arr)
    with pytest.raises(Exception):
        sort_anagrams_by_proximity(string_map, my_arr[1:])
