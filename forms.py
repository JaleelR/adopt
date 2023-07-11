from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import InputRequired, optional, URL, NumberRange, AnyOf


class PetForm(FlaskForm):
    name = StringField("Name", validators=[
        InputRequired(message = "Must enter a name")] )

    species = SelectField("Species", validators=[
        InputRequired(message="Please select a species"), AnyOf(["dog, cat, porcupine"])])

    photo_url = StringField("Image URL", validators=[
        URL(), optional()])

    age = IntegerField("Age", validators=[
        optional(), NumberRange(max=30)])

    notes = StringField("More info about animal?",  validators=[
        optional()])

    not_available = BooleanField("Unvalible for adoption",  validators=[
       optional()])


class EditPet(FlaskForm):

    photo_url = StringField("Image URL", validators=[
        URL(), optional()])

    notes = StringField("More info about animal?",  validators=[
        optional()])

    not_available = BooleanField("Unvalible for adoption",  validators=[
       optional()])