import string

def is_pangram(inStr):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(inStr.lower())
    return not(alphabet - letters)
    
