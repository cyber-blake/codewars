def rgb(r, g, b) -> str:
    # if r < 0:
    #     r = 0
    # if g < 0:
    #     g = 0
    # if b < 0:
    #     b = 0

    # if r > 255:
    #     r = 255
    # if g > 255:
    #     g = 255
    # if b > 255:
    #     b = 255
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return f"{r:02X}{g:02X}{b:02X}"
