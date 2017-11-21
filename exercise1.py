"""
Here are two dictionaries with sample data.
Follow directions to complete the exercise
"""
cat = {'species': 'cat', 'name': 'Fred', 'color': 'black and white', 'fur': 'long', 'personality': 'very affectionate', 'size': 'gigantic', 'age': 16, 'interests': 'belly rubs'}
cat2 = {'species': 'cat', 'name': 'Maurice', 'color': 'black and white', 'fur': 'short', 'personality': 'timid', 'size': 'normal', 'age': 8, 'interests': 'food'}

# Examples
cat2_name = cat2['name']

print(f"One of my cats is named {cat2_name}")
#  I don't actually need to create a variable just to store these values.
print(f"{cat2_name} has {cat2['fur']} {cat2['color']} fur.")

# Replace the empty string with the necessary code to assign cat's name (from the dictionary) to the variable
cat_name = cat['name']

# Fill in the brackets in the formatted string so the string is correct. Make sure you use the values from the dictionary.
# If you fill it in right, the story of Fred will make sense
# I hope you like cats.
# If you don't want to hear about cats, write me a better story and I'll use it for the next example

the_story_of_fred = f"""{cat_name} is a {cat["personality"]} {cat["species"]}.
He was found as a stray {cat["age"]} years ago in a pothole on a busy street in Philadelphia.
{cat_name} ate a lot, and soon grew to be {cat["size"]}.
He has {cat["fur"]} {cat["color"]} fur and loves {cat["interests"]}
"""

# If you've done this exercise correctly, you'll hear about one of my cats
print(the_story_of_fred)