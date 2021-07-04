from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class PetForm(FlaskForm):
    """form for adding pets"""

    name = StringField('Pet Name', validators=[InputRequired(message="Pet name required")])
    species = SelectField('Species', choices =[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])

class EditPetForm(FlaskForm):
    """form for editing pets"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")

