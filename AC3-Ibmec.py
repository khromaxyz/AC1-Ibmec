def determina_tipo_triangulo(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo!"

    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

def dia_semana(dia):
    
    if dia == 1:
        return "domingo"
    elif dia == 2:
        return "segunda-feira"
    elif dia == 3:
        return "terça-feira"
    elif dia == 4:
        return "quarta-feira"
    elif dia == 5:
        return "quinta-feira"
    elif dia == 6:
        return "sexta-feira"
    elif dia == 7:
        return "sábado"
    else:
        return ""
    
    """
    Caso o senhor queira pelo match case:

    match dia:
        case 1:
            return "domingo"
        case 2:
            return "segunda-feira"
        case 3:
            return "terça-feira"
        case 4:
            return "quarta-feira"
        case 5:
            return "quinta-feira"
        case 6:
            return "sexta-feira"
        case 7:
            return "sábado"
        case _:
            return ""
    """

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não divida por zero!!!"

def interface_cli():
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    operacao = input("Informe a operação: ")

    if operacao == "soma":
        resultado = soma(num1, num2)
    elif operacao == "subtração":
        resultado = subtracao(num1, num2)
    elif operacao == "multiplicação":
        resultado = multiplicacao(num1, num2)
    elif operacao == "divisão":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida!"

    print("Resultado:", resultado)

def main():
    testa_triangulo()
    testa_dia_semana()
    interface_cli()

main()