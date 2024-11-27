import json

# Sample JSON data (you would typically read this from a file)
json_data = '''{
  "recipes": [
    {
      "id": "r001",
      "name": "Spaghetti Bolognese",
      "ingredients": ["Spaghetti", "Ground Beef", "Tomato Sauce", "Onion"],
      "steps": ["Boil spaghetti", "Cook ground beef", "Add sauce", "Mix and serve"],
      "servingSize": 4
    },
    {
      "id": "r002",
      "name": "Chicken Curry",
      "ingredients": ["Chicken", "Curry Powder", "Coconut Milk", "Rice"],
      "steps": ["Cook chicken", "Stir in curry powder", "Add coconut milk", "Simmer and serve"],
      "servingSize": 3
    }
  ]
}'''

# Load JSON data
data = json.loads(json_data)

# Process the JSON data
for recipe in data["recipes"]:
    print(f'--Recipe ID: {recipe["id"]}--')
    print(f'Name: {recipe["name"]}')
    print(f'Ingredients: {", ".join(recipe["ingredients"])}')
    print(f'Steps: {", ".join(recipe["steps"])}')
    print(f'Serving Size: {recipe["servingSize"]}')
    print()  

new_data = {
    "recipes": [
        {
            "id": "r003",
            "name": "Vegetable Stir Fry",
            "ingredients": ["Broccoli", "Carrots", "Bell Pepper", "Soy Sauce"],
            "steps": ["Chop vegetables", "Stir fry in pan", "Add soy sauce", "Serve"],
            "servingSize": 2
        }
    ]
}

# Writing JSON data to a file
with open('recipes.json', 'w') as json_file:
    json.dump(new_data, json_file, indent=4)

print("JSON data written to recipes.json")

# Reading JSON data from a file
with open('recipes.json', 'r') as json_file:
    data_from_file = json.load(json_file)

# Print the loaded data
print(json.dumps(data_from_file, indent=4))