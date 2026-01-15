def generate_hashtag(s):
    if s == "":
        return False
    else:
        s = "#" + s.title().strip().replace(" ", "")
    return s if len(s) <= 140 else False
