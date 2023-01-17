# pylint: disable=bad-indentation
'''Given two strings, write a function to determine if one string is
   a permutation of the other'''

def is_permutation(str1: str, str2: str) -> bool:
	'''function that accepts two strings and returns True
	   if one string is a permutation of the other'''

	if len(str1) is not len(str2):
		return False
    # first, check the length of the two strings, if they are
	# not the same then they cannot be permutations of eachother

    # then, go through each value of one of the strings,
    # and see if it is in the other string.
	for character in str1:
		if character not in str2:
			return False
			# if the character is does not match any in string 2, return false

	# if the function has not returned false by now, the two strings must
	# be permutations of eachother, so we return true
	return True
