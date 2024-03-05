"""
Programação Estruturada
2024.1
05/03/2024

AC4
"""

def ler_nome_usuario():
    return input("Informe o seu nome: ")

def ler_notas():
    ap1 = float(input("Informe sua nota na ap1:"))
    ap2 = float(input("Informe sua nota na ap2:"))
    asub = float(input("Informe sua nota na asub:"))
    ac = float(input("Informe sua nota na ac:"))
    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    """
    Retorna False se pelo menos uma das notas for menor que zero ou
    maior que dez.
    """
    if ap1 < 0 or ap1 > 10:
        return False
    elif ap2 < 0 or ap2 > 10:
        return False
    elif asub < 0 or asub > 10:
        return False
    elif ac < 0 or ac > 10:
        return False    
    return True      

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as informadas.
    """
    if ap1 <= ap2 and ap1 <= asub:
        return ap2, asub
    if ap2 <= ap1 and ap2 <= asub:
        return ap1, asub
    if asub <= ap1 and asub <= ap2:
        return ap1, ap2

def calcular_media(n1, n2, ac):
    """
    Calcula e retorna a média do usuário.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media, nome):
    """
    Informa se o aluno passou ou não na disciplina.
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns,", nome , " você foi aprovado!")
    else:
        print("Você foi reprovado...")

def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media, nome)

main()