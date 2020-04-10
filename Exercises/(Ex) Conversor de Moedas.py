#Conversor de Moedas
rs = float(input("Digite o valor em REAIS (R$): "))

dol = rs / 5.11
bitcoin = rs / 35142.41

print("Com R${} é possível comprar US${} e {} Bitcoin(s)" .format(rs,dol,bitcoin))
