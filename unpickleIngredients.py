import pickle

filepath = '/Users/sofyamalashchenko/Documents/Sofya/Uni stuff/Waterloo Winter 2022/Ingredient-detection/ingr_map.pkl'

ingredients = open(filepath,'rb')

ingrDict = pickle.load(ingredients)

ingredients.close()

ingrDict.to_csv('/Users/sofyamalashchenko/Documents/Sofya/Uni stuff/Waterloo Winter 2022/Ingredient-detection/ingr_map.csv')
