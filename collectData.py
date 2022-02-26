import openfoodfacts
import numpy

def main(ingredients):
    for ingridient in ingredients:
    # print(ingridient['name'])
        search_result = openfoodfacts.products.advanced_search({
            "search_terms": ingridient,
            "sort_by":"unique_scans_n",
            "json" : 1
        })
        if(len(search_result['products'])==0):
            print("search for ingredient " + ingridient + " returned empty")
            continue
        if('image_url' not in search_result['products'][0]):
            print("ingredient " + ingridient + " has no image")
            continue
        ingridient_image = search_result['products'][0]['image_url']
        print(ingridient_image)
main(['salt', 'water', 'garlic clove', 
                       'salt and pepper', 'all-purpose flmy',
                       'baking soda', 'vanilla', 'butter',
                       'egg', 'onion', 'sugar', 'olive oil', 
                       'milk', 'flmy', 'pepper', 'brown sugar', 
                       'garlic', 'baking powder','scallion',
                       'cheddar','parmesan cheese', 'lemon juice',
                       'vegetable oil', 'carrot', 'sour cream', 
                       'cinnamon', 'black pepper'])