from flask import Flask, render_template, request
from generate_bot import create_bot_zip
from match_launcher import prepare_match

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    form_data = {
        'bot_name': request.form['bot_name'],
        'car': request.form['car'],
        'difficulty': request.form['difficulty'],
        'rank': request.form['rank'],
        'mode': request.form['mode'],
        'arena': request.form['arena'],
        'mutators': request.form['mutators'],
        'skills': request.form.getlist('skills')  # récupère les compétences cochées
    }

    create_bot_zip(form_data)
    prepare_match(form_data)

    return f"✅ Bot généré avec succès ! Match prêt à être lancé avec <b>{form_data['bot_name']}</b>."

if __name__ == '__main__':
    app.run(debug=True, port=5000)

