# features 1 = si y 0 = no
# tiene el pelo largo?
# tiene las uñas afiladas?
# hace miau?

perro1 = [0, 1, 1]
perro2 = [1, 0, 1]
perro3 = [1, 1, 1]

gato1 = [0, 1, 0]
gato2 = [0, 1, 1]
gato3 = [1, 1, 0]

datos = [perro1, perro2, perro3, gato1, gato2, gato3]
clases = [1, 1, 1, 0, 0, 0]

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(datos, clases)

animal_misterioso = [1, 1, 1]
model.predict([animal_misterioso])

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

x_train = [misterio1, misterio2, misterio3]
y_train = [0, 1, 1]

model.predict(x_train)

previsiones = model.predict(x_train)
correctos = (previsiones == y_train).sum()
total = len(x_train)
tasa_de_acierto = correctos / total

print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

from sklearn.metrics import accuracy_score

tasa_de_acierto = accuracy_score(y_train, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

import pandas as pd

url = "https://gist.githubusercontent.com/ahcamachod/38673f75b54ec62ffc290eff8e7c716e/raw/6eaa07e199d9f668bf94a034cb84dac58c82fa4f/tracking.csv"
datos = pd.read_csv(url)
print(datos.sample(5))

mapa = {
    "home": "principal",
    "how_it_works": "como_funciona",
    "contact": "contacto",
    "bought": "compro",
}
datos = datos.rename(columns=mapa)
print(datos.sample(3))

x = datos[["principal", "como_funciona", "contacto"]]
print(x.head())

y = datos.compro
print(y.head())

datos.shape

x_train = x[:75]
y_train = y[:75]
x_test = x[75:]
y_test = y[:75]

print(
    f"Entrenaremos con {len(x_train)} elementos y probaremos con {len(x_test)} elementos"
)

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

model = LinearSVC()
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

from sklearn.model_selection import train_test_split

SEED = 42
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=SEED
)

SEED = 42
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=SEED, stratify=y
)

model = LinearSVC()
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

url = "https://gist.githubusercontent.com/ahcamachod/7c55640f0d65bcbd31bb986bb599180c/raw/1b616e97a8719b3ff245fcdd68eaebdb8da38082/projects.csv"
datos = pd.read_csv(url)
print(datos.head())

mapa = {
    "unfinished": "no_finalizado",
    "expected_hours": "horas_esperadas",
    "price": "precio",
}
datos = datos.rename(columns=mapa)
datos.sample(3)

cambio = {1: 0, 0: 1}
datos["finalizado"] = datos.no_finalizado.map(cambio)

import seaborn as sns

sns.scatterplot(x="horas_esperadas", y="precio", hue="finalizado", data=datos)

sns.relplot(
    x="horas_esperadas", y="precio", hue="finalizado", data=datos, col="finalizado"
)

x = datos[["horas_esperadas", "precio"]]
y = datos.finalizado

import numpy as np

SEED = 42
np.random.seed(SEED)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y)

model = LinearSVC()
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

base_previsiones = np.ones(540)
tasa_de_acierto = accuracy_score(y_test, base_previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

print(sns.scatterplot(x="horas_esperadas", y="precio", hue=y_test, data=x_test))

x_min = x_test.horas_esperadas.min()
x_max = x_test.horas_esperadas.max()
y_min = x_test.precio.min()
y_max = x_test.precio.max()

pixels = 100
eje_x = np.arange(x_min, x_max, (x_max - x_min) / pixels)
eje_y = np.arange(y_min, y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(eje_x, eje_y)
puntos = np.c_(xx.ravel(), yy.ravel())
print(puntos)

z = model.predict(puntos)
z = z.reshape(xx.shape)
print(z)

import matplotlib.pyplot as plt

plt.contourf(xx, yy, z, alpha=0.3)
plt.scatter(x_test.horas_esperadas, x_test.precio, c=y_test, s=1)

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

x = datos[["horas_esperadas", "precio"]]
y = datos.finalizado

SEED = 42
np.random.seed(SEED)

raw_x_train, raw_x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, stratify=y
)

scaler = StandardScaler()
scaler.fit(raw_x_train)
x_train = scaler.transform(raw_x_train)
x_test = scaler.transform(raw_x_test)

model = SVC()
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

data_x = x_test[:, 0]
data_y = x_test[:, 1]

x_min = data_x.horas_esperadas.min()
x_max = data_x.horas_esperadas.max()
y_min = data_y.precio.min()
y_max = data_y.max()

pixels = 100
eje_x = np.arange(x_min, x_max, (x_max - x_min) / pixels)
eje_y = np.arange(y_min, y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(eje_x, eje_y)
puntos = np.c_(xx.ravel(), yy.ravel())
print(puntos)

z = model.predict(puntos)
z = z.reshape(xx.shape)

plt.contourf(xx, yy, z, alpha=0.3)
plt.scatter(data_x, data_y, c=y_test, s=1)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

url = "https://gist.githubusercontent.com/ahcamachod/1595316a6b37bf39baac355b081d9c3b/raw/98bc94de744764cef0e67922ddfac2a226ad6a6f/car_prices.csv"
datos = pd.read_csv(url)
print(datos.head(5))

mapa = {
    "mileage_per_year": "millas_por_ano",
    "model_year": "ano_del_modelo",
    "price": "precio",
    "sold": "vendido",
}
datos = datos.rename(columns=mapa)
datos.sample(3)

cambio = {"no": 0, "yes": 1}
datos.vendido = datos.vendido.map(cambio)
datos.sample(3)

from datetime import datetime

ano_actual = datetime.today().year
datos["edad_de_modelo"] = ano_actual - datos.ano_del_modelo
datos.sample(3)

datos["km_por_ano"] = datos.millas_por_ano * 1.60934
datos.sample(3)

datos = datos.drop(columns=["Unnamed: 0", "millas_por_ano", "ano_del_modelo"], axis=1)
datos.sample(3)

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

x = datos[["edad_del_modelo", "km_por_ano", "precio"]]
y = datos.vendido

SEED = 42
np.random.seed(SEED)

raw_x_train, raw_x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, stratify=y
)
print(
    f"Entrenaremos con {len(raw_x_train)} elementos y probaremos con {len(raw_x_test)} elementos."
)

scaler = StandardScaler()
scaler.fit(raw_x_train)
x_train = scaler.transform(raw_x_train)
x_test = scaler.transform(raw_x_test)

model = SVC()
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

from sklearn.dummy import DummyClassifier

dummy = DummyClassifier(strategy="stratified")
dummy.fit(x_train, y_train)
exactitud = dummy.score(x_test, y_test) * 100
print(f"La exactitud del clasificador Dummy stratified fue: {round(exactitud,2)}")

from sklearn.tree import DecisionTreeClassifier

x = datos[["edad_del_modelo", "km_por_ano", "precio"]]
y = datos.vendido

SEED = 42
np.random.seed(SEED)

raw_x_train, raw_x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, stratify=y
)
print(
    f"Entrenaremos con {len(raw_x_train)} elementos y probaremos con {len(raw_x_test)} elementos."
)

scaler = StandardScaler()
scaler.fit(raw_x_train)
x_train = scaler.transform(raw_x_train)
x_test = scaler.transform(raw_x_test)

model = DecisionTreeClassifier(max_depth=3)
model.fit(x_train, y_train)
previsiones = model.predict(x_test)

tasa_de_acierto = accuracy_score(y_test, previsiones)
print(f"La tasa de acierto fue de: {round(tasa_de_acierto*100,2)}%")

from sklearn.tree import export_graphviz
import graphviz

features = x.columns
dot_data = export_graphviz(model, feature_names=features)
grafico = graphviz.Source(dot_data)
print(grafico)
