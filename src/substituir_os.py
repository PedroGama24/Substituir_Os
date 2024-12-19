import csv

# Função para substituir os textos
def substituir_servicos(servicos):
    servicos_substituidos = []
    for servico in servicos:
        if "Mudança de Endereço" in servico:
            servico = servico.replace("Mudança de Endereço", "Mudança")
        if "Reparo Corretivo" in servico:
            servico = servico.replace("Reparo Corretivo", "Reparo")
        if "Mudança de Cômodo" in servico:
            servico = servico.replace("Mudança de Cômodo", "Cômodo")
        if "Upgrade/Downgrade" in servico:
            servico = servico.replace("Upgrade/Downgrade", "Upgrade")
        if "Troca de ONU - Preventivo" in servico:
            servico = servico.replace("Troca de ONU - Preventivo", "Troca")
        if "Reparo Preventivo" in servico:
            servico = servico.replace("Reparo Preventivo", "Reparo")
        servicos_substituidos.append(servico)
    return servicos_substituidos

# Lista de serviços
servicos = [
    "ALCIR DA SILVA FRAGA	Ativação",
    "ANDRE COUTINHO RODRIGUES	Ativação",
    "ANDRE COUTINHO RODRIGUES	Mudança de Endereço",
    "ANDRE COUTINHO RODRIGUES	Upgrade/Downgrade",
    "ANDRE COUTINHO RODRIGUES	Upgrade/Downgrade",
    "ANDRE COUTINHO RODRIGUES	Ativação",
    "LEANDRO MONTEIRO TEIXEIRA	Mudança de Endereço",
    "LEANDRO MONTEIRO TEIXEIRA	Mudança de Endereço",
    "LEANDRO MONTEIRO TEIXEIRA	Upgrade/Downgrade",
    "RAFAEL SCARP CARVALHO 	Ativação",
    "RAFAEL SCARP CARVALHO 	Mudança de Endereço",
    "RAFAEL SCARP CARVALHO 	Mudança de Endereço",
    "RAFAEL SCARP CARVALHO 	Mudança de Endereço",
    "RAFAEL SCARP CARVALHO 	Ativação",
    "THALYSON FERREIRA DE SOUZA TOLEDO	Ativação",
    "THALYSON FERREIRA DE SOUZA TOLEDO	Ativação",
    "THALYSON FERREIRA DE SOUZA TOLEDO	Ativação",
    "THALYSON FERREIRA DE SOUZA TOLEDO	Ativação",
    "THALYSON FERREIRA DE SOUZA TOLEDO	Ativação",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Ativação",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Ativação",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Ativação",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Ativação",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Upgrade/Downgrade",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Mudança de Endereço",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Mudança de Endereço",
    "YURI LUIZ GRANADEIRO DE MEDEIROS	Ativação",
    "Higor Henrrique Penido	Ativação",
    "Higor Henrrique Penido	Reparo Corretivo",
    "Higor Henrrique Penido	Ativação",
    "IAGO OLIVEIRA DA SILVA	Ativação",
    "IAGO OLIVEIRA DA SILVA	Ativação",
    "MAGNO FERNANDO INACIO CARVALHO	Ativação",
    "MAGNO FERNANDO INACIO CARVALHO	Ativação",
    "MAGNO FERNANDO INACIO CARVALHO	Ativação",
    "MAGNO FERNANDO INACIO CARVALHO	Ativação",
    "MAGNO FERNANDO INACIO CARVALHO	Mudança de Endereço",
    "MARCUS VINICIUS PINHEIRO RAMOS 	Mudança de Endereço",
    "MARCUS VINICIUS PINHEIRO RAMOS 	Ativação",
    "RENAN MARINHO DA SILVA	Ativação",
    "RENAN MARINHO DA SILVA	Ativação",
    "HELDER MARLON DOS SANTOS LIMA	Ativação",
    "HELDER MARLON DOS SANTOS LIMA	Mudança de Endereço",
    "THALES VIEIRA BAZILIO	Ativação",
    "THALES VIEIRA BAZILIO	Ativação",
    "THALES VIEIRA BAZILIO	Ativação",
    "THALES VIEIRA BAZILIO	Ativação",
    "DOUGLAS PINHEIRO BANDEIRA	Reparo Corretivo",
    "DOUGLAS PINHEIRO BANDEIRA	Upgrade/Downgrade",
    "DOUGLAS PINHEIRO BANDEIRA	Upgrade/Downgrade",
    "DOUGLAS PINHEIRO BANDEIRA	Mudança de Endereço",
    "ALCIR DA SILVA FRAGA	Mudança de Endereço",
    "ALCIR DA SILVA FRAGA	Ativação",
    "MATTHEUS GONCALVES MALTEZ	Mudança de Endereço",
    "MATTHEUS GONCALVES MALTEZ	Mudança de Endereço",
    "MATTHEUS GONCALVES MALTEZ	Ativação",
    "MATTHEUS GONCALVES MALTEZ	Mudança de Endereço",
    "JOAO HENRIQUE DE JESUS	Ativação",
    "JOAO HENRIQUE DE JESUS	Ativação",
    "JOAO HENRIQUE DE JESUS	Mudança de Endereço",
    "JULIANO SANTOS DA SILVA CHAGAS	Mudança de Endereço",
    "JULIANO SANTOS DA SILVA CHAGAS	Ativação",
    "ELDER DE PAULA DELGADO	Ativação",
    "ELDER DE PAULA DELGADO	Ativação",
    "ELDER DE PAULA DELGADO	Ativação",
    "ELDER DE PAULA DELGADO	Ativação",
    "ELDER DE PAULA DELGADO	Ativação",
    "ERISVALDO BRAGA DOS SANTOS	Ativação",
    "ERISVALDO BRAGA DOS SANTOS	Ativação",
    "ERISVALDO BRAGA DOS SANTOS	Ativação",
    "DEIVID SOARES VIEIRA	Mudança de Endereço",
    "DEIVID SOARES VIEIRA	Mudança de Endereço",
    "DEIVID SOARES VIEIRA	Mudança de Endereço",
    "DEIVID SOARES VIEIRA	Mudança de Endereço",
    "DEIVID SOARES VIEIRA	Ativação",
    "EVANDRO FELIPE DA SILVA	Ativação",
    "EVANDRO FELIPE DA SILVA	Ativação",
    "FILIPE ALMEIDA DA SILVEIRA	Mudança de Endereço",
    "FILIPE ALMEIDA DA SILVEIRA	Ativação",
    "MARCIO MARCIANO DO NASCIMENTO	Ativação",
    "MARCIO MARCIANO DO NASCIMENTO	Ativação",
    "MARCIO MARCIANO DO NASCIMENTO	Ativação",
    "MARCIO MARCIANO DO NASCIMENTO	Ativação",
    "PAULO ROBERTO DA SILVA	Ativação",
    "WAGNER JOSE GUERREIRO DA SILVA	Mudança de Endereço",
    "WAGNER JOSE GUERREIRO DA SILVA	Mudança de Endereço",
    "WAGNER JOSE GUERREIRO DA SILVA	Ativação",
    "NAUTO MARINS LEAL	Ativação",
    "NAUTO MARINS LEAL	Ativação",
    "NAUTO MARINS LEAL	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "LEANDRO NEUBANER DE PAULA	Ativação",
    "EDER ADRIANO CANDIDO	Reparo Corretivo",
    "EDER ADRIANO CANDIDO	Reparo Corretivo",
    "EDER ADRIANO CANDIDO	Reparo Corretivo",
    "LENILSON MONTEIRO TEIXEIRA	Ativação",
    "LENILSON MONTEIRO TEIXEIRA	Ativação",
    "LENILSON MONTEIRO TEIXEIRA	Ativação",
    "MAICON PLACIDO FLORZINO 	Ativação",
    "MAICON PLACIDO FLORZINO 	Ativação",
    "MAICON PLACIDO FLORZINO 	Ativação",
    "Patrick Pitzer da Silva	Mudança de Endereço",
    "Patrick Pitzer da Silva	Mudança de Endereço",
]

# Aplicar a função à lista de serviços
servicos_modificados = substituir_servicos(servicos)

# Mapeamento de nomes para números
nome_para_numero = {
    "ALCIR DA SILVA FRAGA": 19,
    "ANDRE COUTINHO RODRIGUES": 44,
    "ARIEL SILVA DE CARVALHO": 37,
    "DEIVID SOARES VIEIRA": 43,
    "DOUGLAS PINHEIRO BANDEIRA": 20,
    "EDER ADRIANO CANDIDO": 29,
    "ELDER DE PAULA DELGADO": 30,
    "ERISVALDO BRAGA DOS SANTOS": 27,
    "EVANDRO FELIPE DA SILVA": 18,
    "FILIPE ALMEIDA DA SILVEIRA": 5,
    "HELDER MARLON DOS SANTOS LIMA": 10,
    "IAGO OLIVEIRA DA SILVA": 26,
    "JOAO HENRIQUE DE JESUS": 14,
    "JOAO PAULO DE LIMA MACIEL": 12,
    "JOSE MAURICIO DA SILVA": 11,
    "JULIANO SANTOS DA SILVA CHAGAS": 34,
    "LEANDRO MONTEIRO TEIXEIRA": 32,
    "LEANDRO NEUBANER DE PAULA": 35,
    "LENILSON MONTEIRO TEIXEIRA": 24,
    "MAGNO FERNANDO INACIO CARVALHO": 25,
    "MAICON PLACIDO FLORZINO": 48,
    "MARCIO MARCIANO DO NASCIMENTO": 23,
    "MARCUS VINICIUS PINHEIRO RAMOS": 47,
    "MATTHEUS GONCALVES MALTEZ": 16,
    "NAUTO MARINS LEAL": 9,
    "PAULO ROBERTO DA SILVA": 15,
    "RAFAEL SCARP CARVALHO": 7,
    "RENAN MARINHO DA SILVA": 22,
    "ROBERIO CARNEIRO": 8,
    "ROBSON MARQUES CARNEIRO": 17,
    "THALES VIEIRA BAZILIO": 45,
    "THALYSON FERREIRA DE SOUZA TOLEDO": 46,
    "WAGNER JOSE GUERREIRO DA SILVA": 28,
    "YURI LUIZ GRANADEIRO DE MEDEIROS": 6,
    "MARCELO JUNIOR LOPES ALBERTASSI": 53,
    "Patrick Pitzer da Silva": 58,
    "HIGOR HENRIQUE PENIDO": 55,
    "GUILHERME DOS SANTOS DE FREITAS": 54,
    "Higor Henrrique Penido": 59,
    "Ativação": 1,
    "Mudança": 4,
    "Cômodo": 9,
    "Reparo": 3,
    "Upgrade": 7,
    "Clean up": 14,
    "Troca": 15,
    "Preventivo": 3
}

# Transformar a lista
lista_transformada = []
for item in servicos_modificados:
    # Separar nome e ação
    partes = item.split()
    nome = ' '.join(partes[:-1])
    acao = partes[-1]
    
    # Substituir nome e ação pelos números correspondentes
    numero_nome = nome_para_numero.get(nome, nome)
    numero_acao = nome_para_numero.get(acao, acao)
    lista_transformada.append([numero_nome, numero_acao])

# Escrever a lista transformada em um arquivo CSV
try:
    with open('lista_transformada.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Ação"])  # Cabeçalhos do CSV
        writer.writerows(lista_transformada)
    print("Lista transformada salva em 'lista_transformada.csv'")
except Exception as e:
    print(f"Erro ao salvar o arquivo CSV: {e}")