import math

#data of reaching for the price 27/03/2026
# reais 1 = 0.19 dolares
# sol peruano 1 = 0.26 dolares
# colombian peso 1 = 0.27 dolares

print('Dolar Calculate $')
print('----------------------\n')
pesos = float(input('How do you have left in pesos CO? '))
reais = float(input('How do you have left in reais BR? '))
soles = float(input('How do you have left in soles PE? '))

#coversion
pesosTransform = pesos * 0.27
reaisTransform = reais * 0.19
solesTransform = soles * 0.26

#result
result = pesosTransform + reaisTransform + solesTransform

print('----------------------\n')
print('You have US$: ', result)
