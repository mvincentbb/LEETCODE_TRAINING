# 1 --> un 
# 2

# 99
# 100 -- 
# 200 deux cent === nombrefrancais9(2) - "cent"
# 300 trois cent === nombrefrancais9(3) - "cent"
# 400 quatre cent === nombrefrancais9(4) - "cent"
# 500 cinq cent === nombrefrancais9(5) - "cent"
# 600 six cent === nombrefrancais9(5) - "cent"
# 700 sept cent === nombrefrancais9(5) - "cent"
# 800 huit cent === nombrefrancais9(5) - "cent"
# 900 neuf cent === nombrefrancais9(9) - "cent"



# 999-> neuf-cent-quatre-vingt-dix-neuf


# 10 20 30 40 50 60 70 80 90
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

# 1---10 20 --- 30 -40---50-----90---99
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

# 11 -- 16 
# 17 nombreDizaine(1) - nombreFrancais9(7)
# 18 nombreDizaine(1) - nombreFrancais9(8)
# 19 nombreDizaine(1) - nombreFrancais9(9)

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

# 1 -------- 99

def nombreFrancais99(n):
    #dizaines 20 
    dizaines = [20, 30, 40, 50, 60]
    if n <= 19: #0 --19
        return nombreFrancais19(n)
    elif n in dizaines: # 20 30 40 50 60 
        return nombreDizaineFrancais6(n // 10)
    elif n <= 69: # 
        return nombreDizaineFrancais6(n // 10) + "-" + nombreFrancais9(n % 10)
    elif n <= 79:
        return nombreDizaineFrancais6(6) + "-" + nombreFrancais19(n - 60)
    elif n == 80:
        return "quatre-vingt"
    elif n <= 89:
        return "quatre-vingt" + "-" + nombreFrancais9(n % 10)
    else:
        return "quatre-vingt" + "-" + nombreFrancais19(n - 80)

# si 1 = 2
#     action 1
# sinon si 1 == 0
#     action 2
# sinon si 1 == 2
#     action 3
# sinon
#     action 4

# articles = ["chaussure","sac", " pantalon", "habit"]
# article = "chaussure"
# if article in articles :
#     print(" l'article a ete retrouve")



def nombreFrancais(n):
    centaines = [200, 300, 400, 500, 600, 700, 800, 900]
    if n <= 99:
        return nombreFrancais99(n)
    elif n == 100:
        return "cent"
    elif n in centaines: # n == 200
        return nombreFrancais9(n / 100)  + "-" + "cent" 
        # Etape 1 -->  200// 100 = 9 
        # Etape 2 ---> nombreFrancais9(9) = neuf
        # Etape 3 ---> neuf- cent 
    # 101 - 199
    # 101 = cent un
    
    elif n <= 199:
        return "cent" + "-" + nombreFrancais99(n % 100)
        #  200 - 999
        # 201 = deux cent un
        # 301 = trois cent un
    else:
        return nombreFrancais9(n // 100)  + "-" + "cent" + "-" + nombreFrancais99(n % 100)

# KHLH

def testNombresFrancais():
# # ARRANGE 
#     n = 30
# #ACT
#     result = nombreFrancais(30)
# #ASSERT
#     assert result == "trente"
#    for a in range(200, 400):
#     print(a, "en lettre devint ", nombreFrancais(a))
#     print('\n')

# TEST DE LA FONCTION NOMBRE DIZAINE
    assert nombreDizaineFrancais6(3) == "trente"
    assert nombreDizaineFrancais6(4) == "quarante"
    assert nombreDizaineFrancais6(5) == "cinquante"
    assert nombreDizaineFrancais6(6) == "soixante"

# TEST DE LA FONCTION NOMbre 0 -9
    assert nombreFrancais9(4) == "quatre"
    assert nombreFrancais9(5) == "cinq"
    assert nombreFrancais9(6) == "six"
    assert nombreFrancais9(7) == "sept"
    assert nombreFrancais9(8) == "huit"
#TEST 11- 16 nombreFrancais19(n)
    assert nombreFrancais19(11) == "onze"
    assert nombreFrancais19(12) == "douze"
    assert nombreFrancais19(13) == "treize"
    assert nombreFrancais19(14) == "quatorze"
    assert nombreFrancais19(15) == "quinze"
#TEST 20 --  99 nombreFrancais99()
    assert nombreFrancais99(20) == "vingt"
    assert nombreFrancais99(30) == "trente"
    assert nombreFrancais99(40) == "quarante"
    assert nombreFrancais99(50) == "cinquante"
    assert nombreFrancais99(60) == "soixante"
    assert nombreFrancais99(70) == "soixante-dix"
    assert nombreFrancais99(79) == "soixante-dix-neuf"
    assert nombreFrancais99(90) == "quatre-vingt-dix"
    assert nombreFrancais99(99) == "quatre-vingt-dix-neuf"
    assert nombreFrancais99(90) == "quatre-vingt-dix"

#TEST 20 --  99 nombreFrancais()
    assert nombreFrancais(100) == "cent"
    assert nombreFrancais(200) == "deux-cent"
    assert nombreFrancais(300) == "trois-cent"
    assert nombreFrancais(400) == "quatre-cent"
    assert nombreFrancais(110) == "cent-dix"
    assert nombreFrancais(520) == "cinq-cent-vingt"




# assert RESULTAT_OBTENU estegale RESULTAT_ESCOMPTE, "CE QUE JE DOIS AFFICHE SI CE N EST PAS LA MEME CHOSE"

testNombresFrancais()
