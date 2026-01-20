def permutations(s: str) -> list:
    """
    In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
    Create as many "shufflings" as you can!
    :param s: input string
    :output l: list of all perm's
    """
    import random

    l1 = []
    s = list(s)
    # word = ""
    # symb = ""
    # for x in s:  # первый цикл
    #     for y in s:  # второй цикл
    #         word += x
    #     l1.append(word)
    #     word = ""
    # return l1

    # ? another intereting example
    # for _ in range(1000):
    #     l1.append(
    #         random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s)
    #     )
    # return set(l1), len(set(l1))


print(permutations("aabb"))
