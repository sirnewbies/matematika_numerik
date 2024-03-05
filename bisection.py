def fungsi(nilai_x):
    return nilai_x ** 3 + nilai_x ** 2 - 3 * nilai_x ** 1 - 3

epsilon = 0.0001

xn = int(input("masukan xn: "))
xn_tambah_1 = int(input("masukan xn + 1: "))
print("")

fxn = fungsi(xn)
fxn_tambah_1 = fungsi(xn_tambah_1)

xt = fxn * fxn_tambah_1 < 0

while xt:
    xt = (xn + xn_tambah_1) / 2
    print("nilai xt: ", xt)
    fxt = fungsi(xt)
    
    if fxt * fxn < 0:
        xn_tambah_1 = xt
        fxn_tambah_1 = fxt 
        print("nilai xn: ", xn)
        print("nilai xn+1: ", xn_tambah_1)
        print("nilai xt: ", xt)
        print("nilai f(xn): ", fxn)
        print("nilai f(xn+1): ", fxn_tambah_1)
        print("nilai f(xx)2: ", fxt)
        print("")
    
    else :
        xn = xt
        fxn = fxt
        print("nilai xn: ", xn)
        print("nilai fxn: ", fxn)
        
    if abs(fxt) <= epsilon :
        akar = xt
        print("Akar: ",akar)
        break
