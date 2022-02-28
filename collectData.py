import openfoodfacts
import numpy
import urllib.request as ureq
import os


def main(ingredients):
    for ingredient in ingredients:
        if not (os.path.exists('ingredients/{ingredient}'.format(ingredient = ingredient))):
            os.mkdir('ingredients/{ingredient}'.format(ingredient = ingredient))

        search_result = openfoodfacts.products.advanced_search({
            "search_terms": ingredient,
            "sort_by":"unique_scans_n",
            "page_size" : 1000,
            "json" : 1
            })

        if (len(search_result['products']) == 0):
            print("search for ingredient " + ingredient + " returned empty")
            continue
        l = len(search_result['products'])
        length = min(l, 100)
        curr = 0
        i = 0
        while 1:
            if curr >= length or i >= l:
                print("Add {curr} ingredients: {ingredient}".format(curr = curr, ingredient = ingredient))
                print("i = {i}, l = {l} \n".format(i = i, l = l))
                break
            if ('image_url' not in search_result['products'][i]):
                i += 1
                continue
            else:
                ingredient_image = search_result['products'][i]['image_url']
                ureq.urlretrieve(ingredient_image, 
                    'ingredients/{ingredient}/image{j}.jpg'.format(ingredient = ingredient, 
                        j = curr))
                i += 1
                curr += 1

main(['baking soda', 'vanilla', 'butter', 'egg', 'onion', 'sugar', 'oil', 
                       'milk', 'flour', 'pepper', 'brown sugar', 'baking powder',
                       'cheddar','parmesan cheese', 'lemon juice', 'sour cream', 
                       'cinnamon'])

# Use raw sugar instead of sugar
# Baking powder and baking soda are the same thing
# onions are in the vegetables dataset
# try searching for specific oils and put them all into oil
# Try putting vanilla extract instead of vanilla
# Do something different for eggs
# Put sugar and brown sugar into the same category
# Add lemon juice to lemon
# search different types of milk
# Get pepper from veg dataset
# Butter seems to return the most irrelevant data as of now
'''
Finished ingredients:
- Baking Powder and Baking soda - need to combine
- Lemon juice
'''