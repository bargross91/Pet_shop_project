from flask import Flask
from flask import render_template
from flask import redirect , url_for

from cart import get_cart, save_cart, get_cart_total
from pets import get_pets, find_pet



app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/pets/")
def pets():
	pets = get_pets()
	return render_template('pets.html', pets=pets)


@app.route("/pets/<int:pet_id>")
def pet(pet_id):
	pet = find_pet(pet_id)
	return render_template('pet.html', pet=pet)

@app.route("/cart/")
def cart():
	cart = get_cart() 
	total = get_cart_total(cart)
	return render_template('cart.html', cart=cart, total=total)

@app.route("/cart/add_pet/<int:pet_id>")
def add_pet(pet_id):
	pet = find_pet(pet_id)
	cart = get_cart() 
	cart.append(pet)
	new_cart = {
		"pets_in_cart": cart
	}         
	save_cart(new_cart)
	return redirect(url_for('cart'))

@app.route("/cart/empty")
def empty_cart():
	cart ={"pets_in_cart":[] 
	} 
	save_cart(cart)
	return redirect(url_for('index'))


