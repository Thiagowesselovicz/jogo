from estrutura import soma
from estrutura import subtracao
from estrutura import multiplicacao
from estrutura import divisao







def main():
    print("Calculadora: Escolha uma operação")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    opcao = input("Digite o número correspondente à operação desejada: ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos!")
        return

    if opcao == "1":
        print(f"Resultado: {soma(num1, num2)}")
    elif opcao == "2":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == "4":
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida! Escolha uma operação entre 1 e 4.")

# Executar o programa
if __name__ == "__main__":
    main()
