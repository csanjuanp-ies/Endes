def valid(card_num):
    number = "".join([s for s in card_num if s.isdigit()])
    number_no_spaces = card_num.replace(" ", '')
    ret = False
    suma = 0
    len_number = len(number)
    if len_number > 1 and len_number == len(number_no_spaces):  # Solo puede haber números
        for ele in range(1, len_number + 1, 1):
            if ele % 2 == 0:
                valor = int(number[len_number - ele]) * 2
                if valor >= 10: valor -= 9
                suma += valor
            else:
                suma += int(number[len_number - ele])

        if suma % 10 == 0:
            ret = True
    return ret

# Validate
print(
valid("1"),  # False
valid("0"), # False
valid("059"),  # True
valid("59"),  # True
valid("055 444 285"),  # True
valid("055 444 286"),  # False
valid("8273 1232 7352 0569"),  # False
valid("095 245 88"),  # True
valid("234 567 891 234"),  # True
valid("059a"),  # False
valid("055-444-285"),  # False
valid("055# 444$ 285"),  # False
valid(" 0"),  # False
valid("0000 0"),  # True
valid("091"),  # True
valid("055b 444 285"),  # False
valid(":9"))  # False
