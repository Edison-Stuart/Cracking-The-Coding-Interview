'''
Write A method to sort an array of strings so that all the anagrams are next to each other.

This problem can be broken into two sub-sections, the first being consume the list of strings
and find all the strings that are anagrams. The second is to sort these anagrams to be next
to eachother in the list.

We can do the first part by creating some sort of map from the string into a set of the specific
letters the string contains, and then comparing those instad of the base string.

We can create this map a few ways. I want to create it using a function that consumes the list
of strings that we have, then builds out a set of each character that appears in the list.
We can use this set for each individual word to determine how many of each character appears.

Like so:

	['hello', 'goodbye', 'abcdefg', 'who', 'what']

would be broken down into

	('h', 'e', 'l', 'o', 'g', 'd', 'b', 'y', 'a', 'c', 'f', 'w', 't')

Then this set would be used as keys to a dictionary that holds the value of how many
time a given character has appeared.

Something like this:

	For the first string:
		{'h': 1, 'e': 1, 'l': 2, 'o': 1, 'g': 0, 'd': 0, 'b': 0, 'y': 0, 'a': 0,
        'c': 0, 'f': 0, 'w': 0, 't': 0}
		'hello'

The second step would be to take these maps that we've created and sort by those
instead of sorting by the original strings. We will have to sort both this new list
of maps and the list of strings.

Note when I say sort I just mean ensuring that the maps which are the same are next to eachother
in the list.

The function that creates this map for us accepts a list and returns a dict.
it will just run one time to give us the base map we need.
then we will copy it and fill it out for each individual string.

To do this we can use the reduce function from functools to get one large string that
is all the strings combined. We can the turn this into a set and use the
set as keys that we return.

	def create_string_map(anagram_list: list[str]) -> dict:
		combined_anagram_set = set(reduce(lambda str1,str2 : str1 + str2, anagram_list))
        return {x : 0 for x in combined_anagram_set}

We can use this function to create a list with as many copies
of this map as there are strings. Then we go through the strings and the new list
using the same index and fill out the maps.

To do the second part of this problem, which is sorting the two lists at the same time;
we can create a function that accepts two lists and sorts them so
all anagrams are next to eachother. In order to maintain a pure function we will
copy these lists before changing them at all.
From this function we will return our sorted list which we can return from our top level function.

We also want to throw an error if our map and list are not the same length.

We can use a few different sorting algorithms to figure this out. Ultimately what we need is
for our algorithm to check if any number of these dictionaries are equal to eachother, and if so,
we need to then put them next to eachother.

	def sort_anagrams_by_proximity(string_map: list, string_list: list) -> list:
		if len(string_map) is not len(string_list):
			raise SomeCustomError()

We can throw an exception if string map and string list are not the same.

		sorted_list = []
		indices_sorted = []

        string_map_copy = deepcopy(string_map)
        string_list_copy = deepcopy(string_list)

We can make two empty lists, one for our output and one to help keep track of
ground we have already traveled.

For the sorting, we can use a nested loop which compares each map to each other map.

		for i in range(len(string_list)):

In order to keep down our overhead, we can use the indices_sorted list to skip sections of the loop
which are not needed. We can add the index of each string we add to the sorted_list.

			if i in indices_sorted:
				continue

We can add the initial string to our indices sorted and sorted list arrays.
This way even if a string has no matches it will go into the list and be skipped.

            indices_sorted.append(i)
            sorted_list.append(string_list_copy[i])

            begin_size = len(sorted_list)
			current_map = string_map_copy[i]

In this inner loop we don't want to compare any value to itself, so we first check
if i is ever equal to j or if this index has already been sorted.

			for j in range(len(string_list)):
				if i == j or j in indices_sorted:
					continue

Then finally, we check if our current map is equal to the map at the index we are checking.
If it is, then we have an anagram, or a string with the same letters in a different orientation;
And we add it along with its index to their respective lists.

                if current_map == string_map_copy[j]:
					sorted_list.append(string_list_copy[j])
                    indices_sorted.append(j)

We return the sorted list at the end.

		return sorted_list

So, now that we can create our initial map, and we can sort our list based on the map,
now all we need to do is correctly populate our maps based on the content of each string.

We can do this in our top level solution function because it will not be overly complicated.

	def sort_anagram_list(anagram_list: list) -> list:

We first want to create our 'blueprint' map using our create_string_map function
so we can make an array of them which are the length of the anagram list

        map_list_blueprint = create_string_map(anagram_list)
        map_list = [None] * len(anagram_list)

Then we can do another nested loop, this time using our map list for the outer loop,
and our actual string related to the map_list for our inner loop.

We can create our empty copies from the blueprints as we go along the outer loop.

		for i in range(map_list):
            map_list[i] = copy(map_list_blueprint)

			for j in anagram_list[i]:

We can simply acces our map_list at index i, and loop through the related string,
marking each character amount up by one.

				map_list[i][j] += 1

And then we can return the result of sort_anagrams_by_proximity with our new map list
and our initial anagram list

        return sort_anagrams_by_proximity(map_list, anagram_list)
'''
from functools import reduce
from copy import deepcopy, copy

def create_string_map(anagram_list: list) -> dict:
    '''
    Takes a list of strings and returns a dictionary of the letters in the strings.

    Args:
        anagram_list: A list of strings that will be used to create the 'string map'.

    Raises:
        TypeError: If anagram_list does not contain all strings.

    Returns:
        string_map(dict{str: int}): A set of all the letters contained in anagram_list used
            as keys of a dict.
    '''
    for item in anagram_list:
        if not isinstance(item, str):
            raise TypeError("List must contain strings")
    combined_anagram_set = set(reduce(lambda str1,str2 : str1 + str2, anagram_list).lower())
    return {x : 0 for x in combined_anagram_set}


def sort_anagrams_by_proximity(string_map: list, string_list: list) -> list:
    '''
    Takes a list of dictionaries and a list of strings that coorelate to eachother.

    Args:
        string_map: A list of dictionaries that contain values related to the string_list strings.
            Comes from the function create_string_map.

        string_list: A list of strings that relate to the string_map list. Same list passed into
            create_string_map.

    Raises:
        ArraySizeException
    '''
    if len(string_map) is not len(string_list):
        raise Exception("string_map is not the length of string_list")

    sorted_list = []
    indices_sorted = []

    string_map_copy = deepcopy(string_map)
    string_list_copy = deepcopy(string_list)

    for i in range(len(string_list)):
        if i in indices_sorted:
            continue

        current_map = string_map_copy[i]

        sorted_list.append(string_list_copy[i])
        indices_sorted.append(i)

        for j in range(len(string_list)):
            if i == j or j in indices_sorted:
                continue

            if current_map == string_map_copy[j]:
                sorted_list.append(string_list_copy[j])
                indices_sorted.append(j)

    return sorted_list



def sort_anagram_list(anagram_list: list) -> list:
    '''
    Takes a list of strings and sorts them such that anagrams are next to eachother.

    Args:
        anagram_list(list[str]): A list of strings that may or may not contain anagrams.

    Returns:
        list: a list where every anagram if any are sorted such that they are next to
            each other.
    '''
    map_list_blueprint = create_string_map(anagram_list)
    map_list = [None] * len(anagram_list)
    for i in range(len(anagram_list)):
        map_list[i] = copy(map_list_blueprint)
        for j in anagram_list[i]:
            map_list[i][j] += 1
    return sort_anagrams_by_proximity(map_list, anagram_list)
