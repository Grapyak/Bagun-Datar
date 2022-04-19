import math
import matplotlib.pyplot as plt

Radius = []
Diameter = []
Luas = []
Keliling = []

def salam():
    print('Anda memilih lingkaran')

def proper_input(number):
    if not number.isdigit():
        print("'" + str(number) + "' harus berupa angka!")
        return False
    return True

def diket_radius(radius_):
    radius = float(radius_)
    Radius.append(radius)
    print()
    print('Radius lingkaran adalah {0:.2f} cm.'.format(radius))

def diket_diameter(diameter_):
    diameter = float(diameter_)
    Diameter.append(diameter)
    print()
    print('Diameter lingkaran adalah {0:.2f} cm.'.format(diameter))

def diket_luas(luas_):
    luas = float(luas_)
    Luas.append(luas)
    print()
    print('Luas lingkaran adalah {0:.2f} cm\u00b2.')
    
def diket_keliling(keliling_):
    keliling = float(keliling_)
    Keliling.append(keliling)
    print()
    print('Keliling lingkaran adalah {0:.2f} cm.')

def radius(diameter):
    radius = 0.5 * diameter
    Radius.append(radius)
    print('Radius = 1/2 * diameter')
    print('Radius = 1/2 * {0:.2f}'.format(diameter))
    print('Radius lingkaran adalah {0:.2f} cm.'.format(radius))
    print()

def radius_luas(luas):
    radius = math.sqrt((luas / math.pi))
    Radius.append(radius)
    print('Radius = \u221A(luas / \u03C0)')
    print('Radius = \u221A({0:.2f} / \u03C0)'.format(luas))
    print('Radius lingkaran dengan luas {0:.2f} cm\u00b2'.format(luas), \
          'adalah {0:.2f} cm'.format(radius))
    print()
    
def radius_keliling(keliling):
    radius = keliling / (2 * math.pi)
    Radius.append(radius)
    print('Radius = keliling / (2 * \u03C0)')
    print('Radius = {0:.2F} / (2 * \u03C0)'.format(keliling))
    print('Radius lingkaran dengan keliling {0:.2f} cm'.format(keliling), \
          'adalah {0:.2f} cm'.format(radius))
    print()

def diameter(radius):
    diameter = 2 * radius
    Diameter.append(diameter)
    print('Diameter = 2 x radius')
    print('Diameter = 2 x {0:.2f}'.format(radius))
    print('Diameter lingkaran adalah {0:.2f} cm.'.format(diameter))
    print()
    
def luas(radius):
    luas = math.pi * radius * radius
    Luas.append(luas)
    print('Luas = \u03C0 x radius\u00b2')
    print('Luas = \u03C0 x {0:.2f}\u00b2'.format(radius))
    print('Luas lingkaran dengan radius {0:.2f} cm adalah'.format(radius), \
          '{0:.2f} cm\u00b2.'.format(luas))
    print()
          
def keliling(radius):
    keliling = 2 * math.pi * radius
    Keliling.append(keliling)
    print('Kelilng = 2 x \u03C0 x radius')
    print('Keliling = 2 x \u03C0 x {0:.2f}'.format(radius))
    print('Keliling lingkaran dengan radius {0:.2f} cm adalah'.format(radius), \
          '{0:.2f} cm'.format(keliling))
    print()
    
def plot_gambar(radius):
    labels = '{0:<8}'.format('Diameter') + ' = {0:.2f} cm'.format(Diameter[-1]) \
           + '\n{0:<11}'.format('Luas') + ' = {0:.2f} cm\u00b2'.format(Luas[-1]) \
           + '\n{0:<11}'.format('Keliling') + ' = {0:.2f} cm'.format(Keliling[-1])
    
    patch = plt.Circle((0., 0.), radius, facecolor = 'khaki', edgecolor = 'blue'
                       , lw = 2, label = labels)
    fig, ax = plt.subplots()
    ax.add_patch(patch)
    ax.plot([0., radius], [0., 0.], color = 'black', ls = '--',
            label = '{0:<10}'.format('Radius') + ' = {0:.2f} cm'.format(Radius[-1]))
    ax.set_title('Lingkaran')
    ax.set_xlabel('Radius (cm)')
    ax.set_ylabel('Radius (cm)')
    ax.legend(bbox_to_anchor = (1.1, 1), loc = 'upper left')
    ax.autoscale_view()
    plt.show()
    

def pilihan_menu():
    print('Silahkan pilih yang diketahui')
    print('    1) Radius')
    print('    2) Diameter')
    print('    3) Luas')
    print('    4) Keliling')
    print('    0) Kembali')
    pilih = input('Pilihan: ')
    if pilih in ['1','2', '3', '4', '0']:
        return pilih
    else:
        print(pilih + '? Tolong masukkan pilihan yang benar!')
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
            radius_ = input('Masukkan radius lingkaran (cm): ')
            if not proper_input(radius_):
                continue
            diket_radius(radius_)
            diameter(Radius[-1])
            luas(Radius[-1])
            keliling(Radius[-1])
            plot_gambar(Radius[-1])
            
        elif pilih == '2':
            diameter_ = input('Masukkan diameter lingkaran (cm): ')
            if not proper_input(diameter_):
                continue
            diket_diameter(diameter_)
            radius(Diameter[-1])
            luas(Radius[-1])
            keliling(Radius[-1])
            plot_gambar(Radius[-1])
            
        elif pilih == '3':
            luas_ = input('Masukkan luas lingkaran(cm\u00b2): ')
            if not proper_input(luas_):
                continue
            diket_luas(luas_)
            radius_luas(Luas[-1])
            diameter(Radius[-1])
            keliling(Radius[-1])
            plot_gambar(Radius[-1])
            
        elif pilih == '4':
            keliling_ = input('Masukkan keliling lingkaran (cm): ')
            if not proper_input(keliling_):
                continue
            diket_keliling(keliling_)
            radius_keliling(Keliling[-1])
            diameter(Radius[-1])
            luas(Radius[-1])
            plot_gambar(Radius[-1])
            
        else:
            print('Pilihan tidak ada.')
