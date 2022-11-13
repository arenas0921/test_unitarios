def area_rectangulo(base, altura):
    if not isinstance(base, (int, float)):
        raise ValueError("base debe ser de tipo numerico")
    if not isinstance(altura, (int, float)):
        raise ValueError("altura debe ser de tipo numerico")
    if base < 0:
        raise ValueError("base debe ser un numero positivo")
    if altura < 0:
        raise ValueError("altura debe ser un numero positivo")
    return base * altura


if __name__ == '__main__':

    rectangulos = ((4, 2), (3.3, 5), (-2, 8), (True, 4), ('Hola', 2))

    for rectangulo in rectangulos:
        base, altura = rectangulo
        area = area_rectangulo(base, altura)
        print(f'El area del rectangulo con base {base} y altura {altura} es area {area}')
