def formater_Num_Acc(x):
    try:
        return int(x)
    except:
        return 0


######################
# Vehicle
######################

def formater_catv(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x or x > 99:
        return 0
    else:
        return x


######################
# User
######################

def formater_place(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x or x > 9:
        return 0
    else:
        return x


def formater_catu(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x or x > 3:
        return 0
    else:
        return x


def formater_grav(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x or x > 4:
        return 0
    else:
        return x


def formater_sexe(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x or x > 2:
        return 0
    else:
        return x


def formater_an(x):
    try:
        return int(x)
    except:
        return 0


######################
# Places
######################

def formater_surf(x):
    try:
        x = int(x)
    except:
        return -1
    if 1 > x or x > 9:
        return -1
    else:
        return x


######################
# Characteristic
######################

def formater_lum(x):
    try:
        x = int(x)
    except:
        return 0
    if 0 > x > 5:
        return 0
    else:
        return x


def formater_atm(x):
    try:
        x = int(x)
    except:
        return -1
    if 1 > x or x > 9:
        return -1
    else:
        return x


def formater_lat(x):
    try:
        x = int(x)
    except:
        return -1
    if 0 > x:
        return -1
    else:
        return x


def formater_dept(x):
    try:
        x = int(x)
    except:
        if x == "2A" or x == "2B":
            return x
        else:
            return "00"
    if x <= 970:
        x = int(x / 10)
    if x < 10:
        x = "0" + str(x)
    elif x == 20:
        x = "00"
    return str(x)
