#kod dibina oleh ANG KAI XIN
#https://github.com/KaixinAng
#angkaixin0706@gmail.com

ke_nombor_bank_akaun = str('Tolong  hantarkan kiriman wang anda ke RandomBank: 12-3456-78') #boleh ditukarkan
kata_laluan = str('angkaixin') #boleh ditukarkan

def error():    #tunjukkan kesalahan ejaan supaya perisian jalan lancar tanpa ralat
    print ('Sila semak ejaan anda')

def tamat():     #tamat proses dari mana-mana tempat aplikasi
    tekanq = input ('Tekan [q] untuk tamatkan proses')
    if tekanq == ('q'):
      print('Aplikasi ditamatkan.')
      quit()
    else:
        error()

def main():     #pengenalan
    print ('Assalamualaikum dan Selamat Sejahtera!')
    print ('Perisian ini ialah [Hak Asasi Manusia Dilindungi Bersama ––  Program Menghulurkan Bantuan kepada Orang yang Memerlukannya]')
    print ('Saya Ang Kai Xin sebagai pergatur cara perisian ini memang harapkan program ini dapat membantu anda!', '\n')

# if desicion = 1
def minta_bantuan_teks():
  print('\n','Aduhai, tahun ini mesti menyusahkan anda!')
  print('Tapi  jangan risau!')

def tolong_isi_maklumat(): #minta pengguna isi maklumat
  print('\n','Tolong isi maklumat anda.')
  print('''Jangan risau, maklumat penting anda tidak akan terbocor. Kami hanya akan memberitahukan pembantu umur dan kesusahan anda.
Nombor IC dan nama pula untuk memastikan bantuan kami disampaikan kepada anda.
Sementara itu, untuk mengemaskini bilangan bantuan kita dapat  dari perisian ini dan juga memastikan tiada pengguna masukkan maklumat yang salah atau terulang.''','\n')

def minta_bantuan(): #maklumat peminta bantuan
    minta_bantuan_teks()
    tolong_isi_maklumat()
    nama = input('Nama: ')
    umur =input ('Umur: ')
    nomboric = str (input ('Nombor IC: '))
    nombortelefon = str (input ('Nombor telefon: '))
    email = str (input ('Email: '))
    alamat = str (input ('Alamat: '))
    golongan = str (input ('Golongan[t20] / [m40] / [b40] : '))
    kesusahan = str (input ('Kesusahan yang sedang anda mengalami: '))
    with open('list_minta.txt','a') as f:
      f.write('''
              Nama: ''')
      f.write(nama)
      f.write('''
              Umur: ''')
      f.write(umur)
      f.write('''
              Nombor IC: ''')
      f.write(nomboric)
      f.write('''
              Nombor telefon: ''')
      f.write(nombortelefon)
      f.write('''
              Email: ''')
      f.write(email)
      f.write('''
              Alamat: ''')
      f.write(alamat)
      f.write('''
              Golongan: ''')
      f.write(golongan)
      f.write('''
              Kesusahan: ''')
      f.write(kesusahan)
      f.write('''
              ''')
    jenis_bantuan = input('\n','Sila pilih jenis bantuan anda hendak dapatkan: kewangan[1] / mental[2] / tenaga[3] / ketiga-tignya[4]')
    if jenis_bantuan == ('1' or '4' ):
        nombor_bank_akaun = input ('Nombor bank akaun: ') #nombor bank akaun hanya akan dimintakan jika pengguna ingin memberi sokongan kewangan
        with open('list_minta.txt','a') as f:
          f.write('''Nombor bank akuan: ''')
          f.write(nombor_bank_akaun)
    print('\n','Maklumat dikemaskinikan ke dalam sistem kami.')
    print('\n','Permohonan sedang dijalankan. Sila tunggu sehingga pihak kami balas keputusan permohonan anda.')
    print('\n','Tolong “stay safe” dalam masa ini!')

# jika pengguna pilih a
def admin(): #jika pengguna merupakan admin
    pastikan = str(input('Masukkan kata laluan bagi admin.'))
    if  pastikan == kata_laluan:
        print('Selamat sejahtera. Apakah jenis maklumat yang ingin anda lihat? (Maklumat peminta[1] /  Maklumat pembantu[2]')
        print('Tekan [q] untuk tamat process, tekan [n] untuk tambah info di Kilen')
        desicion = str (input (''))
        if desicion == ('1'): 
            with open('list_minta.txt',encoding='utf8') as f:
              for line in f:
                  print(line.strip())
        elif desicion == ('2'):

            with open('list_hulur.txt',encoding='utf8') as f:
              for line in f:
                  print(line.strip())
        elif desicion  == ('q'):
            tamat()
        elif desicion  == ('n'):
            print('Maklumat yang sedia ada di dalam program: ','\n')
            with open('info.txt',encoding='utf8') as f:
              for line in f:
                print(line.strip())
            tambah = ('Ingin tambah maklumat? [ya/tidak]')
            if tambah == ('ya'):
              add = str(input('Tambahkan maklumat:'))
              with open('list_minta.txt','a') as f:
                f.write(add)
            elif tambah == ('tidak'):
              tamat()
            else:
              error()            
        else:
          tamat()
    else: error()

def minta_maklumat(): #maklumat penghulur bantuan
  nama = input('Nama: ')
  umur =input ('Umur: ')
  nomboric = str (input ('Nombor IC: '))
  nombortelefon = str (input ('Nombortelefon: '))
  email = str (input ('Email: '))
  alamat = str (input ('Alamat: '))
  with open('list_hulur.txt','a') as f:
      f.write('''
              Nama: ''')
      f.write(nama)
      f.write('''
              Umur: ''')
      f.write(umur)
      f.write('''
              Nombor IC: ''')
      f.write(nomboric)
      f.write('''
              Nombor telefon: ''')
      f.write(nombortelefon)
      f.write('''
              Email: ''')
      f.write(email)
      f.write('''
              Alamat: ''')
      f.write(alamat)
  
#jika pengguna pilih 2
def hulur_bantuan():
  print('Ribuan terima kasih ingin saya ucapkan kepada anda!')
  tolong_isi_maklumat()
  minta_maklumat() 
  for a in range(0,4):
      jenis_bantuan = input('Sila pilih jenis bantuan boleh anda menghulurkan: kewangan[1] / mental[2] / tenaga[3] / tiada lagi [4]')
      if jenis_bantuan == ('1'):
        print(ke_nombor_bank_akaun) #= input ('Nombor bank akaun: ') #nombor bank akaun hanya akan dimintakan jika pengguna ingin memberi sokongan kewangan
      else:
        pass #print('Nombor bank akaun hanya akan diberi jika pengguna ingin memberi sokongan kewangan.')
      if jenis_bantuan != ('4'):
          with open('list_hulur.txt','a') as f:
            f.write('''
                    Jenis bantuan: ''')
            f.write(jenis_bantuan)
          continue
      else: break  
  print('\n','Maklumat dikemaskinikan ke dalam sistem kami.')
  print('Permohonan sedang dijalankan. Sila tunggu sehingga pihak kami balas keputusan permohonan anda.')
  print('Izinkan saya menyatakan kesyukuran saya kepada tuan/puan sekali lagi')
  print('Tolong “stay safe” dalam masa ini!')
    
#############################
with open('info.txt',encoding='utf8') as f:
    for line in f:
        print(line.strip())

main()
desicion  = str (input ('Anda hendak: meminta bantuan[1] / menghulurkan bantuan[2] / admin[a] / tamat proses[q]'))
if desicion  == ('1'):
    minta_bantuan()
elif desicion  == ('2'):
    hulur_bantuan()
elif desicion  == ('a'):
    admin()
elif desicion  == ('q'):
    tamat()
else:
    error()
    
#############################
#kod dibina oleh ANG KAI XIN
#https://github.com/KaixinAng
#angkaixin0706@gmail.com
