import json
import urllib.parse
from flask import Blueprint, render_template, request, redirect, url_for
from .forms import PersonalityChecklistForm

app = Blueprint('app', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonalityChecklistForm()
    if form.validate_on_submit():
        user_answers = form.data
        results = determine_personality(user_answers)  # <-- Call your function!
        results_json = urllib.parse.quote(json.dumps(results))  # Safely encode for URL
        return redirect(url_for('app.results', results=results_json))
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    import json, urllib.parse
    results = request.args.get('results')
    if results:
        results = json.loads(urllib.parse.unquote(results))
        return render_template('results.html', **results)
    return render_template('results.html', user_traits=[], apostles=[], best_match=None)


def determine_personality(answers):
    apostles = [
        {"name": "Peter", "traits": ["leadership", "bold", "impulsive"], "description": "Leader of the apostles, bold and outspoken."},
        {"name": "John", "traits": ["thoughtful", "loving", "faithful"], "description": "The beloved disciple, thoughtful and caring."},
        {"name": "James", "traits": ["community", "supportive", "encouraging"], "description": "The supportive disciple, always building community."},
        {"name": "Andrew", "traits": ["curious", "inquisitive", "seeker"], "description": "The first-called disciple, always seeking."},
        {"name": "Philip", "traits": ["analytical", "practical", "realistic"], "description": "The pragmatic disciple, focused on details."},
        {"name": "Bartholomew", "traits": ["honest", "straightforward", "sincere"], "description": "The honest disciple, known for his integrity."},
        {"name": "Matthew", "traits": ["organized", "detail-oriented", "methodical"], "description": "The tax collector, meticulous and precise."},
        {"name": "Thomas", "traits": ["skeptical", "doubting", "questioning"], "description": "The doubter, always seeking proof."},
        {"name": "James the Less", "traits": ["humble", "quiet", "reserved"], "description": "The lesser-known apostle, humble and reserved."},
        {"name": "Thaddeus", "traits": ["loyal", "devoted", "faithful"], "description": "The loyal disciple, devoted to his mission."},
        {"name": "Simon the Zealot", "traits": ["passionate", "zealous", "committed"], "description": "The passionate apostle, committed to his cause."},
        {"name": "Judas Iscariot", "traits": ["betrayer", "complex", "conflicted"], "description": "The betrayer, a complex and conflicted figure."}
        
    ]
    trait_map = {
        "question1": "leadership",
        "question2": "thoughtful",
        "question3": "community",
        "question4": "sacrifice",
        "question5": "wisdom",
        "question6": "action",
        "question7": "helping",
        "question8": "behind_the_scenes",
        "question9": "peacemaker",
        "question10": "justice",
        "question11": "teaching",
        "question12": "prayer",
        "question13": "studying",
        "question14": "serving",
        "question15": "missions",
        "question16": "hospitality",
        "question17": "encouragement",
        "question18": "leadership",
        "question19": "mercy",
        "question20": "giving",
        "question21": "faith"
    }
    user_traits = [trait_map[q] for q in trait_map if answers.get(q) == 'yes']
    
    # Find best match
    best_match = max(apostles, key=lambda a: len(set(user_traits) & set(a['traits'])))
    return {
        "user_traits": user_traits,
        "apostles": apostles,
        "best_match": best_match
    }
    