import random

print("Sayı tahmin oyununa hoş geldiniz")
iht = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
ts = random.choice(iht)
while True:
    print("1 ile 10 arasında bir sayı seçtim tahmin et")
    y = input()
    if int(y) > int(ts):
        print("Tuttuğum sayı daha küçük")
    elif int(y) < int(ts):
        print("Tuttuğum sayı daha büyük")
    elif int(y) == int(ts):
        print("Doğru bildin, tebrikler!")
        break