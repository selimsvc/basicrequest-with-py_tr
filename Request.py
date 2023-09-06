import requests
import time
import os

try:
  os.system("cls")
except:
  pass

site = input("Link: ")
refresh_interval = input("Yenileme Süresi (saniye): ")
if refresh_interval.isdigit():
    refresh_interval = int(refresh_interval)
else:
    print("Geçersiz değer girdiniz. Yenileme süresi 300 saniye olarak ayarlandı.")
    refresh_interval = 300
refresh_count = input("Yenileme Sayısı: ")
if refresh_count.isdigit():
    refresh_count = int(refresh_count)
else:
    print("Geçersiz değer girdiniz. Yenileme sayısı 6 olarak ayarlandı.")
    refresh_count = 6

count = 0
while True:
  try:
    os.system("cls")
  except:
     pass
  response = requests.get(site)
  count += 1
  print(f"[Sıra No: {count}] Link: {site}")
  if(count == refresh_count):
     break
  time.sleep(refresh_interval)

if(count == refresh_count):
  try:
    os.system("cls")
  except:
    pass
  print(f"Program sonlandı. {refresh_interval} saniye aralıklarla {refresh_count} kere tekrarlandı.")
  print("Çıkmak için ENTER'a basın...")
  print()
  input()
  quit()