from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import MenuItem
from .forms import ContactForm, ReservationForm
#from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/menu')
def menu():
    items = MenuItem.query.all()
    return render_template('menu.html', items=items)

@main_bp.route('/guide')
def guide():
    questions = [
      {
        'question': 'Have you tried our coffee before?',
        'options': [
          {'value':'yes','label':'Yes'}, {'value':'no','label':'No'}
        ]
      },
      {
        'question': 'Do you like your coffee with milk or without?',
        'options': [
          {'value':'milk','label':'With Milk'},
          {'value':'black','label':'Without Milk'}
        ]
      },
      {
        'question': 'Do you prefer a more balanced taste or a sweeter, milky profile?',
        'options': [
          {'value':'balanced','label':'Balanced'},
          {'value':'sweet','label':'Milky & Sweet'}
        ]
      }
    ]
    recommendations = {
      'milk|sweet': 'Latte',
      'milk|balanced': 'Cappuccino',
      'black|balanced': 'Americano',
      'default': 'Espresso'
    }
    return render_template('guide.html', questions=questions,
                           recommendations=recommendations)


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        # … handle the submitted message …
        flash('Your message has been sent!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', contact_form=contact_form)

@main_bp.route('/reserve', methods=['GET', 'POST'])
def reserve():
    contact_form = ContactForm()
    reservation_form = ReservationForm()

    # Only process the reservation form when its submit button is clicked
    if 'submit' in request.form and reservation_form.validate_on_submit():
        # … handle saving reservation …
        flash('Your reservation is confirmed!', 'success')
        return redirect(url_for('main.reserve'))

    return render_template(
        'contact.html',
        contact_form=contact_form,
        reservation_form=reservation_form
    )