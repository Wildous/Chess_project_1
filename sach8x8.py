# Reprezentácia šachovnice (8x8)
# v/V = veža, j/J = jazdec, s/S = strelec, d/D = dáma, k/K = kráľ, p/P = pešiak

# Velke pismena Biela, Male pismena Cierna 

board = [
    ["v", "j", "s", "d", "k", "s", "j", "v"], # 0. riadok (čierne figúrky)
    ["p", "p", "p", "p", "p", "p", "p", "p"], # 1. riadok (čierni pešiaci)
    [".", ".", ".", ".", ".", ".", ".", "."], # 2. riadok (prázdny)
    [".", ".", ".", ".", ".", ".", ".", "."], # 3. riadok (prázdny)
    [".", ".", ".", ".", ".", ".", ".", "."], # 4. riadok (prázdny)
    [".", ".", ".", ".", ".", ".", ".", "."], # 5. riadok (prázdny)
    ["P", "P", "P", "P", "P", "P", "P", "P"], # 6. riadok (bieli pešiaci)
    ["V", "J", "S", "D", "K", "S", "J", "V"]  # 7. riadok (biele figúrky)
]

def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print(8 - i)
    print("  a b c d e f g h")

def preved_suradnicu(policko):
    mapa_pismen = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    pismeno = policko[0]
    cislo = policko[1]
    stlpec = mapa_pismen[pismeno]
    riadok = 8 - int(cislo)
    return riadok, stlpec
    
def piece_move():
    tah_hraca = input("what's your move ? ")
    print(tah_hraca)

    start, ciel = tah_hraca.split()
    print("Pohyb políčka", start, "na políčko", ciel)
    preved_suradnicu(start)

    start_riadok, start_stlpec = preved_suradnicu(start)
    print(start_riadok, start_stlpec)

print_board(board)
piece_move()


