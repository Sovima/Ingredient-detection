# Ingredient-detection
Model to identify ingredients from an image


## General plan

- [X] Review most common ingredients and get a visual in R if necessary (Feb 20)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The data from [here](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=ingr_map.pkl) has been uploaded to the R notebook. It can be sorted by the number of occurences in the recipes so I can easily extract the most common ingredients. However, I will explore this dataset more to understand general patterns.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I would like to know how well the top 15 ingredients cover the recipes. That is, how many recipes I can get with only top 15 most common ingredients. 

- [X] Find the images for most common ingredients (Start with small amounts, only look at most common ones)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: might need to filter the current images


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Important links:
* [Fruits and veggies](https://www.kaggle.com/kritikseth/fruit-and-vegetable-image-recognition)
* [Open food facts](https://world.openfoodfacts.org/cgi/search.pl?search_terms=ketchup&search_simple=1&action=process)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For usage see [openfoodfacts git](https://github.com/openfoodfacts/openfoodfacts-python/blob/develop/docs/Usage.md)

- [X] Collect the data for most common ingredient labels. This includes reviewing and cleaning it up.
- [ ] Research the best models and pick the most appropriate one
- [ ] Test amd adjust the parameters
- [ ] The rest (Whenever)
- [ ] Add a good description for the project