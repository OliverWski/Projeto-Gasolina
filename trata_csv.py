def trata():

    ## Libs
    import pandas as pd
    import numpy
    import glob
    import pandas as pd
    
    ## Carrega as strings com os caminhos dos arquivos que vamos ler
    list_of_files = glob.glob(
        "C:/Users/oliver.rospendowski/Desktop/Estudo/EstudoPython/output/*.csv"
    )
    print("Iniciando concatenação de bases")
    ## Cria uma lista vazia, que posteriormente vai conter as bases para o concat

    appended_data = []
    for i in list_of_files:

        ## Captura a identificação da base
        identificacao = i.replace(
            "C:/Users/oliver.rospendowski/Desktop/Estudo/EstudoPython/output\\",
            "",
        )
        identificacao = identificacao.replace(
            ".csv",
            "",
        )

        ## Lê a bse
        df = pd.read_csv(i, sep=";")

        ## Atribui a identificação da base
        df["Identificacao da Base"] = identificacao

        ## Salva a base num canto
        appended_data.append(df)
     
    ## Transforma a lista de dataframes em um dataframe
    final = pd.concat(appended_data)

    ## Exporta
    base = final.to_csv(r"C:\Users\oliver.rospendowski\Desktop\Estudo\EstudoPython\Base.csv", sep=";", index = False, encoding = 'utf-8-sig')
    df = pd.read_csv('Base.csv', sep=";", encoding = 'utf-8')
    print("Filtrando dados")
    filtro = df[["Estado - Sigla", "Municipio", "Produto", "Data da Coleta", "Valor de Venda", "Identificacao da Base"]]
    filtro.to_csv('Base.csv', sep=";", encoding = 'utf-8')
    print("Concatenação realizada")
