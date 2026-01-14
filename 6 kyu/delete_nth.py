def delete_nth(order: list, max_e: int) -> list:
    """
    Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
    For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
    With list [20,37,20,21] and number 1, the result would be [20,37,21].
    """
    # result = []
    # for index, value in enumerate(order):
    #     if order.count(value) > max_e:
    #         continue
    #     else:
    #         result.append(value)
    # return result

    # result = []
    # for index, value in enumerate(order):
    #     if order.count(index) >= max_e:
    #         order.pop(index)
    #     else:
    #         result.append(value)
    # return result
    # harz = {}
    # for x in order:
    #     harz.update(x, "1")
    # return list(harz.keys())

    # harz = {x: order.count(x) for x in order}
    # return list(harz.values())
    result = []
    harz = {x: 0 for x in order}
    for x in order:
        if x in harz:
            harz[x] += 1
            if harz[x] <= max_e:
                result.append(x)

    return result
    # * что дал чатжпт
    # counts = {}
    # result = []

    # for x in lst:
    #     if counts.get(x, 0) < n:
    #         result.append(x)
    #         counts[x] = counts.get(x, 0) + 1


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))  # [1,2,3,1,2,3]
