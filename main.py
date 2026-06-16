from flask import Flask, render_template, request
import random
app = Flask(__name__)

# Criamos aqui a nossa mochila (que são os personagens cadastrados).
# Cada vez que cadastrarmos um novo personagem, vamos adicionar aqui.
mochila_de_pokemons = [
    {
        'nome': 'Pikachu', 'cor': '#f1c40f', 'hp': '⚡ 70 HP',
        'img': 'https://sm.ign.com/ign_br/screenshot/default/fotojet-2024-03-08t101121308_wexc.jpg',
        'atk1': 'Choque do Trovão', 'dano1': '90',
        'atk2': 'Relâmpago', 'dano2': '30',
        'desc': 'Pikachu armazena energia elétrica em suas bochechas.'
    },
    {
        'nome': 'Charmander', 'cor': '#e67e22', 'hp': '🔥 60 HP',
        'img': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png',
        'atk1': 'Arranhão', 'dano1': '40',
        'atk2': 'Lança-Chamas', 'dano2': '80',
        'desc': 'A chama na ponta de sua cauda indica como ele está se sentindo.'
    }
]

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/novo', methods=['POST'])
def novo():
    novo_personagem = {
        'nome': request.form['nome'],
        'cor': '#3498db',  # Uma cor padrão para os novos, ou você pode add um campo de cor no form!
        'hp': request.form['hp'],
        'img': request.form['url'],
        'atk1': request.form['ataque1'], 'dano1': request.form['dano1'],
        'atk2': request.form['ataque2'], 'dano2': request.form['dano2'],
        'desc': request.form['descricao']
    }

    mochila_de_pokemons.append(novo_personagem)

    return render_template('card.html',
                           personagem=novo_personagem,
                           mensagem_sucesso="✨ Carta adicionada à sua coleção com sucesso! ✨"
                           )

@app.route('/colecao')
def colecao():
    return render_template('colecao.html', lista_pokemons=mochila_de_pokemons)

@app.route('/pikachu')
def pikachu():
    # Mantivemos a rota original fixa do Pikachu como exemplo didático
    personagem_exemplo = mochila_de_pokemons[0]
    return render_template('card.html', personagem=personagem_exemplo)

@app.route('/achei')
def achei_um_pokemon():
    # Em vez de uma lista de textos, sorteamos um dicionário inteiro da nossa mochila!
    achei_esse = random.choice(mochila_de_pokemons)

    # Enviamos o dicionário completo para o template
    return render_template('achei.html', personagem_sorteado=achei_esse)



if __name__ == '__main__':
    app.run(debug=True)
