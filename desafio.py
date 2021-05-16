import time
from datetime import date

def valor_investido():
    return float(input("Digito o valor que deseja investir: R$ "))

def total_visualizacoes(valor_investido):
    return (valor_investido * 21.6) * 4 + (valor_investido * 30)

def gerenciamento():
    cadastro_anuncio = []
    while True:
        print("Digite a opçõa desejada: ")
        print("1 - Cadastro de Anúncio")
        print("2 - Relatório de anuncio")
        print("3 - Consultar Anúncio")
        print("4 - Sair")
        opcao=int(input(" Digite opção?  "))
        #Cadastro de anuncio
        if opcao == 1:
            nome = input(" Escreva o nome do anúncio: ")
            cliente = input(" Digite o nome do cliente: ")
            print("Inicio de investimento ?")
            dia = int(input("Dia: "))
            mes = int(input("Mes: "))
            ano = int(input("Ano: "))
            print("\n\n Quando encerrará Investimento ? \n")
            dia_final = int(input("Dia: "))
            mes_final = int(input("Mes: "))
            ano_final = int(input("Ano: "))
            valor_investido = float(input("\n Quanto deseja investir por dia ? R$ "))
            dias_contados = (date(year = ano_final, month=mes_final, day=dia_final) - date(year=ano, month=mes, day=dia))
            total_investido = float(dias_contados.days *valor_investido)
            numero_views = float((total_investido * 21.6) * 4 + (total_investido * 30))
            total_cliques = float(dias_contados.days * 3.6 * valor_investido)
            total_compartilhamento = float(dias_contados.days * 0.54 * valor_investido)
            cadastro_anuncio.append((nome,cliente,valor_investido, ano,mes,dia,ano_final,mes_final,dia_final, total_investido, numero_views,total_cliques, total_compartilhamento))
            print("\n" * 130)
        #relatorio
        elif opcao == 2:
            for anuncio in cadastro_anuncio:
                nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                print(f'Nome: {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f"%total_investido}'
                      f'\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}\n'
                      f'Visualizações: {"%.2f"%numero_views}\n')
        #buscar             
        elif opcao == 3:
            print("1. Procurar por cliente"
           "\n2. Procurar por período")

            opcao = int(input("Opção: \n"))
            #procurar por cliente
            if opcao == 1:
                cliente_desejado = input("Nome do cliente: ")
                for anuncio in cadastro_anuncio:
                    nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                    if cliente == cliente_desejado:
                        print(
                        f'Nome:  {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f"%total_investido}\n'
                        f'Visualizações: {"%.2f"%numero_views}\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}')
                        print("\n" * 2)
                    else:
                        print("Cliente não encontrado")
                        break
            #procurar por periodo
            elif opcao == 2:
                ano_periodo = int(input("ANO: "))
                mes_periodo = int(input("MES: "))
                dia_periodo = int(input("DIA: "))
                for anuncio in cadastro_anuncio:
                    nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                if date(year=ano_periodo, month=mes_periodo, day=dia_periodo) >= date(year=ano, month=mes, day=dia) and date(
                        year=ano_periodo, month=mes_periodo, day=dia_periodo) <= date(year=ano_final, month=mes_final, day=dia_final):
                    for anuncio in cadastro_anuncio:
                        nome, cliente, valor_investido, ano, mes, dia, ano_final, mes_final, dia_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio

                        print(

                        f'Nome:  {nome}\nCliente: {cliente}\nValor investido: R$ {"%.2f"%valor_investido}\nTotal investido: R$ {"%.2f"%total_investido}\n'
                        f'Visualizações: {"%.2f"%numero_views}\nTotal de cliques: {"%.2f"%total_cliques}\nTotal de compartilhamento: {"%.2f"%total_compartilhado}')

                        print("\n" * 2)
                else:
                    print("cliente não encontrado: ")
            else:
                print("Opção Inválida")  
        #sair  
        elif opcao == 4:
            break
        else:
            print("Opção Inválida")
        
        



gerenciamento()
