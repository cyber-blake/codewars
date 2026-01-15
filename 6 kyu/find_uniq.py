# def find_uniq(arr): * doesnt work for large arrays
#     res = {arr.count(x): x for x in arr}
#     return res[1]


# def find_uniq(arr): * works only for integer numbers
#     for i in range(len(arr) - 2):
#         l1 = tuple(arr[i : i + 3])
#         a = l1[0]
#         b = l1[1]
#         c = l1[2]
#         print(l1)
#         if a == b == c:
#             continue
#         else:
#             return l1[0] ^ l1[1] ^ l1[2]


def find_uniq(arr):
    for i in range(len(arr) - 2):
        a, b, c = tuple(arr[i : i + 3])
        if a == b == c:
            continue
        else:
            if a == b:
                return c
            elif a == c:
                return b
            else:
                return a
