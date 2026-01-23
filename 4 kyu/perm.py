from traceback import print_list


def permutations(s: str) -> list:
    """
    In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
    Create as many "shufflings" as you can!
    :param s: input string
    :output l: list of all perm's
    """
    import random

    list_of_results = []
    # ? прототип решения для 4х символьных перестановок
    new_perm = ""
    for first_cycle in s:
        new_perm += first_cycle
        print("first_cycle added")
        for second_cycle in s[1:]:
            new_perm += second_cycle
            print("second cycle added")
            for third_cycle in s[2:]:
                new_perm += third_cycle
                print("third cycle added")
                for fourth_cycle in s[3:]:
                    new_perm += fourth_cycle
                    list_of_results.append(new_perm)
                    print("permutation added!")
                    new_perm = ""
                    # * я почти дошел до нужного решения, главное щас понять на каком моменте нужно обнулять new_perm слово
    return list_of_results


print(permutations("abcd"))


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
