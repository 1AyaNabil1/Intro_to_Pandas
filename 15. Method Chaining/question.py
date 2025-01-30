import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filter_animal = animals[animals['weight']>100]
    sort_animal = filter_animal.sort_values(by='weight', ascending = False)
    names = sort_animal[['name']]
    return names