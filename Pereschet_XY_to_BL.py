from math import sin, cos, radians
from functions import zone, func

def pereschet_XY_to_BL(x, y, n):

    betta = round(x / 6367558.4969 * 206265, 8)
    cos_betta = round(cos(radians(betta / 3600)), 12)
    sin_betta = round(sin(radians(betta / 3600)), 12)

    Bx = round(betta + (50221746 + (293622 + (2350 + 22 * cos_betta ** 2)
    * cos_betta ** 2) * cos_betta ** 2) * 10 ** (-10) * sin_betta * cos_betta * 206265, 8)
    cos_Bx = cos(radians(Bx / 3600))
    sin_Bx = sin(radians(Bx / 3600))

    b3 = round(0.333333 - (0.166667 - 0.001123 * cos_Bx ** 2) * cos_Bx ** 2, 8)
    b2 = round((0.5 + 0.003369 * cos_Bx ** 2) * sin_Bx * cos_Bx, 8)
    b4 = round(0.25 + (0.16161 + 0.00562 * cos_Bx ** 2) * cos_Bx ** 2, 8)
    b5 = round(0.2 - (0.1667 - 0.0088 * cos_Bx ** 2) * cos_Bx ** 2, 8)

    Nx = 6399698.902 - (21562.267 - (108.973 - 0.612 * cos_Bx ** 2) * cos_Bx ** 2) * cos_Bx ** 2
    z = round(y / (Nx * cos_Bx), 8)
    l = round((1 - (b3 - b5 * z ** 2) * z ** 2) * z * 206265, 8)

    B = round(Bx - (1 - (b4 - 0.12 * z ** 2) * z ** 2) * z ** 2 * b2 * 206265, 8)
    L = zone(n) * 3600 + l

    return B, L
def answer(B, L, x, y, n):
    user_text = f"""
                <b>Прямоугольные координаты</b>
                <b>Координата х</b>: {x}
                <b>Координата y</b>: {y}
                <b>Зона </b>: {n}
                ------------------------
                <b>Геодезические координаты</b>
                <b>Широта B</b>: {func(B)}
                <b>Долгота L</b>: {func(L)}
            """
    return user_text
