a = int(input("Сколько билетов вы хотите купить?"))
b = int(input("Ваш возраст?"))
s = 0
disc = 10 if a > 3 else 0
k_disk = (100-disc)/100
if b < 18 :
  s = "Вход бесплатный"
elif 18 < b < 25 :
  s = "К оплате: " + str(990 * k_disk)[:-2] + " руб."
else:
  s = "К оплате: " + str(1390 * k_disk)[:-2] + " руб."

print (s)
