#!/usr/bin/python

import math

ingredientos = {
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}

recipeos = {
  'eggs': 1,
  'butter': 2,
  'sugar': 4,
  'flour': 6
}

def recipe_batches(recipe, ingredients):
  # print(ingredients.items())
  # print(recipe['butter'])
  smallest = None

  for key in recipe:
    if key not in ingredients:
      return 0

    result = ingredients[key] // recipe[key]

    if result == 0:
      return 0

    elif smallest is None or result < smallest:
      smallest = result
  
  return smallest
  


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))



print(recipe_batches(recipeos,ingredientos))