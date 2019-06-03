import json

def find_pet(pet_id):
	with open("pets.json", "r") as read_file:
		data = json.load(read_file)
	found_pet = {}
	for pet in data:
		if pet["pet_id"] == pet_id:
			found_pet = pet
			break
	return found_pet
 
def get_pets():
	with open("pets.json", "r") as read_file:
		data = json.load(read_file)
	return data



