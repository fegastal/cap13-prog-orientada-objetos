def inter(11, 12):
    if 11 == []:
        return 12
    elif 12 == []:
        return 11
    else:
        return [11[0], 12[0]] + inter(11[1:], 12[1:])