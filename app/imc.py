print("Programa Cálculo IMC")
print("Digite seu peso exemplo: 56.7 kg e sua altura á 1.76 cm")

peso = float(input("Seu peso em Kg: "))

altura = float(input("Sua altura: "))

imc = peso /altura ** 2

if imc <= 16:

   print(imc)

   print("IMC abaixo de 16 aponta magreza grave.")

elif imc <= 18.5:

   print(imc)

   print("IMC entre 16 e 18.5 aponta magreza moderada.")

elif imc <= 25:

   print(imc)

   print("IMC entre 18.5 e 25 é considerado saudável, apresentando menor risco para doenças.")

elif imc <= 30:

   print(imc)

   print("IMC entre 25 e 30 indica sobrepeso, podendo levar à fadiga, varizes e má circulação.")

elif imc <= 35:

   print(imc)

   print("IMC entre 30 e 35 aponta obesidade de grau I, podendo resultar em diabetes, infarto, angina e aterosclerose.")

elif imc >= 35:

   print(imc)

   print("IMC acima de 35 indica obesidade de grau II (severa), podendo causar falta de ar e apneia do sono")
