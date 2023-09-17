import pandas as pd

datos = pd.read_csv("credit_card.csv")
print(datos)

print(datos.info())
# 2.
import pandas as pd

datos = pd.read_csv("credit_card.csv")
datos.columns

dic_columnas = {
    "LIMIT_BAL": "limite",
    "CHECKING_ACCOUNT": "cuenta_corriente",
    "EDUCATION": "escolaridad",
    "MARRIAGE": "estado_civil",
    "AGE": "edad",
    "BILL_AMT": "valor_factura",
    "PAY_AMT": "valor_pago",
    "DEFAULT": "moroso",
}

tarjetas = datos.rename(columns=dic_columnas)
print(tarjetas)

cuenta_corriente = tarjetas.cuenta_corriente.unique()
print(cuenta_corriente)

dic_cuenta = {"Yes": "Si", "No": "No"}

tarjetas.cuenta_corriente.map(dic_cuenta)
print(tarjetas)

tarjetas.cuenta_corriente = tarjetas.cuenta_corriente.map(dic_cuenta)
print(tarjetas)

print(tarjetas.escolaridad.unique())
dic_escolaridad = {
    "2.University": "2.Universidad",
    "3.Graduate School": "3.Pos-graduación",
    "1.High School": "1.Colegio",
}

tarjetas.escolarida = tarjetas.escolaridad.map(dic_escolaridad)
print(tarjetas)

dic_estado_civil = {"Married": "Casado/a", "Single": "Soltero/a"}
tarjetas.estado_civil = tarjetas.estado_civil.map(dic_estado_civil)
print(tarjetas)

# 4.importando seaborn y analisis de distribución
import seaborn as sns

sns.displot(data=tarjetas, x="limite", hue="escolaridad")

# 5.Creando variable numerica
tarjetas["iu"] = tarjetas["valor_factura"] / tarjetas["limite"]

print(tarjetas.head())

sns.displot(data=tarjetas, x="iu")

# 6.Parámetros de gráficos
sns.set_style("darkgrid")
sns.displot(data=tarjetas, x="limite", hue="escolaridad")

# 7.Countplot,catplot y swarmplot
sns.countplot(x="cuenta_corriente", data=tarjetas, hue="moroso", palette="coolwarm")

sns.catplot(x="estado_civil", y="limite", data=tarjetas, hue="moroso", dodge=True)
sns.swarmplot(x="escolaridad", y="iu", data=tarjetas)

# 8.Boxplot y violinplot
sns.boxenplot(x="escolaridad", y="iu", data=tarjetas, hue="moroso", palette="bone")

sns.violinplot(x="escolaridad", y="iu", data=tarjetas, hue="moroso")

# 9.Creando y analizando variable categórica
bins = [20, 30, 40, 50, 100]
nombres = ["20-30", "30-40", "40-50", "50+"]
tarjetas["rango_edad"] = pd.cut(tarjetas["edad"], bins, labels=nombres)
sns.boxenplot(x="rango_edad", y="limite", data=tarjetas)

# 10.Displot
sns.displot(data=tarjetas, x="limite", col="escolaridad", kind="kde", hue="moroso")

# 11.Scatterplot y implot
sns.scatterplot(x="iu", y="valor_factura", data=tarjetas, hue="cuenta_corriente")

# 12.Test de hipótesis
sns.scatterplot(x="iu", y="valor_factura", data=tarjetas, col="moroso")

from scipy.stats import ranksums

moroso = tarjetas.query("moroso == 1").valor_factura
print(moroso)

no_moroso = tarjetas.query("moroso == 0").valor_factura
print(no_moroso)

resultado = ranksums(moroso, no_moroso)
print(resultado)

# 13.Jointplot
sns.jointplot(x="edad", y="limite", data=tarjetas)

# 14.Pairplot
print(tarjetas.describe())
print(sns.pairplot(data=tarjetas))
print(sns.pairplot(data=tarjetas, hue="escolarida", palette="cividls"))
