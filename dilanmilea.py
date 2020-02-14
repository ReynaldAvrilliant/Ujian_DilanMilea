import requests

api_key = "4so5q9zrJyhfJHCqYpmlZWVZBn5ocQTcQ9wMmtGPZk7nTiFTum5zyKb3JiLcEZPH"
url_provinsi = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json"
url_kode_pos = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json"
data_provinsi = requests.get(url_provinsi).json()
kode_pos = requests.get(url_kode_pos).json()
# provinsi milea
provinsi_milea = input("masukan provinsi milea = ").upper()
kabupaten_milea = input("masukan kabupaten milea = ").upper()
kecamatan_milea = input("masukan kecamatan milea = ").upper()
kelurahan_milea = input("masukan kelurahan milea = ").upper()
# provinsi dilan
provinsi_dilan = input("masukan provinsi dilan = ").upper()
kabupaten_dilan = input("masukan kabupaten dilan = ").upper()
kecamatan_dilan = input("masukan kecamatan dilan = ").upper()
kelurahan_dilan = input("masukan kelurahan dilan = ").upper()


kode_provinsi = []
list_provinsi = []
for i in data_provinsi.keys():
    kode_provinsi += [i]
for i in data_provinsi.values():
    list_provinsi += [i]

if provinsi_dilan in list_provinsi:
    index = list_provinsi.index(provinsi_dilan)
    index_dilan = kode_provinsi[index]
if provinsi_milea in list_provinsi:
    index = list_provinsi.index(provinsi_milea)
    index_milea = kode_provinsi[index]

for j in kode_pos[index_dilan]:
    if j["urban"] == kelurahan_dilan:
        if j["sub_district"] == kecamatan_dilan:
            if j["city"] == kabupaten_dilan:
                kode_pos_dilan = j["postal_code"]

for j in kode_pos[index_milea]:
    if j["urban"] == kelurahan_milea:
        if j["sub_district"] == kecamatan_milea:
            if j["city"] == kabupaten_milea:
                kode_pos_milea = j["postal_code"]

urlJarak =  f"https://www.zipcodeapi.com/rest/{api_key}/distance.json/{kode_pos_dilan}/{kode_pos_milea}/km"
data_jarak = requests.get(urlJarak).json()
total_jarak = data_jarak["distance"]

print(f"Kode Pos Dilan = {kode_pos_dilan}")
print(f"Kode Pos Milea = {kode_pos_milea}")
print(f"Jarak Dilan dan Milea =  {total_jarak} km")