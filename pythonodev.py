
 ## furkan katırancı

#mukemmel sayi soru 1 : 
def mukemmel_sayi_mi(sayi):
  toplam = 0
  for i in range(1, sayi):
    if sayi % i == 0:
      toplam += i
  return toplam == sayi

for sayi in range(1, 1000):
  if mukemmel_sayi_mi(sayi):
    print(sayi)

# soru2  ebob bulma
def ebob(sayi1, sayi2):
  i = 1
  while i <= sayi1 and i <= sayi2:
    if sayi1 % i == 0 and sayi2 % i == 0:
      ebob = i
    i += 1
  return ebob

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob(sayi1, sayi2)}")

# soru 3 ekok bulma

def ekok(sayi1, sayi2):
  if sayi1 > sayi2:
    en_buyuk = sayi1
  else:
    en_buyuk = sayi2
  while True:
    if en_buyuk % sayi1 == 0 and en_buyuk % sayi2 == 0:
      ekok = en_buyuk
      break
    en_buyuk += 1
  return ekok

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok(sayi1, sayi2)}")

# soru 4 Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

def sayinin_okunusu(sayi):
  birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
  onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
  sayi_str = str(sayi)
  if len(sayi_str) != 2:
    return "Geçersiz sayı"
  else:
    onlar_basamagi = int(sayi_str[0])
    birler_basamagi = int(sayi_str[1])
    if onlar_basamagi == 1:
      return "on" + birler[birler_basamagi]
    else:
      return onlar[onlar_basamagi] + birler[birler_basamagi]

sayi = int(input("2 basamaklı bir sayı girin: "))
print(f"{sayi} sayısının okunuşu: {sayinin_okunusu(sayi)}")

#soru 5 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor_ucgeni(sayi1, sayi2):
  if sayi1 ** 2 + sayi2 ** 2 == (sayi1 + sayi2) ** 2:
    return True
  else:
    return False

for a in range(1, 101):
  for b in range(1, 101):
    if pisagor_ucgeni(a, b):
      print(f"({a}, {b})")





