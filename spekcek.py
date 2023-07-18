#CREATED BY ALL IN AKBAR !
#FB : AKBAR CANNAVARO
#YT : ALL IN AKBAR !
#GITHUB : AkbarDTrafalgar
def spekk_hp_spek(ram, storage, cpu_cores, camera_res):
    if ram <= 2 and storage <= 32 and cpu_cores <= 4 and camera_res <= 12:
        return "Kentang"
    elif ram <= 4 and storage <= 64 and cpu_cores <= 8 and camera_res <= 24:
        return "Lumayan"
    else:
        return "Spek Dewa"

#Untuk Text Respon, Silahkan Ubah Sesuka Hati😁
def response_spek(kategori):
    if kategori == "low":
        return ( kuning + "Semangat ya bro semoga kebeli hp baru, maaf ini hp kamu tergolong hp low/kentang:)" + reset )
    elif kategori == "Lumayan":
        return ( biru + "Good Bro Lumayan Speknya, Semoga bisa upgrade ya.." + reset )
    elif kategori == "Spek Dewa":
        return ( hijau + "Gilee Spek Dewa, Enak Ga Sih Pake Spek Setinggi itu:)" + reset )
    else:
        return ( merah + "Njir Kategorinya Ga Ada, Hp Apa Tuh" + reset )

# Kode Ram Untuk Response
ram = 3  # GB
storage = 64  # GB
cpu_cores = 6
camera_res = 16  # MP

#kode warna untuk text
merah = "\033[91m"
hijau = "\033[92m"
kuning = "\033[93m"
biru = "\033[94m"
reset = "\033[0m"

spek = spekk_hp_spek(ram, storage, cpu_cores, camera_res)
response = response_spek(spek)
print(response)
