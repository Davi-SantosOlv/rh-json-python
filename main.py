import json

def cadastrar_empregado():
  empregado = {}

  empregado["nome"] = digitar_str("Digite o nome do empregado: ")
  empregado["setor"] = digitar_str("Digite o setor: ")
  empregado["cargo"] = digitar_str("Digite o cargo: ")
  
  while True:
    salario = input("Digite o salário: ")
    if salario.isdigit():
      empregado["salario"] = float(salario)
      break
    else:
      print("Digite apenas números!")

  with open("empregados.json", "a") as arq:
    json.dump(empregado, arq)


def excluir_cadastro():
  pass

def buscar_empregados():
  pass

def digitar_str(str):
  while True:
    entrada = input(str)
    if entrada.isalpha():
      return entrada
    else:
      print("Digite apenas letras!")

def main():
  while True:
    print("** SISTEMA DE RH **")
    print("[1] Cadastrar empregado")
    print("[2] Excluir cadastro")
    print("[3] Mostrar empregados cadastrados")
    print("[4] Sair")
    opcao = input("Digite uma opção: ")
    
    if not opcao.isdigit():
      print("Digite um número!")
      continue

    opcao = int(opcao)

    match(opcao):
      case 1:
        cadastrar_empregado()

      case 2:
        excluir_cadastro()

      case 3:
        buscar_empregados()

      case 4:
        break

      case _:
        print("Opção inválida!")

if __name__ == '__main__':
  main()