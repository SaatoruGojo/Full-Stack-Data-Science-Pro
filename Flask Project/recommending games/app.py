from flask import Flask, render_template, request

app = Flask(__name__)

games = {
    1: {'title': 'PUBG', 'category': 'Action'},
    2: {'title': 'Minecraft', 'category': 'Adventure'},
    3: {'title': 'Call Of Duty', 'category': 'Action'},
    4: {'title': 'Clash of Clans', 'category': 'Strategy'},
    5: {'title': 'GTA 5', 'category': 'Adventure'},
}

def recommend_games(preferred_category):
    recommendations = []
    for game_id, game in games.items():
        if game['category'] == preferred_category:
            recommendations.append({'title': game['title'], 'category': game['category']})
    return recommendations

@app.route('/')
def home():
    return render_template('game_preferences.html')

@app.route('/select-preferences', methods=['GET', 'POST'])
def select_preferences():
    if request.method == 'POST':
        preferred_category = request.form.get('category')
        recommendations = recommend_games(preferred_category)
        if recommendations:
            return render_template('game_recommendations.html', recommendations=recommendations)
        else:
            return render_template('no_game_recommendations.html', category=preferred_category)
    return render_template('game_preferences.html')

if __name__ == '__main__':
    app.run(debug=True)
