def equa_2_grau():
    a = int(input("Informe o parâmetro a da equação:"))
    b = int(input("Informe o parâmetro b da equação:"))
    c = int(input("Informe o parâmetro c da equação:"))
    primeira_raiz = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
    segunda_raiz = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)
    return primeira_raiz, segunda_raiz

def ano_bissexto():
    ano = int(input("Informe o ano: "))
    bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
    return bissexto

def main():
    primeira_raiz, segunda_raiz = equa_2_grau()
    print("A primeira raiz da equação é:", primeira_raiz,'\n'
          "A segunda raiz da equação é:", segunda_raiz)
    bissexto = ano_bissexto()
    print(bissexto)

main()