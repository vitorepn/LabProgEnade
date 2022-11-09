import pandas as pd
import matplotlib.pyplot as plt


def printResultadosIme():
    print("- - - - - - - - - - Dados do IME - - - - - - - - - -")
    print("Nº de Concluintes Inscritos IME:" + str(imedf['Nº de Concluintes Inscritos'].sum()))
    print("Nº  de Concluintes Participantes IME:" + str(imedf['Nº  de Concluintes Participantes'].sum()))
    print("Nota Bruta - FG IME:" + str(imedf['Nota Bruta - FG'].mean()))
    print("Nota Padronizada - FG IME:" + str(imedf['Nota Padronizada - FG'].mean()))
    print("Conceito Enade (Contínuo) IME:" + str(imedf['Conceito Enade (Contínuo)'].mean()))

if __name__ == '__main__':
    file_name = "enade.xlsx"
    df = pd.read_excel('enade.xlsx')
    imedf = df[df['Sigla da IES'] == 'IME']

    escolha = int(input("Você deseja visualizar o comparativo gráfico? 1 - SIM / 0 - NÃO"))
    if (escolha == 1):
        df.hist(column=["Conceito Enade (Contínuo)"],  bins = 20)
        plt.show()

    while(True):
        print("1 - Geral / 2 - Particular")
        escolha = int(input("Você quer comparar com algum dado geral ou particular?"))
        if(escolha==1 or escolha ==2):
            break
        print("Escolha inválida")

    if(escolha == 1):
        while(True):
            print("1 - Media / 2 - Variância; 3 - Mediana")
            escolha = int(input("Qual dado você deseja consultar?"))
            if(escolha==1 or escolha == 2 or escolha == 3):
                break
            print("Escolha inválida")
        if(escolha == 1):
            print("Nº de Concluintes Inscritos:" + str(df['Nº de Concluintes Inscritos'].mean()))
            print("Nº  de Concluintes Participantes:" + str(df['Nº  de Concluintes Participantes'].mean()))
            print("Nota Bruta - FG:" + str(df['Nota Bruta - FG'].mean()))
            print("Nota Padronizada - FG:" + str(df['Nota Padronizada - FG'].mean()))
            print("Conceito Enade (Contínuo):" + str(df['Conceito Enade (Contínuo)'].mean()))
        if (escolha == 2):
            print("Nº de Concluintes Inscritos:" + str(df['Nº de Concluintes Inscritos'].var()))
            print("Nº  de Concluintes Participantes:" + str(df['Nº  de Concluintes Participantes'].var()))
            print("Nota Bruta - FG:" + str(df['Nota Bruta - FG'].var()))
            print("Nota Padronizada - FG:" + str(df['Nota Padronizada - FG'].var()))
            print("Conceito Enade (Contínuo):" + str(df['Conceito Enade (Contínuo)'].var()))
        if (escolha == 3):
            print("Nº de Concluintes Inscritos:" + str(df['Nº de Concluintes Inscritos'].median()))
            print("Nº  de Concluintes Participantes:" + str(df['Nº  de Concluintes Participantes'].median()))
            print("Nota Bruta - FG:" + str(df['Nota Bruta - FG'].median()))
            print("Nota Padronizada - FG:" + str(df['Nota Padronizada - FG'].median()))
            print("Conceito Enade (Contínuo):" + str(df['Conceito Enade (Contínuo)'].median()))
        printResultadosIme()

    if(escolha == 2):
        estado = input("Você quer comparar com uma universidade de qual estado?").upper()
        print("Dentro desse estado temos os seguintes municípios:")
        UFdf = df[df['Sigla da UF'] == estado]
        print(UFdf['Município do Curso'].unique())

        cidade = input("Você quer comparar com uma universidade de qual cidade?")
        print("Dentro dessa cidade temos as seguintes universidades:")

        cidadedf = df[df['Município do Curso'] == cidade]
        print(cidadedf['Nome da IES'].unique())

        universidade = input("Você quer comparar com qual universidade?").upper()
        unidf = df[df['Nome da IES'] == universidade]

        print("Nº de Concluintes Inscritos:" + str(unidf['Nº de Concluintes Inscritos'].sum()))
        print("Nº  de Concluintes Participantes:" + str(unidf['Nº  de Concluintes Participantes'].sum()))
        print("Nota Bruta - FG:" + str(unidf['Nota Bruta - FG'].median()))
        print("Nota Padronizada - FG:" + str(unidf['Nota Padronizada - FG'].median()))
        print("Conceito Enade (Contínuo):" + str(unidf['Conceito Enade (Contínuo)'].median()))
        printResultadosIme()










