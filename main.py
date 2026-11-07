import json

def cadastrar_empregado():
  empregado = dict()
  empregado["nome"] = input("Digite o nome do empregado: ")
  empregado["setor"] = input("Digite o setor: ")
  empregado["cargo"] = input("Digite o cargo: ")
  
  while True:
    salario = input("Digite o salário: ")
    if salario.isdigit():
      empregado["salario"] = float(salario)
      break
    else:
      print("Digite apenas números!")

  with open("empregados.json", "r") as arq:
    empregados = json.load(arq)

  empregados.append(empregado)

  with open("empregados.json", "w") as arq:
    json.dump(empregados, arq, indent=2)

  print("Cadastro realizado com sucesso!\n")

def excluir_cadastro():
  with open("empregados.json", "r") as arq:
    empregados = json.load(arq)

  nome = input("Digite o nome do empregado: ")

  i = 0
  for empregado in empregados:
    if empregado["nome"] == nome:
      empregados.pop(i)
      break
    i += 1

  with open("empregados.json", "w") as arq:
    json.dump(empregados, arq, indent=2)

  print("Exclusão feita com sucesso!\n")

def visualizar_empregados():
  with open("empregados.json", "r") as arq:
    empregados = json.load(arq)

  print("NOME       | SETOR      | CARGO      | SALÁRIO")
  for empregado in empregados:
    print(f"{empregado["nome"]: <10} | {empregado["setor"]: <10}" +
          f" | {empregado["cargo"]: <10} | R${empregado["salario"]: <10}")
  print()

def main():
  while True:
    print("** SISTEMA DE EMPREGADOS **")
    print("[1] Cadastrar")
    print("[2] Excluir")
    print("[3] Visualizar")
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
        visualizar_empregados()

      case 4:
        break

      case _:
        print("Opção inválida!")

if __name__ == '__main__':
  main()