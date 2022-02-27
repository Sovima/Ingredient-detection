import openfoodfacts
import numpy

def main(ingredients):
    for ingridient in ingredients:
        search_result = openfoodfacts.products.advanced_search({
            "search_terms": ingridient,
            "sort_by":"unique_scans_n",
            "json" : 1
        })
        if (len(search_result['products']) == 0):
            print("search for ingredient " + ingridient + " returned empty")
            continue
        if ('image_url' not in search_result['products'][0]):
        	i = 0
        	while 'image_url' not in search_result['products'][i]:
        		i += 1
        	ingridient_image = search_result['products'][i]['image_url']
        	print(ingridient_image)
        	continue

        ingridient_image = search_result['products'][0]['image_url']
        print(ingridient_image)
main(['baking soda', 'vanilla', 'butter', 'egg', 'onion', 'sugar', 'oil', 
                       'milk', 'flour', 'pepper', 'brown sugar', 'baking powder',
                       'cheddar','parmesan cheese', 'lemon juice', 'sour cream', 
                       'cinnamon'])