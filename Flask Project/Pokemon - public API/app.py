from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#GET is an assumed method when not mentioned
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.ok:
            try:
                data = response.json().get("stats")
                spritedata = response.json()["sprites"]['other']['dream_world'].get("front_default")
            except:
                error_string=f'There is no info for {pokemon}'
                return render_template("pokemon.html",error=error_string)
            all_stats = []
            for stat in data:
                stat_dict={
                    'poke_statbase':stat['base_stat'],
                    'poke_stateffort':stat['effort'],
                    'poke_statname':stat['stat']['name'],
                }
                all_stats.append(stat_dict)
            return render_template("pokemon.html",stats=all_stats, sprite=spritedata, pokemon=pokemon.title())
        else:
            error_string="Error passing string"
            return render_template("pokemon.html",error=error_string)
    return render_template("pokemon.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)