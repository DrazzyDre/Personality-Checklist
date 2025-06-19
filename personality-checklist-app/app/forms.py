from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class PersonalityChecklistForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    question1 = RadioField('Do you consider yourself a leader?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    question2 = RadioField('Are you more of a thinker than a doer?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    question3 = RadioField('Do you value community and fellowship?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    question4 = RadioField('Are you willing to sacrifice for others?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')