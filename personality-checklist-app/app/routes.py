from flask import Blueprint, render_template, request, redirect, url_for
from .forms import PersonalityChecklistForm

app = Blueprint('app', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonalityChecklistForm()
    if form.validate_on_submit():
        # Process the form data and determine the personality type
        user_answers = form.data
        # Logic to crosscheck with the 12 apostles would go here
        results = determine_personality(user_answers)
        return redirect(url_for('app.results', results=results))
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    # You may want to use session or pass more data via query string
    # For now, let's assume you pass a result dict as JSON string (or use Flask session)
    import json
    results = request.args.get('results')
    if results:
        results = json.loads(results)
        return render_template('results.html', **results)
    return render_template('results.html', user_traits=[], apostles=[], best_match=None)


def determine_personality(answers):
    apostles = [
        {"name": "Peter", "traits": ["leadership", "bold", "impulsive"], "description": "Leader of the apostles, bold and outspoken."},
        {"name": "John", "traits": ["thoughtful", "loving", "faithful"], "description": "The beloved disciple, thoughtful and caring."},
        # ...add all 12
    ]
    trait_map = {
        "question1": "leadership",
        "question2": "thoughtful",
        "question3": "community",
        "question4": "sacrifice"
    }
    user_traits = [trait_map[q] for q in trait_map if answers.get(q) == 'yes']
    # Find best match
    best_match = max(apostles, key=lambda a: len(set(user_traits) & set(a['traits'])))
    return {
        "user_traits": user_traits,
        "apostles": apostles,
        "best_match": best_match
    }
    