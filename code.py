def funcion1(data):
    ordenados = data.sort_values('retweetCount', ascending=False)
    return ordenados.head(10)


import pandas as pd

data = pd.read_json("data.json", lines=True)

func1 = funcion1(data)