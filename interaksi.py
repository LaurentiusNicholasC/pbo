#Laurentius Nihcolas 2215061059
#Arnora Mardiansyah 2215061015
#Theofani Hati K 2255061004
class Mahasiswa:

    def __init__ (self, nama, npm):
        self.nama = nama
        self.npm = npm

    def mengambil(self, matkul):
        print(self.nama + ' mengambil Mata Kuliah ' + matkul.namaMatkul)
        matkul.diambil(matkul.kapasitas, self.nama)

class Mata_kuliah:
    def __init__ (self, namaMatkul, kapasitas):
        self.namaMatkul = namaMatkul
        self.kapasitas = kapasitas

    def diambil(self, kapasitas, nama_mahasiswa):
        self.kapasitas -= 1
        print ('kapasitas tersedia: ' + str(self.kapasitas))
        print (self.namaMatkul + ' diambil oleh ' + nama_mahasiswa)

PBO = Mata_kuliah('PBO', 40)
AI  = Mata_kuliah('AI', 40)

Arnora = Mahasiswa('Arnora', '2215061015')
Nico = Mahasiswa('Nico', '2215061059')
Theofani = Mahasiswa('Theofani', '2215061015')

Arnora.mengambil(PBO)
Nico.mengambil(AI)
Theofani.mengambil(PBO)
