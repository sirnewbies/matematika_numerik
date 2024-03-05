def fungsi(nilai_x):
    return nilai_x ** 3 + nilai_x ** 2 - 3 * nilai_x ** 1 - 3

print("Contoh: " "0.0001")
epsilon = float(input("Masukan nilai epsilon: "))

xn = float(input("Masukkan nilai xn: "))
xn_tambah_1 = float(input("Masukkan nilai xn + 1: "))
print("")

fxn = fungsi(xn)
fxn_tambah_1 = fungsi(xn_tambah_1)

xt = fxn * fxn_tambah_1 < 0

iterasi = 1

while xt:
    xt = (xn + xn_tambah_1) / 2
    fxt = fungsi(xt)
    
    print("Iterasi ke:", iterasi)
    print("Nilai xn:", xn)
    print("Nilai xn+1:", xn_tambah_1)
    print("Nilai xt:", xt)
    print("Nilai f(xn):", fxn)
    print("Nilai f(xn+1):", fxn_tambah_1)
    print("Nilai f(xt):", fxt)
    print("")
    
    if fxt * fxn < 0:
        xn_tambah_1 = xt
        fxn_tambah_1 = fxt 
        
    else:
        xn = xt
        fxn = fxt
        
    if abs(fxt) <= epsilon:
        akar = xt
        print("Akar:", akar)
        break
        
    iterasi += 1
