Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emasAwal = 25
>>> hargaBeli = emasAwal * 650000
>>> hargaJual = emasAwal * 685000
>>> keuntungan = hargaJual - hargaBeli
>>> keuntungan
875000
>>> persentaseUntung = (keuntungan/hargaBeli) * 100
>>> persentaseUntung
5.384615384615385
>>> beliEmasLagi = 15 * 685000
>>> totalEmas = emasAwal + 15
>>> totalHargaJual = totalEmas * 715000
>>> totalUntung = totalHargaJual - (hargaBeli + beliEmasLagi)
>>> totalUntung
2075000
>>> totalPersenUntung = (totalUntung/(hargaBeli + beliEmasLagi)) * 100
>>> totalPersenUntung
7.822808671065033
