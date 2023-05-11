'''
Given a sorted array of n integers that has been
rotated an unknown number of times, write
code to find an element in the array. You may
assume that the array way originally sorted in
increasing order.

There are a few ways to solve this issue.
One way is to unshift the array and then do a binary search.
Another way is to first split the list at the point it was shifted at, then
do a binary search on both of the halves.

in order to find the point where the array originally started, we have to crawl through
the array comparing each value to the previous value. Once we find the point where the previous
value is more than the new value, we know we found the point to split.
If we find our target during this process then we will just return the current index.

The loop to do this would look something like this:

	lists_to_search = []

	for i in range(1, len(rotated_list)):
		current = rotated_list[i]
        previous = rotated_list[i - 1]

        if current == target:
			return i
        if previous == target:
			return i - 1

        if previous < current:
			continue

		if previous > current:
			lists_to_search.append(rotated_list[:i])
			lists_to_search.append(rotated_list[i:])
            break

This would give us two seperate sorted lists that we then can search for our target in.
Alternatively, we could also just stitch the two ends together back in the right order,
then do our search on the new sorted list.

This is version of the code will only search the right half of the list if it has to,
and due to us adding the length of the first list to the right index if it is returned,
this function wil return us the index of our target relative to the original rotated_list
that we recieve.

    	list_to_search = []

    	for i in range(1, len(rotated_list)):
        	current = rotated_list[i]
        	previous = rotated_list[i - 1]

        	if current == target:
        	    return i
        	if previous == target:
        	    return i - 1

        	if previous < current:
        	    continue

        	if previous > current:
        	    list_to_search.append(rotated_list[:i])
        	    list_to_search.append(rotated_list[i:])
        	    break

        left_search = binary_search(
        	list_to_search[0], target, 0, len(list_to_search[0]) - 1)
        if left_search == - 1 or list_to_search[0][left_search] != target:
        	return binary_search(
                list_to_search[1], target, 0, len(list_to_search[1]) - 1
                ) + len(list_to_search[0])

    	return left_search

The next step is for us to implement the binary_search function.
This is a realatively simple algorithm where we split the array into smaller
and smaller parts to search for our target until our target is the "mid" index.

	def binary_search(array, x, low, high):
    if low > high:
        return -1  # Error
    mid = (low+high) // 2
    if array[mid] < x:
        return binary_search(array, x, mid + 1, high)
    if array[mid] > x:
        return binary_search(array, x, low, mid - 1)

    return mid

And that's it! we will get the index of our target from the array
with these two functions.
'''


def search_rotated_list(target: int, rotated_list: list) -> int:
    '''
        Takes a list that may or may not be rotated by a random amount and finds a target index.

    Args:
        target(int): The target number that we are searching for.
        rotated_list(list): The list that we are searching for our target.

    Returns:
        target_index: The index of our target value in relation to our original rotated_list.
    '''
    list_to_search = []

    if len(rotated_list) == 1:
        if target == rotated_list[0]:
            return 0
        return -1

    for i in range(1, len(rotated_list)):
        current = rotated_list[i]
        previous = rotated_list[i - 1]

        if current == target:
            return i
        if previous == target:
            return i - 1

        if previous < current:
            continue

        if previous > current:
            list_to_search.append(rotated_list[:i])
            list_to_search.append(rotated_list[i:])
            break

    if len(list_to_search) == 0:
        return -1
    left_search = binary_search(
        list_to_search[0], target, 0, len(list_to_search[0]) - 1
    )
    if left_search == - 1 or list_to_search[0][left_search] != target:
        right_search = binary_search(
            list_to_search[1], target, 0, len(list_to_search[1]) - 1
        )
        if right_search == -1 or list_to_search[1][right_search] != target:
            return -1

        return right_search + len(list_to_search[0])

    return left_search


def binary_search(array: list, target: int, low: int, high: int) -> int:
    '''
    Takes an array and some other values and returns the index of our target in the array.

    Args:
        array(list): The array that will be split and searched.
        target: our target value.
        low: The beginning index of our list section
        high: the ending index of our list section

    Returns:
        mid: The index in the array that relates to our target.
    '''
    if low > high:
        return -1  # Error
    mid = (low+high) // 2
    if array[mid] < target:
        return binary_search(array, target, mid + 1, high)
    if array[mid] > target:
        return binary_search(array, target, low, mid - 1)

    return mid


my_list = [15, 18, 20, 26, 30, 1, 4, 7, 10, 13]
print(search_rotated_list(7, my_list))
