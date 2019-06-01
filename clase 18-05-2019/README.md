# Resumen

## Analisis con variables dependientes
* RLS           -> Post-Doc
* RLM           -> Post-Doc
* Reg log       -> Ad-hoc
* Discriminante   -> Ad-hoc

## Analisis con Variables independientes
* Clúster
* Componentes principales
* correspondencia

# optical scale in R

https://cran.r-project.org/web/packages/optiscale/optiscale.pdf

# Análisis discriminante
Es una técnica estadistica que permite asignar o clasificar nuevos individuos dentro de grupos previamente reconocidos o definidos, en esta técnia tiene que hab er 1 variable dependiente.

Ad-hoc = Sabe de ante-mano las categorias en que está

En el analisis de discriminante se debe de buscar la que mayor discrimina. El objetivo es clasificar la observación a un grupo de acuerdo a unas variables.

Tiene como objetivo fundamental producir una regla o un esquema de clasificación que permita a un investigador predecir la población a la que más probable.

## Clasificación con dos grupos 
Se debe de buscar la maximización a la razón de varibilidad entre los grupos (lo mas homogeneo) y los intragrupos (lo más heterogeneo)

F/W=lambda
lamda es la razón a maximizar.

Se requiere al menos 20 datos para que sea un mejor modelo.

### Ejemplo con python
python LDA.py habitos_1.csv 1 "tipocine"

## Matplot
markers: https://matplotlib.org/api/markers_api.html
colors: https://matplotlib.org/gallery/color/named_colors.html

# Arboles de decisión

## Arboles CHAID
El método Chi-Square Automatic Interaction Detector)
https://github.com/Rambatino/CHAID 
## Arboles CART
Classification and Regression Tree

## Arboles Quest:
Son arboles hechos para resolver problemas que se presentaron en el método CHAID y CART

Quick Unbaised, Efficient Stadistical Tree

