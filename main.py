from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'
db = SQLAlchemy(app)

class Personagem(db.Model):
    id    = db.Column(db.Integer, primary_key=True) #automatico
    nome  = db.Column(db.String(100), nullable=False)
    cor   = db.Column(db.String(20),  nullable=False)
    hp    = db.Column(db.String(50),  nullable=False)
    genero = db.Column(db.String(1),  nullable=False)
    img   = db.Column(db.String(500), nullable=False)
    atk1  = db.Column(db.String(100), nullable=False)
    dano1 = db.Column(db.String(20),  nullable=False)
    atk2  = db.Column(db.String(100), nullable=False)
    dano2 = db.Column(db.String(20),  nullable=False)
    desc  = db.Column(db.Text,         nullable=False)



@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/novo', methods=['POST'])
def novo():
    novo_personagem = Personagem(
        nome = request.form['nome'],
        cor = request.form['cor'],  # Uma cor padrão para os novos, ou você pode add um campo de cor no form!
        genero = request.form['genero'],
        hp = request.form['hp'],
        img = request.form['url'],
        atk1 = request.form['ataque1'], dano1 = request.form['dano1'],
        atk2 = request.form['ataque2'], dano2 = request.form['dano2'],
        desc = request.form['descricao']
        )

    db.session.add(novo_personagem)
    db.session.commit()

    return render_template('card.html',
                           personagem=novo_personagem,
                           mensagem_sucesso="✨ Carta adicionada à sua coleção com sucesso! ✨"
                           )

@app.route('/colecao')
def colecao():
    lista_personagens = Personagem.query.order_by(Personagem.id).all()

    return render_template('colecao.html', lista_pokemons=lista_personagens)

@app.route('/pikachu')
def pikachu():
    # Mantivemos a rota original fixa do Pikachu como exemplo didático
    personagem_exemplo = Personagem.query.get(1)
    return render_template('card.html', personagem=personagem_exemplo)

@app.route('/achei')
def achei_um_pokemon(): # Tarefa de casa
    # Em vez de uma lista de textos, sorteamos um dicionário inteiro da nossa mochila!
    achei_esse = random.choice(mochila_de_pokemons)

    # Enviamos o dicionário completo para o template
    return render_template('achei.html', personagem_sorteado=achei_esse)

@app.route('/personagem/<int:id>')
def ver_personagem(id):
    meu_personagem = Personagem.query.get(id)
    return render_template('card.html', personagem=meu_personagem)



with app.app_context():
    db.create_all()

    if Personagem.query.count() == 0:
        iniciais = [
            Personagem(nome='Pikachu', cor='#f1c40f', hp='⚡ 70 HP', genero='M',
                    img='https://sm.ign.com/ign_br/screenshot/default/fotojet-2024-03-08t101121308_wexc.jpg',
                    atk1='Choque do Trovao', dano1='90',
                    atk2='Relampago',        dano2='30',
                    desc='Pikachu armazena energia elétrica nas bochechas.'),

            Personagem(nome='Charmander', cor='#e67e22', hp='🔥 60 HP', genero='M',
                    img='https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png',
                    atk1='Arranhao', dano1='40',
                    atk2='Lanca-Chamas', dano2='80',
                    desc='A chama na ponta de sua cauda indica seu humor.'),
        ]

        db.session.add_all(iniciais)
        db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)
