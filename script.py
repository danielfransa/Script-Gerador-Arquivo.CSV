import csv
import random
import datetime

# Definir as categorias, marcas e descrições
categories = ['Escrita', 'Papelaria', 'Pintura', 'Escolar', 'Escritório']

brands = ['Tilibra', 'Durex', 'Jandaia', 'Chamex', 'Faber-Castel', '3M', 'Bic', 'Pilot']

descriptions = ['Caneta esferográfica colorida','Lápis grafite macio','Borracha escolar branca','Apontador duplo prático','Caderno universitário quadriculado',
                'Agenda escolar diária','Mochila escolar resistente','Régua transparente flexível','Cola branca líquida','Tesoura escolar sem ponta']

produto = [ "Caneta", "Lápis", "Borracha", "Apontador", "Caderno", "Agenda", "Marcador", "Estojo", "Mochila", "Régua", "Compasso", "Transferidor", "Esquadro", 
            "Pasta", "Fichário", "Pincel", "Tinta", "Papel", "Giz de cera", "Lápis de cor", "Canetinha", "Corretivo", "Grampeador", "Clipes", "Cola", "Tesoura", "Giz",
            "Quadro branco", "Apagador", "Estilete", "Fita adesiva", "Pincel atômico", "Calculadora", "Livro", "Mapa", "Lupa", "Bússola", "Projetor", "Aquarela", 
            "Cavalete", "Molde", "Modelador", "Massa de modelar", "Kit Geometria", "Dicionário", "Tesoura escolar", "Papel sulfite", "Cartolina", "Pasta catálogo", 
            "Envelopes", "Cantil", "Garrafa térmica", "Lancheira", "Cadeado", "Lápis preto", "Lápis 6B", "Lápis 2B", "Lápis 4B", "Lápis HB", "Lápis 4H", 
            "Lápis de cor aquarelável", "Caneta esferográfica", "Caneta hidrográfica", "Caneta tinteiro", "Caneta nanquim", "Caneta marca-texto", 
            "Pincel para aquarela", "Borracha branca", "Borracha colorida", "Borracha de apagar a tinta", "Borracha para desenho", "Corretivo em fita", "Corretivo líquido",
            "Fita corretiva", "Agulha de crochê", "Agulha de tricô", "Linha para crochê", "Linha para tricô", "Tinta guache", "Tinta acrílica", "Tinta para tecido", 
            "Tinta para cerâmica", "Tinta para artesanato", "Papel para origami", "Papel crepom", "Papel cartão", "Papel kraft", "Papel cartolina", "Papel seda",    
            "Papel laminado", "Papel autocolante", "Papel colorido",'Folha de EVA glitter', 'Carimbo', 'Carimbo de borracha', 'Papel cartão laminado', 'Rolo de papel',
            'Papel seda crepado', 'Gabarito de desenho','Pincel redondo', 'Lápis de cor aquarelável','Folha de papel sulfite colorido', 'Papel craft', 'Saco plástico',
            'Porta documento',]



# Função para gerar um nome aleatório
def randomName():
    firstNames = ['João', 'Maria', 'Pedro', 'Ana', 'Luís', 'Carla', 'Gustavo', 'Mariana', 'Daniel', 'Guilherme', 'Valdelaine']
    lastNames = ['Silva', 'Santos', 'Pereira', 'Ferreira', 'Oliveira', 'Souza', 'Almeida', 'Chagas', 'Pires', 'Albuquerque']
    firstName = random.choice(firstNames)
    lastName = random.choice(lastNames)
    return f"{firstName} {lastName}"

# Função para gerar uma data aleatória
def randomDate():
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()
    date = start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return date.strftime('%Y-%m-%d')

# Função para gerar uma linha do CSV
def generateRow():
    codVenda = random.randint(0, 1000000)
    dataVenda = randomDate()
    codClient = random.randint(0, 10000)
    nomeCliente = randomName()
    codProduto = random.randint(0, 100000)
    descricao = random.choice(descriptions)
    nome = random.choice(produto)
    categoria = random.choice(categories)
    marca = random.choice(brands)
    valor = round(random.uniform(0.01, 999.99), 2)
    qtd = random.randint(1, 10)
    return f"{codVenda},{dataVenda},{codClient},{nomeCliente},{codProduto},{descricao},{nome},{categoria},{marca},{valor},{qtd}"

# Gerar o arquivo CSV
filename = "escolar.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['cod_venda', 'data_venda', 'cod_client', 'nome_cliente', 'cod_produto', 'descricao', 'nome', 'categoria', 'marcas', 'valor', 'qtd'])
    for i in range(1, 1000001):
        row = generateRow()
        writer.writerow(row.split(','))
        print(f"Gerada linha {i}")
    print(f"Arquivo {filename} gerado com sucesso!")
