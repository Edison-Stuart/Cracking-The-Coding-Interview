'''
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.

If you look at these two arrays, you can see that we are already in the process of a mergesort.
We have already split the array into two sorted halves, now all we need to do is merge them.

We can use either a helper array to hold extra values or we could use the extra space in the
array A and fill it backwards.

I am going to make my first solution using a helper array because it seems a little bit easier
to wrap my head around.

Let's start by defining our function that will merge these two arrays.

	def merge(arrayA: list, arrayB: list):

We can make our helper array hold the values in arrayA for the time being,
so we can use the space in arrayA to hold all the sorted values.

		helper_array = []
        i = 0
        while arrayA[i] is not None:
			helper_array.push(arrayA[i])
            i += 1

After we get our values moved over, we can compare the lowest values of helper_array and arrayB;
putting the values from each array in sorted order into arrayA

My first thought was to have two pointer values that represent the index of helper_array and arrayB
that we are on, as well as a third pointer that represents the finished array.

		pointerA = 0
        pointerB = 0
        pointerC = 0

We can then compare the values of each array while incrementing the index indivudualy.
Because we don't want to mutate the original array we can make a deepcopy of arrayA, which
we will be adding to and returning

		arrayA_copy = deepcopy(arrayA)

		while arrayA_copy[-1] is None:
			if pointerA > len(helper_array) - 1:
				for index in range(pointerB, len(arrayB)):
					arrayA_copy[pointerC] = arrayB[index]
                    pointerC += 1
			elif pointerB > len(arrayB) - 1:
				for index in range(pointerA, len(helper_array)):
					arrayA_copy[pointerC] = helper_array[index]
                    pointerC += 1
            elif helper_array[pointerA] < arrayB[pointerB]:
				arrayA_copy[pointerC] = helper_array[pointerA]
                pointerA += 1
                pointerC += 1
            elif helper_array[pointerA] > arrayB[pointerB]:
				arrayA_copy[pointerC] = arrayB[pointerB]
                pointerB += 1
                pointerC += 1
        return arrayA_copy
'''
from copy import deepcopy

class ArraySizeError(Exception):
    """Gets thrown when an array is not the proper size"""


def fill_list(array1: list, pointer1: int, array2: list, pointer2: int) -> None:
    '''
    Function that takes two lists along with associated their associated index

    Args:
        array1: The array that we are copying from.
        pointer1: The index that we want to start array1 at.
        array2: The array that we are copying to
        pointer2: The index that we want to begin filling array2 from.
    '''
    for index in range(pointer1, len(array1)):
        array2[pointer2] = array1[index]
        pointer2 += 1

def set_list_value(array1: list, pointer1: int, array2: list, pointer2: int) -> tuple:
    '''
    Function that copies a value at a specific index from one array to another.

    Args:
        array1: The array that we are copying the value to.
        pointer1: The index of array1 that we copy the value to.
        array2: The array that we are copying from.
        pointer2: The index of array2 that we copy the value from.

    Returns(tuple(list, int, int)):
        array1: The updated array with a new value added
        pointer1, pointer2: The pointers used now incremented to the next value.
    '''
    array1[pointer1] = array2[pointer2]
    pointer1 += 1
    pointer2 += 1

    return array1, pointer1, pointer2

def merge(array_a: list, array_b: list):
    '''
    Function that takes two sorted lists and returns a merged version of them.

    Args:
        array_a: The first array passed into the function, must be pre sorted, as well
            as have enough empty space at the end for array_b to fit into it.

        array_b: The second array passed into the function, also must be pre sorted

    Returns:
        array_a_copy: A sorted version of the combined values of each array.

    Raises:
        ArraySizeError: When array_a does not have the proper number of empty spaces at
            the end of it.
    '''
    helper_array = []
    i = 0
    while array_a[i] is not None:
        helper_array.append(array_a[i])
        i += 1

    if len(array_a[i:len(array_a)]) is not len(array_b):
        raise ArraySizeError("Array_a must have exactly enough None" +
                             " values at the end to hold array_b")


    pointer_a = 0
    pointer_b = 0
    pointer_c = 0


    array_a_copy = deepcopy(array_a)

    while array_a_copy[-1] is None:
        if pointer_a > len(helper_array) - 1:
            fill_list(array_b, pointer_b, array_a_copy, pointer_c)

        elif pointer_b > len(array_b) - 1:
            fill_list(helper_array, pointer_a, array_a_copy, pointer_c)

        elif helper_array[pointer_a] < array_b[pointer_b]:
            array_a_copy, pointer_c, pointer_a = set_list_value(
                array_a_copy,pointer_c,
                helper_array,
                pointer_a)

        elif helper_array[pointer_a] > array_b[pointer_b]:
            array_a_copy, pointer_c, pointer_b = set_list_value(
                array_a_copy,
                pointer_c,
                array_b,
                pointer_b)

        else:
            array_a_copy, pointer_c, pointer_a = set_list_value(
                array_a_copy,
                pointer_c,
                helper_array,
                pointer_a)

    return array_a_copy
