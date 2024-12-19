from flask import Flask, render_template, request, send_file
import csv
import io

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    servicos = request.form['servicos'].split('\n')
    servicos_modificados = substituir_servicos(servicos)
    
    lista_transformada = []
    for item in servicos_modificados:
        partes = item.split()
        if len(partes) < 2:
            continue  # Ignorar linhas vazias ou mal formatadas
        nome = ' '.join(partes[:-1])
        acao = partes[-1]
        
        numero_nome = nome_para_numero.get(nome, nome)
        numero_acao = nome_para_numero.get(acao, acao)
        lista_transformada.append([numero_nome, numero_acao])
    
    # Criar um arquivo CSV em memória
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Nome", "Ação"])
    writer.writerows(lista_transformada)
    output.seek(0)
    
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='lista_transformada.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)