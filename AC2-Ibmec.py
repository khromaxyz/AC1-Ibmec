def equa_2_grau(a,b,c):
    primeira_raiz = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
    segunda_raiz = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)
    return primeira_raiz, segunda_raiz

def ano_bissexto(ano):
    bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
    return bissexto

def calcula_salario(valor_hora, num_hora, irpf=0.275):
    salario = valor_hora*num_hora*(1-irpf)
    return salario
def main():
    primeira_raiz, segunda_raiz = equa_2_grau()
    print("A primeira raiz da equação é:", primeira_raiz,'\n'
          "A segunda raiz da equação é:", segunda_raiz)
    
    bissexto = ano_bissexto()
    print(bissexto)

    salario = calcula_salario()
    print("O salário líquido é", salario)

main()