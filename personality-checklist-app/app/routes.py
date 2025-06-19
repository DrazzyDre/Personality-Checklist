from flask import Blueprint, render_template, request, redirect, url_for
from .forms import PersonalityForm

app = Blueprint('app', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonalityForm()
    if form.validate_on_submit():
        # Process the form data and determine the personality type
        user_answers = form.data
        # Logic to crosscheck with the 12 apostles would go here
        results = determine_personality(user_answers)
        return redirect(url_for('app.results', results=results))
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    results = request.args.get('results')
    return render_template('results.html', results=results)

def determine_personality(answers):
    # Placeholder for logic to determine personality based on answers
    # This function should return a result that corresponds to the apostles
    return "Your personality matches with Apostle X"  # Example result