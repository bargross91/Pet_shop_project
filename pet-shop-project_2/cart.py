import json

def get_cart():
	with open('cart.json') as open_file:
		cart = json.load(open_file)
		return cart['pets_in_cart']
	
def save_cart(data):
	with open('cart.json', 'w') as write_file:
		json.dump(data, write_file)
		

def get_cart_total(cart):
	cart_list = cart
	total = []
	for pet in cart_list:
		pet_cost = pet['pet_price']
		total.append(pet_cost)
	final_total = sum(total)
	if int(sum(total)) == 0:
		final_total = "Your cart is empty."
	return final_total
	





