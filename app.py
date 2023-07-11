from flask import Flask, redirect, render_template, flash
from model import db, connect_db, Pet 
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm, EditPet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adoption"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

app.config['SECRET_KEY'] = 'Naruto7'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config["SECRET_KEY"] = 'NARUTO7'
debug = DebugToolbarExtension(app)
ctx = app.app_context()
ctx.push()




@app.route("/")
def petlist():
    pets = Pet.query.all()
    return render_template("pets.html", pets = pets)


@app.route('/addpet', methods = (["GET", "POST"]))
def add():
    form = PetForm()
    species_type = db.session.query(Pet.species.distinct())
    form.species.choices = [(species, species) for species, in species_type]
    if form.validate_on_submit():
        name = form.name.data 
        photo = form.photo_url.data
        age = form.age.data  
        notes = form.notes.data
        available = form.not_available.data

        new_pet = Pet(name=name, photo_url = photo, age = age, notes = notes, available = available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("addpet.html", form=form)



@app.route("/details/<int:pet_id>")
def details(pet_id):
    pets = Pet.query.get_or_404(pet_id)
    return render_template("details.html", pets = pets)



@app.route("/edit/<int:pet_id>", methods = (["GET", "POST"]))
def edit(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form2 = EditPet(obj=pet)
    if form2.validate_on_submit():
        pet.photo_url = form2.photo_url.data
        pet.notes = form2.notes.data
        pet.available = form2.not_available.data
     
        db.session.commit()
        return redirect(f'/details/{ pet.id }')
    else:
        return render_template("edit.html", form2 = form2, pet = pet)


@app.route("/delete/<int:pet_id>", methods= ["POST"])
def delete(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect("/")






