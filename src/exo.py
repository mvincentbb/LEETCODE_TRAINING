
def nombreDizaineFrancais6(n):
    if n == 1:
        return "dix"
    elif n == 2:
        return "vingt"
    elif n ==3:
        return "trente"
    elif n == 4:
        return "quarante"
    elif n == 5:
        return "cinquante"
    else:
        return "soixante"

def nombreFrancais9(n):
    if n <= 1:
        return "un"
    elif n == 2:
        return "deux"
    elif n == 3:
        return "trois"
    elif n == 4:
        return "quatre"
    elif n == 5:
        return "cinq"
    elif n == 6:
        return "six"
    elif n == 7:
        return "sept"
    elif n == 8:
        return "huit"
    else:
        return "neuf"

def nombreFrancais19(n):
    if n <= 9:
        return nombreFrancais9(n)
    elif n == 10:
        return nombreDizaineFrancais6(1)
    elif n == 11:
        return "onze"
    elif n == 12:
        return "douze"
    elif n == 13:
        return "treize"
    elif n == 14:
        return "quatorze"
    elif n == 15:
        return "quinze"
    elif n == 16:
        return "seize"
    else:
        return nombreDizaineFrancais6(1) + "-" + nombreFrancais9(n- 10)


def nombreFrancais99(n):
    if n <= 19:
        return nombreFrancais19(n)
    elif n == 20 or n == 30 or n == 40 or n == 50 or n == 60:
        return nombreDizaineFrancais6(n // 10)
    elif n <= 69:
        return nombreDizaineFrancais6(n // 10) + "-" + nombreFrancais9(n % 10)
    elif n <= 79:
        return nombreDizaineFrancais6(6) + "-" + nombreFrancais19(n - 60)
    elif n == 80:
        return "quatre-vingt"
    elif n <= 89:
        return "quatre-vingt" + "-" + nombreFrancais9(n % 10)
    else:
        return "quatre-vingt" + "-" + nombreFrancais19(n - 80)



def nombreFrancais(n):
    if n <= 99:
        return nombreFrancais99(n)
    elif n == 100:
        return "cent"
    elif n in [200, 300, 400, 500, 600, 700, 800, 900]:
        return nombreFrancais9(n // 100)  + "-" + "cent"
    elif n <= 199:
        return "cent" + "-" + nombreFrancais99(n % 100)
    else:
        return nombreFrancais9(n // 100)  + "-" + "cent" + "-" + nombreFrancais99(n % 100)

def testNombresFrancais():

# arrange 
n = 30
#ACT
result = nombreFrancais(30)
#ASSERT
assert result == "trente", "should be trente"
#    for a in range(200, 400):
#     print(a, "en lettre devint ", nombreFrancais(a))
#     print('\n')



testNombresFrancais()
