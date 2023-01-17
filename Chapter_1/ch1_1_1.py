'''Determine if a string has any repeated characters'''

def does_repeat(string_input: str) -> bool:
    '''Function that accepts a string then
    return a boolean indicating if the string had repeating characters or not.'''
    for x in range(0, len(string_input)):
        # For each character in the string starting at the first one,
        # check if it is repeated in any later part of the string.
        if string_input[x] in string_input[x+1:]:
            # if it is, return True
            return True
    # if no part of the string makes the function return True,
    # then we return False.
    return False
