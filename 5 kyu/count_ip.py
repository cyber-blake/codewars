# def ips_between(start: str, end: str) -> int:
#     octets1 = start.split(".")
#     x1, y1 = int(octets1[2]), int(octets1[3])  # * два последних числа первого айпи
#     octets2 = end.split(".")
#     x2, y2 = int(octets2[2]), int(octets2[3])  # * два последних числа второго айпи
#     res = (y2 - y1) % 256
#     return res if res != 0 else 256
# Работает только для последнего октета
def ips_between(start: str, end: str) -> int:
    import ipaddress

    # a, b, c, d = map(int, start.split("."))
    # x, y, z, i = map(int, end.split("."))
    # # end_bin = ".".join(bin(int(x))[2:].zfill(8) for x in end.split("."))
    # decimal_ip_1 = a * 256**3 + b * 256**2 + c * 256 + d
    # decimal_ip_1 = x * 256**3 + y * 256**2 + z * 256 + i
    # return abs(decimal_ip_1 - decimal_ip_1)
    addr1 = ipaddress.IPv4Address(start)
    addr2 = ipaddress.IPv4Address(end)

    # Преобразуем в int
    n1 = int(addr1)
    n2 = int(addr2)

    # Возвращаем разницу (не включая границы)
    return abs(n2 - n1) - 1


print(ips_between("10.0.0.0", "10.10.0.50"))
