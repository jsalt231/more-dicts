"""
I've created a dictionary with sample information

The first level keys are the numbers 1-100
The value associated with each of these first level keys is a dictionary with mathematical operations applied to that number
"""

# DO NOT MODIFY THE LINE BELOW
# This is called a dictionary comprehension. It lets me create a dictionary in one line.
numbers = {x: {'doubled': x*2, 'tripled': x*3, 'squared': x**2, 'cubed': x**3} for x in range(100)}

# The nested for loop below will print out the entire list. This will help you see what the data looks like
for k, v in numbers.items():
    print(f"{k}:")
    for key, value in numbers[k].items():
        print(f"... {key}: {value}")

# Fill in the assignment statements to pull values from the dictionary
# To refer to a key in the second level dictionary, put it in square brackets after hthe first level key you want
# The first one is filled in for you

squared_10 = numbers[10]['squared']

cubed_75 = numbers[75]['cubed']
doubled_7 = numbers[7]['doubled']
tripled_89 = numbers[89]['tripled']
squared_42 = numbers[42]['squared']
cubed_97 = numbers[97]['cubed']

# DO NOT EDIT BELOW THIS LINE

if cubed_75 == 75 ** 3:
    print("first answer correct")
else:
    print(f"first answer wrong. You had {cubed_75}")

if doubled_7 == 7 * 2:
    print("second answer correct")
else:
    print(f"second answer wrong. You had {doubled_7}")

if tripled_89 == 89 * 3:
    print("third answer correct")
else:
    print(f"third answer wrong. You had {tripled_89}")

if squared_42 == 42 ** 2:
    print("fourth answer correct")
else:
    print(f"fourth answer wrong. You had {squared_42}")

if cubed_97 == 97 ** 3:
    print("fifth answer correct")
else:
    print(f"fifth answer wrong. You had {cubed_97}")