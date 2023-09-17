import pandas as pd

# Consultas en DataFrames
datos = {
    "Nombre": ["jetta variant", "passat", "crossfox"],
    "Motor": ["Motor 4.0 turbo", "Motor Diesel"],
    "Año": [65132, 6565, 5565],
    "Valor": [5565, 6566, 5133],
}

dataset = pd.DataFrame(datos)
dataset.head()

dataset.query('Motor == "Motor Diesel" and Cero_km == True')
