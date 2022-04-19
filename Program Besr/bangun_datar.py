# program utama dari bangun datar

def salam():
    print('Selamat Datang!')

def pilihan_menu():
    print('Silahkan pilih bangun datar')
    print('    a) Persegi')
    print('    b) Persegi Panjang')
    print('    c) Lingkaran')
    print('    d) Segitiga')
    print('    e) Trapesium')
    print('    q) Keluar')
    pilih = input('Pilihan: ')
    if pilih.lower() in ['a', 'b', 'c', 'd', 'e', 'q']:
        return pilih.lower()
    else:
        print(pilih + '? Tolong masukkan pilihan yang benar!')
        return None
    
def loop_utama():
    salam()
    
    while True:
        pilih = pilihan_menu()
        if pilih == None:
            continue
        
        if pilih == 'q':
            print('Keluar...')
            break
        
        if pilih == 'a':
            import persegi_ as persegi
            persegi.loop_utama()
            
        elif pilih == 'c':
            import lingkaran_ as lingkaran
            lingkaran.loop_utama()
            
        elif pilih == 'b':
            import per_panjang as perpanjang
            perpanjang.loop_utama()
            
        elif pilih == 'd':
            import segtiga_ as segitiga
            segitiga.loop_utama()
        
        elif pilih == 'e':
            import trapesium_ as trapesium
            trapesium.loop_utama()
        
        else:
            print('Pilihan tidak ada.')

if __name__ == '__main__':
    loop_utama()
