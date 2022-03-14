R Notebook
================

## Important links

-   <https://www.soupersage.com/blog/30-most-popular-recipe-ingredients-2019/>
-   <https://flowingdata.com/2018/09/18/cuisine-ingredients/>
-   <https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=ingr_map.pkl> -
    ingredient data (can be sorted by frequency)

``` r
library(stringr)
```

The ingredients map was originally downloaded in the .pkl format and
converted to csv in python. Now, it can be loaded into the R notebook

``` r
ingr_filepath <- '/Users/sofyamalashchenko/Documents/Sofya/Uni\ stuff/Waterloo\ Winter\ 2022/Ingredient-detection/ingr_map.csv'
ingr <- read.csv(ingr_filepath)
head(ingr, 2)
```

    ##   X                                                                   raw_ingr
    ## 1 0 medium heads bibb or red leaf lettuce, washed, dried* and torn into pieces
    ## 2 1                                      mixed baby lettuces and spring greens
    ##   raw_words
    ## 1        13
    ## 2         6
    ##                                                                   processed
    ## 1 medium heads bibb or red leaf lettuce, washed, dried* and torn into piece
    ## 2                                      mixed baby lettuces and spring green
    ##   len_proc replaced count   id
    ## 1       73  lettuce  4507 4308
    ## 2       36  lettuce  4507 4308

The plan is to look at most used ingredients and use those as the
starting point for the data collection process.

All available ingredients:

``` r
head(unique(ingr["replaced"]))
```

    ##                                       replaced
    ## 1                                      lettuce
    ## 43  french vanilla pudding and pie filling mix
    ## 44                      stove top stuffing mix
    ## 46                                cream cheese
    ## 87                                     cheddar
    ## 171                                  radicchio

From here we can easily get the top most used ingredients however I
would like to perform further research on the available recipes.

First, loading the recipe data from the same notebook and adding a
column “NumIngredients” containing the number of ingredients required
for each recipe.

``` r
recipes_filepath <- '/Users/sofyamalashchenko/Documents/Sofya/Uni\ stuff/Waterloo\ Winter\ 2022/Ingredient-detection/PP_recipes.csv'
recipes <- read.csv(recipes_filepath)
head(recipes, 2)
```

    ##       id     i                                                    name_tokens
    ## 1 424415    23 [40480, 37229, 2911, 1019, 249, 6878, 6878, 2839, 1781, 40481]
    ## 2 146223 96900                   [40480, 18376, 7056, 246, 1531, 2032, 40481]
    ##                                                                                                                                         ingredient_tokens
    ## 1                                                                 [[2911, 1019, 249, 6878], [1353], [6953], [15341, 3261], [2056, 857, 643, 1631, 20480]]
    ## 2 [[17918], [25916], [2507, 6444], [8467, 1179], [8780], [6812], [4370, 2653, 18376], [2654, 5581, 34904, 5940], [15341], [10848], [21447, 7869], [6953]]
    ##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              steps_tokens
    ## 1                                                                                                                                                                   [40480, 40482, 21662, 481, 6878, 500, 246, 1614, 1911, 10757, 240, 674, 9933, 8400, 40478, 40482, 1082, 589, 16126, 500, 481, 6878, 2839, 1781, 5024, 240, 488, 13770, 485, 23667, 40478, 40482, 1233, 481, 4165, 562, 481, 5186, 1454, 6878, 7213, 40478, 40482, 669, 481, 4165, 10230, 485, 256, 1178, 2107, 256, 240, 1233, 246, 17764, 562, 7648, 1571, 40478, 40482, 861, 7648, 1571, 240, 25690, 6878, 556, 481, 4438, 17080, 522, 246, 3602, 9082, 40478, 40482, 4103, 597, 240, 522, 1357, 504, 256, 1178, 2107, 256, 562, 609, 485, 282, 1808, 40478, 40481]
    ## 2 [40480, 40482, 729, 2525, 10906, 485, 43, 8393, 40478, 40482, 23667, 17918, 240, 25916, 240, 2507, 6444, 488, 8467, 1179, 40478, 40482, 4846, 6737, 8780, 488, 7087, 862, 40478, 40482, 3336, 666, 481, 2695, 498, 15473, 6847, 40478, 40482, 19007, 7648, 1571, 40478, 40482, 1000, 19093, 544, 15473, 23667, 6812, 240, 18376, 240, 5940, 240, 21298, 488, 6953, 488, 29369, 1073, 3866, 40478, 40482, 8240, 715, 19093, 488, 19007, 6828, 260, 14635, 1571, 1073, 4858, 544, 1233, 488, 2898, 13908, 500, 2732, 2323, 551, 2698, 40478, 40482, 851, 2548, 491, 844, 7858, 40478, 40482, 1892, 666, 19118, 488, 1325, 15405, 556, 6198, 31757, 488, 36672, 21940, 240, 645, 10114, 40478, 40482, 8658, 746, 775, 22519, 40478, 40481]
    ##                                                                                                                                                                       techniques
    ## 1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ## 2 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ##   calorie_level
    ## 1             0
    ## 2             0
    ##                                                           ingredient_ids
    ## 1                                          [389, 7655, 6270, 1527, 3406]
    ## 2 [2683, 4969, 800, 5298, 840, 2499, 6632, 7022, 1511, 3248, 4964, 6270]

First, convert the ingre dient\_ids column into a list format

``` r
recipes$SepIngredients <- apply(recipes, 1, FUN = function(x)
        strtoi(scan(text=substr(x["ingredient_ids"], 2, 
                                    nchar(x["ingredient_ids"])-1), 
                        what='',
                        sep = ',',
                        strip.white = TRUE, 
                        quiet = TRUE)))
# Then count the number of ingredients in each and add it to a new column
recipes$NumIngredients <- apply(recipes, 1, FUN = function(x) length(x$SepIngredients))
head(recipes, 2)
```

    ##       id     i                                                    name_tokens
    ## 1 424415    23 [40480, 37229, 2911, 1019, 249, 6878, 6878, 2839, 1781, 40481]
    ## 2 146223 96900                   [40480, 18376, 7056, 246, 1531, 2032, 40481]
    ##                                                                                                                                         ingredient_tokens
    ## 1                                                                 [[2911, 1019, 249, 6878], [1353], [6953], [15341, 3261], [2056, 857, 643, 1631, 20480]]
    ## 2 [[17918], [25916], [2507, 6444], [8467, 1179], [8780], [6812], [4370, 2653, 18376], [2654, 5581, 34904, 5940], [15341], [10848], [21447, 7869], [6953]]
    ##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              steps_tokens
    ## 1                                                                                                                                                                   [40480, 40482, 21662, 481, 6878, 500, 246, 1614, 1911, 10757, 240, 674, 9933, 8400, 40478, 40482, 1082, 589, 16126, 500, 481, 6878, 2839, 1781, 5024, 240, 488, 13770, 485, 23667, 40478, 40482, 1233, 481, 4165, 562, 481, 5186, 1454, 6878, 7213, 40478, 40482, 669, 481, 4165, 10230, 485, 256, 1178, 2107, 256, 240, 1233, 246, 17764, 562, 7648, 1571, 40478, 40482, 861, 7648, 1571, 240, 25690, 6878, 556, 481, 4438, 17080, 522, 246, 3602, 9082, 40478, 40482, 4103, 597, 240, 522, 1357, 504, 256, 1178, 2107, 256, 562, 609, 485, 282, 1808, 40478, 40481]
    ## 2 [40480, 40482, 729, 2525, 10906, 485, 43, 8393, 40478, 40482, 23667, 17918, 240, 25916, 240, 2507, 6444, 488, 8467, 1179, 40478, 40482, 4846, 6737, 8780, 488, 7087, 862, 40478, 40482, 3336, 666, 481, 2695, 498, 15473, 6847, 40478, 40482, 19007, 7648, 1571, 40478, 40482, 1000, 19093, 544, 15473, 23667, 6812, 240, 18376, 240, 5940, 240, 21298, 488, 6953, 488, 29369, 1073, 3866, 40478, 40482, 8240, 715, 19093, 488, 19007, 6828, 260, 14635, 1571, 1073, 4858, 544, 1233, 488, 2898, 13908, 500, 2732, 2323, 551, 2698, 40478, 40482, 851, 2548, 491, 844, 7858, 40478, 40482, 1892, 666, 19118, 488, 1325, 15405, 556, 6198, 31757, 488, 36672, 21940, 240, 645, 10114, 40478, 40482, 8658, 746, 775, 22519, 40478, 40481]
    ##                                                                                                                                                                       techniques
    ## 1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ## 2 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ##   calorie_level
    ## 1             0
    ## 2             0
    ##                                                           ingredient_ids
    ## 1                                          [389, 7655, 6270, 1527, 3406]
    ## 2 [2683, 4969, 800, 5298, 840, 2499, 6632, 7022, 1511, 3248, 4964, 6270]
    ##                                                         SepIngredients
    ## 1                                          389, 7655, 6270, 1527, 3406
    ## 2 2683, 4969, 800, 5298, 840, 2499, 6632, 7022, 1511, 3248, 4964, 6270
    ##   NumIngredients
    ## 1              5
    ## 2             12

Now, getting the frequency histogram for the number of ingredients.

``` r
hist(recipes$NumIngredients,
     breaks = 20,
     main = "Number of ingredients in a recipe",
     xlab = "Number of ingredients",
     ylab = "Number of recipes")
```

![](InitialResearch_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
boxplot(recipes$NumIngredients,
        ylab = "Number of ingredients",
        main = "The barplot for Number of ingredients")
```

![](InitialResearch_files/figure-gfm/unnamed-chunk-7-1.png)<!-- --> From
the two graphs above we see that most recipes have less than 15
ingredients and 20 ingredients is the max. Looking at the top 15
ingredients we see

``` r
temp <- ingr[!duplicated(ingr$replaced),]
head(temp[order(-temp$count),], 2)
```

    ##         X                        raw_ingr raw_words processed len_proc replaced
    ## 903   902 aunt jane's krazy mixed up salt         6      salt        4     salt
    ## 6658 6657            butter flavor crisco         3    butter        6   butter
    ##      count   id
    ## 903  72848 6270
    ## 6658 48039  840

Investigating what ‘flmy’ is:

``` r
head(ingr[ingr$replaced == "flmy", ])
```

    ##         X            raw_ingr raw_words processed len_proc replaced count   id
    ## 4753 4752 bread machine flour         3      flmy        4     flmy 23078 2683
    ## 4754 4753   gluten-free flour         2      flmy        4     flmy 23078 2683
    ## 4755 4754               flour         1      flmy        4     flmy 23078 2683

Clearly, this stands for flour.

Of the top 15 ingredients, salt and water can be assumed. Also, garlic
clove and garlic can be combined into 1. Removing these ingredients from
the top 15, we get

``` r
# Adjusting the list further, I decided to combine all-purpose flower with flower,
# baking powder and baking soda
commonIngredients <- c('salt', 'water', 'garlic clove', 
                       'salt and pepper', 'all-purpose flmy',
                       'baking soda', 'vanilla')
temp <- ingr[!duplicated(ingr$replaced),]
temp <- temp[!(temp$replaced %in% commonIngredients), ]
head(temp[order(-temp$count),], 15)
```

    ##           X                                                          raw_ingr
    ## 6658   6657                                              butter flavor crisco
    ## 10969 10968                                                              eggs
    ## 10568 10567                                                     durkee onions
    ## 11019 11018                                                             sugar
    ## 541     540                         goat cheese packed in olive oil and basil
    ## 6066   6065                                                   2% low-fat milk
    ## 4753   4752                                               bread machine flour
    ## 11017 11016                                                            pepper
    ## 9153   9152                                                       brown sugar
    ## 10985 10984                                                            garlic
    ## 3381   3380                                         gluten free baking powder
    ## 2460   2459                                               green onion dip mix
    ## 87       86 kraft shredded triple cheddar cheese with a touch of philadelphia
    ## 3288   3287                                        kraft 100% parmesan cheese
    ## 9228   9227                                                       lemon juice
    ##       raw_words                                 processed len_proc
    ## 6658          3                                    butter        6
    ## 10969         1                                       egg        3
    ## 10568         2                                     onion        5
    ## 11019         1                                     sugar        5
    ## 541           8 goat cheese packed in olive oil and basil       41
    ## 6066          3                                      milk        4
    ## 4753          3                                      flmy        4
    ## 11017         1                                    pepper        6
    ## 9153          2                               brown sugar       11
    ## 10985         1                                    garlic        6
    ## 3381          4                             baking powder       13
    ## 2460          4                       green onion dip mix       19
    ## 87           10            shredded triple cheddar cheese       30
    ## 3288          4                           parmesan cheese       15
    ## 9228          2                               lemon juice       11
    ##              replaced count   id
    ## 6658           butter 48039  840
    ## 10969             egg 43350 2499
    ## 10568           onion 42631 5010
    ## 11019           sugar 37464 6906
    ## 541         olive oil 34402 5006
    ## 6066             milk 24114 4717
    ## 4753             flmy 23078 2683
    ## 11017          pepper 20027 5319
    ## 9153      brown sugar 16611  800
    ## 10985          garlic 15393 3184
    ## 3381    baking powder 15261  332
    ## 2460         scallion 14377 6335
    ## 87            cheddar 13304 1168
    ## 3288  parmesan cheese 13005 5180
    ## 9228      lemon juice 12097 4253

Based on this, I will select the top 20 ingredients that are not in the
commonIngredients list. Now, we will see how many recipes are covered
with the top 20 ingredients and ingredients from the commonIngredients
list see
<https://www.rdocumentation.org/packages/prob/versions/1.0-1/topics/setdiff>
My strategy for that is to go over all recipes, removing the ingredients
that are in the commonIngredients list from each recipe.

``` r
commonIngredients <- c('salt', 'water', 'garlic clove', 
                       'salt and pepper', 'all-purpose flmy',
                       'baking soda', 'vanilla', 'butter',
                       'egg', 'onion', 'sugar', 'olive oil', 
                       'milk', 'flmy', 'pepper', 'brown sugar', 
                       'garlic', 'baking powder','scallion',
                       'cheddar','parmesan cheese', 'lemon juice',
                       'vegetable oil', 'carrot', 'sour cream', 
                       'cinnamon', 'black pepper')

commonIngredientsNum <-  apply(ingr, 1, FUN = function(x) if (x["replaced"] 
                                                                 %in% commonIngredients)
                                                                 {x["id"]})
commonIngredientsNum <- strtoi(unique(commonIngredientsNum))[2:28]
commonIngredientsNum
```

    ##  [1] 1168 5006 6270 6654 6335 5180  332   63 7449 2683 6276 4717  840 1093 3203
    ## [16] 7557  335  800  590 4253 5010 7655 2499 3184 5319 6906 1511

Now, for each recipe we determine the ingredients that are not in the
common Ingredients list. We will also count them to know how well we can
cover the recipes with the top 20 ingredients

``` r
recipes$RemainingIngr <- apply(recipes, 1, FUN = function(x)
        setdiff(x$SepIngredients, commonIngredientsNum))
recipes$RemainingIngrNum <- apply(recipes, 1, FUN = function(x)
        length(x$RemainingIngr))
head(recipes, 2)
```

    ##       id     i                                                    name_tokens
    ## 1 424415    23 [40480, 37229, 2911, 1019, 249, 6878, 6878, 2839, 1781, 40481]
    ## 2 146223 96900                   [40480, 18376, 7056, 246, 1531, 2032, 40481]
    ##                                                                                                                                         ingredient_tokens
    ## 1                                                                 [[2911, 1019, 249, 6878], [1353], [6953], [15341, 3261], [2056, 857, 643, 1631, 20480]]
    ## 2 [[17918], [25916], [2507, 6444], [8467, 1179], [8780], [6812], [4370, 2653, 18376], [2654, 5581, 34904, 5940], [15341], [10848], [21447, 7869], [6953]]
    ##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              steps_tokens
    ## 1                                                                                                                                                                   [40480, 40482, 21662, 481, 6878, 500, 246, 1614, 1911, 10757, 240, 674, 9933, 8400, 40478, 40482, 1082, 589, 16126, 500, 481, 6878, 2839, 1781, 5024, 240, 488, 13770, 485, 23667, 40478, 40482, 1233, 481, 4165, 562, 481, 5186, 1454, 6878, 7213, 40478, 40482, 669, 481, 4165, 10230, 485, 256, 1178, 2107, 256, 240, 1233, 246, 17764, 562, 7648, 1571, 40478, 40482, 861, 7648, 1571, 240, 25690, 6878, 556, 481, 4438, 17080, 522, 246, 3602, 9082, 40478, 40482, 4103, 597, 240, 522, 1357, 504, 256, 1178, 2107, 256, 562, 609, 485, 282, 1808, 40478, 40481]
    ## 2 [40480, 40482, 729, 2525, 10906, 485, 43, 8393, 40478, 40482, 23667, 17918, 240, 25916, 240, 2507, 6444, 488, 8467, 1179, 40478, 40482, 4846, 6737, 8780, 488, 7087, 862, 40478, 40482, 3336, 666, 481, 2695, 498, 15473, 6847, 40478, 40482, 19007, 7648, 1571, 40478, 40482, 1000, 19093, 544, 15473, 23667, 6812, 240, 18376, 240, 5940, 240, 21298, 488, 6953, 488, 29369, 1073, 3866, 40478, 40482, 8240, 715, 19093, 488, 19007, 6828, 260, 14635, 1571, 1073, 4858, 544, 1233, 488, 2898, 13908, 500, 2732, 2323, 551, 2698, 40478, 40482, 851, 2548, 491, 844, 7858, 40478, 40482, 1892, 666, 19118, 488, 1325, 15405, 556, 6198, 31757, 488, 36672, 21940, 240, 645, 10114, 40478, 40482, 8658, 746, 775, 22519, 40478, 40481]
    ##                                                                                                                                                                       techniques
    ## 1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ## 2 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ##   calorie_level
    ## 1             0
    ## 2             0
    ##                                                           ingredient_ids
    ## 1                                          [389, 7655, 6270, 1527, 3406]
    ## 2 [2683, 4969, 800, 5298, 840, 2499, 6632, 7022, 1511, 3248, 4964, 6270]
    ##                                                         SepIngredients
    ## 1                                          389, 7655, 6270, 1527, 3406
    ## 2 2683, 4969, 800, 5298, 840, 2499, 6632, 7022, 1511, 3248, 4964, 6270
    ##   NumIngredients                      RemainingIngr RemainingIngrNum
    ## 1              5                    389, 1527, 3406                3
    ## 2             12 4969, 5298, 6632, 7022, 3248, 4964                6

The results:

``` r
hist(recipes$RemainingIngrNum,
     breaks = 20,
     main = "Remaining number of ingredients in a recipe",
     xlab = "Remaining number of ingredients",
     ylab = "Number of recipes")
```

![](InitialResearch_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

``` r
boxplot(recipes$RemainingIngrNum,
        ylab = "Number of ingredients",
        main = "The barplot for remaining number of ingredients")
```

![](InitialResearch_files/figure-gfm/unnamed-chunk-14-1.png)<!-- --> We
will now collect the images for the above mentioned ingredients. Note
multiple datasets will be used since I couldn’t find one that contained
all necessary ingredients.

``` r
commonIngredients
```

    ##  [1] "salt"             "water"            "garlic clove"     "salt and pepper" 
    ##  [5] "all-purpose flmy" "baking soda"      "vanilla"          "butter"          
    ##  [9] "egg"              "onion"            "sugar"            "olive oil"       
    ## [13] "milk"             "flmy"             "pepper"           "brown sugar"     
    ## [17] "garlic"           "baking powder"    "scallion"         "cheddar"         
    ## [21] "parmesan cheese"  "lemon juice"      "vegetable oil"    "carrot"          
    ## [25] "sour cream"       "cinnamon"         "black pepper"

``` r
assumed <- 'Assume everyone has it'
kaggleFruitsVeg <- "https://www.kaggle.com/kritikseth/fruit-and-vegetable-image-recognition"
source <- c(assumed, assumed, assumed, kaggleFruitsVeg, kaggleFruitsVeg, 
            kaggleFruitsVeg, assumed, kaggleFruitsVeg, kaggleFruitsVeg, kaggleFruitsVeg,
            assumed)
```
