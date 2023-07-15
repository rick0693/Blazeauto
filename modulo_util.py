from modulo_dataframe import save_to_dataframe


def verificar_numero(color1, color2, color3, color4, count_perdeu_consecutivas):
    if (color1, color2, color3, color4) == (1, 1, 1, 2) or (color1, color2, color3, color4) == (2, 2, 2, 1):
        return 2  # Inverte o retorno para a sequência especificada
    # VVV - P
    elif color1 == 1 and color2 == 1 and color3 == 1:
        return 1
    # PPP- V
    elif color1 == 2 and color2 == 2 and color3 == 2:
        return 2
    # VVP- V
    elif color1 == 1 and color2 == 1 and color3 == 2:
        return 2
    elif color1 == 2 and color2 == 2 and color3 == 1:
        return 1
    elif color1 == 1 and color2 == 2 and color3 == 2:
        return 1
    elif color1 == 2 and color2 == 1 and color3 == 1:
        return 2
    elif color1 == 1 and color2 == 2 and color3 == 1:
        return 2
    elif color1 == 2 and color2 == 1 and color3 == 2:
        return 1
    elif color2 == 0:
        return 2
    elif color1 == 0:
        return 1
    elif color3 == 0:
        return 2
    else:
        return 1
