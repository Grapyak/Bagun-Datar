import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

Sisi = []
Luas = []
Keliling = []
Garing = []

def salam():
    print('Anda memilih bangun persegi')

def proper_input(number):
    if not number.isdigit():
        print("'" + str(number) + "' harus berupa angka!")
        return False
    return True

def diket_sisi(sisi_):
    sisi = float(sisi_)
    Sisi.append(sisi)
    print()
    print('Panjang sisi persegi adalah {0:.2f} cm'.format(sisi))

def diket_luas(luas_):
    luas = float(luas_)
    Luas.append(luas)
    print()
    print('Luas persegi adalah {0:.2f} cm\u00b2'.format(luas))

def diket_keliling(keliling_):
    keliling = float(keliling_)
    Keliling.append(keliling)
    print()
    print('Keliling persegi adalah {0:.2f} cm'.format(keliling))

def diket_garing(garing_):
    garing = float(garing_)
    Garing.append(garing)
    print()
    print('Diagonal persegi adalah {0:.2f} cm'.format(garing))
    
def luas(sisi):
    luas = sisi ** 2
    Luas.append(luas)
    print('Luas = sisi x sisi')
    print('Luas = {0:.2f} x'.format(sisi), '{0:.2f}'.format(sisi))
    print('Luas persegi dengan sisi {0:.2f} cm adalah'.format(sisi), \
          '{0:.2f} cm\u00b2'.format(luas))
    print()

def keliling(sisi):
    keliling = 4 * sisi
    Keliling.append(keliling)
    print('Keliling = 4 x sisi')
    print('Keliling = 4 x {0:.2f}'.format(sisi))
    print('Keliling persegi dengan sisi {0:.2f} cm adalah'.format(sisi), \
          '{0:.2f} cm'.format(keliling))
    print()
    
def sisi_luas(Luas):
    sisi = math.sqrt(Luas)
    Sisi.append(sisi)
    print('Sisi = \u221ALuas')
    print('Sisi = \u221A{0:.2f}'.format(Luas))
    print('Panjang sisi dari persegi dengan luas {0:.2f}'.format(Luas), \
          'cm\u00b2 adalah {0:.2f} cm'.format(sisi))
    print()

def sisi_keliling(Keliling):
    sisi = Keliling / 4
    Sisi.append(sisi)
    print('Sisi = Keliling / 4')
    print('Sisi = {0:.2f} / 4'.format(Keliling))
    print('Panjang sisi dari persegi dengan keliling {0:.2f}'.format(Keliling), \
          'cm adalah {0:.2f} cm'.format(sisi))
    print()

def sisi_garis_miring(Garing):
    sisi = Garing / math.sqrt(2)
    Sisi.append(sisi)
    print('Sisi = Diagonal / \u221A2')
    print('Sisi = {0:.2f} / \u221A2'.format(Garing))
    print('Panjang sisi persegi dengan diagonal {0:.2f}'.format(Garing), \
          'cm adalah {0:.2f} cm'.format(sisi))
    print()

def garis_miring(sisi):
    garing = sisi * math.sqrt(2)
    Garing.append(garing)
    print('Diagonal = Sisi\u221A2')
    print('Diagonal = {0:.2f}\u221A2'.format(sisi))
    print('Panjang diagonal adalah {0:.2f} cm'.format(garing))
    print()

def plot_gambar(sisi):
    verts = [
        (0., 0.),
        (0., sisi),
        (sisi, sisi),
        (sisi, 0.),
        (0.,0.)]
    
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY]
    
    labels = '{0:<10}'.format('Sisi') + ' = {0:.2f} cm'.format(Sisi[-1]) \
           + '\n{0:<8}'.format('Luas') + ' = {0:.2f} cm\u00b2'.format(Luas[-1]) \
           + '\n{0:<8}'.format('Keliling') + ' = {0:.2f} cm'.format(Keliling[-1])
              
    path = Path(verts, codes)
    
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor = 'khaki', edgecolor = 'blue',
                              lw=2, label = labels)
    
    ax.add_patch(patch)
    ax.plot([0., sisi], [0., sisi], color = 'red', 
            label = 'Diagonal persegi = {0:.2f} cm'.format(Garing[-1])) 
    ax.set_title('Persegi')
    ax.set_xlabel('Sisi (cm)')
    ax.set_ylabel('Sisi (cm)')
    ax.legend(bbox_to_anchor = (1.1, 1), loc = 'upper left', 
              borderaxespad = 0.)
    ax.margins(0.15, 0.15)
    plt.show()

def pilihan_menu():
    print('Silahkan pilih bagian yang diketahui')
    print('    1) Sisi')
    print('    2) Luas')
    print('    3) Kelling')
    print('    4) Diagonal')
    print('    0) Kembali')
    pilih = input('Pilihan: ')
    if pilih in ['1', '2', '3', '4', '0']:
        return pilih
    else:
        print(pilih +'?' + ' Tolong masukkan pillihan yang benar!')
        return None
    
def loop_utama():
    salam()
    
    while True:
        pilih = pilihan_menu()
        if pilih == None:
            continue
        
        if pilih == '0':
            print('Kembali ke menu utama...')
            break
        
        if pilih == '1':
            sisi_ = input('Masukkan panjang sisi persegi (cm): ')
            if not proper_input(sisi_):
                continue
            diket_sisi(sisi_)
            luas(Sisi[-1])
            keliling(Sisi[-1])
            garis_miring(Sisi[-1])
            plot_gambar(Sisi[-1])
            
        elif pilih == '2':
            luas_ = input('Masukkan luas persegi (cm\u00b2): ')
            if not proper_input(luas_):
                continue
            diket_luas(luas_)
            sisi_luas(Luas[-1])
            keliling(Sisi[-1])
            garis_miring(Sisi[-1])
            plot_gambar(Sisi[-1])
            
        elif pilih == '3':
            keliling_ = input('Masukkan keliling persegi (cm): ')
            if not proper_input(keliling_):
                continue
            diket_keliling(keliling_)
            sisi_keliling(Keliling[-1])
            luas(Sisi[-1])
            garis_miring(Sisi[-1])
            plot_gambar(Sisi[-1])
            
        elif pilih == '4':
            garing_ = input('Masukkan diagonal persegi (cm): ')
            if not proper_input(garing_):
                continue
            diket_garing(garing_)
            sisi_garis_miring(Garing[-1])
            luas(Sisi[-1])
            keliling(Sisi[-1])
            plot_gambar(Sisi[-1])
            
        else:
            print('Pilihan tidak ada.')

    