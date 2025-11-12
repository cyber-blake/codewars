# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.


# mine
def xo(s):
    return True if s.lower().count("o") == s.lower().count("x") else False


# better
def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")
