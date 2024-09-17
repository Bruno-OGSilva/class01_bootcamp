COSTANTE_BONUS = 1000

# O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite seu nome: ")
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Insira seu salario: "))
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus = float(input("Insira o seu bonus em %: "))
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
kpi = COSTANTE_BONUS + salario * bonus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f'Olá {nome_usuario}, o seu valor bônus foi de ${kpi}')