'''Check whether the given string is a palindrome.'''

string = input('Input the string for test.\n')

def valid_palindrome(string, start, end):
    if (end-start >= 1):
        if string[start] == string[end]:
            if valid_palindrome(string, start+1, end-1):
                return True
        return False
    else: return True
    return False

if valid_palindrome(string, 0, len(string)-1):
    print('\nGiven string is a palindrome.')
else:
    print('\nGiven string is not a palindrome.')


