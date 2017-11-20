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

the_story_of_fred = f"""{"__INSERT NAME HERE__"} is a {"__INSERT PERSONALITY HERE__"} {"__INSERT SPECIES HERE__"}.
He was found as a stray {"__INSERT AGE HERE__"} years ago in a pothole on a busy street in Philadelphia.
{"__INSERT NAME HERE__"} ate a lot, and soon grew to be {"__INSERT SIZE HERE__"}.
He has {"__INSERT FUR LENGTH HERE__"} {"__INSERT COLOR HERE__"} fur and loves {"__INSERT INTERESTS HERE__"}
"""

# If you've done this exercise correctly, you'll hear about one of my cats
print(the_story_of_fred)