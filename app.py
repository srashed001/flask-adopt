from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)  

default_img = "https://static.wixstatic.com/media/760dfc_84266ca3cce4402290a46a7145e1de57~mv2.jpg/v1/fill/w_340,h_220,al_c,q_80,usm_0.66_1.00_0.01/Pets%20Picture%20Not%20Available.webp"

@app.route('/')
def home_page():
    """renders home page with display of all pets"""
    pets = Pet.query.all()
    return render_template('home_page.html', pets = pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
    """displays add-pet form and adds pet to db
        redirects to home page with successful post"""
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data if form.photo_url.data else default_img, age=form.age.data, notes=form.notes.data)
        db.session.add(pet)
        db.session.commit()
        flash(f'You have added {pet.name}')

        return redirect('/')
    else:
        return render_template('add_pet.html', form = form )

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def display_edit_form(pet_id):
    """displays edit-pet form and edits selected pet info 
        redirects to main page with successful post"""
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data if form.photo_url.data else pet.photo_url
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('display_edit.html', pet = pet, form=form)


