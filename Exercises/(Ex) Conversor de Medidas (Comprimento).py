#Conversor de MEDIDAS (Comprimento)
num = float(input("Digite um número: "))

km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000

print("As medidas de comprimento relacionadas ao número {} são iguais à:\nKM: {}\nHM: {}\nDAM: {}\nDM: {}\nCM: {}\nMM: {} " .format(num,km,hm,dam,dm,cm,mm))
