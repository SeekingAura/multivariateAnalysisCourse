[Clase anterior:](/clase&#32;29-03-2019 "Clase 29-03-2019") La clase se presentó algunas definiciones varias y entrada al analisis de datos.

# Tipos de variables
**Cuantitiativa:** son las variables que se pueden cuantificar, dar valor númerico o medir, estas variables se pueden clasificar de 2 formas  
* **Discreta:** Son valores que poseen un rango de valores definidos, estos rangos pueden "clasificar" , como carasteristica principal no permiten valores "intermedios" en el rango", ejemplo.  
    | Valores       |Monedas        |
    |      -        |:-------------:|
    |       1       | 50 |
    | 2             | 100|
    | 3             | 200|
* **Continua:** que puede tomar cualquier valor

**Cualitativa:** Describa una cualidad, la cual puede ser una descripción, clasificación; estas variables para ser tratadas requierne de una representación discreta, donde se le da un valor númerico operable, las operaciones más usadas son conteo, moda, entre otros se clasifican de 3 formas.
* **Ordinal:** Son valores que tienen un orden, donde estas dan un significado con su orden, por ejemplo *0 es peor 5 es mejor*
* **Nominal:** Son variables que no tienen orden, es decir que los datos no tienen significado con su orden, como por ejemplo darle un valor a cada una de las carreras de la universidad
* **Dicotómica:** Cuando se pueden colocar como variables de dos categorias (0 y 1)
# Modelos
## Regresión lineal Simple
Es una técnica estadística utilizada para estudiar la relación entre variables, en un modelo de regresión lineal con una sola variable, se utilizan 2 variable  
**x** → Independiente → Variable de control  
**y** → Dependiente  → Variable de respuesta al valor de la variable independiente  
**Varianza:** la relación que tiene los valores  
**Correlación:** es donde se verifica la relación que tienen las variables, por ejemplo verificar si son directamente proporcionales (correalción positiva) si son indirectamente (correlación negativa)

La regresión lineal simple lo que busca es una linea recta que asocie un par de variables. En la regresión lineal simple existen dos variables una dependiente y una independiente, la dependiente será **y** y la independiente **x**.  
![Ecuacion linea recta](/Images/Ecuacion&#32;linea&#32;recta.png)

b0 -> Intercepto  
b1 -> pendiente

## Modelo Matemático
Modelo de regresión lineal simple  
![Ecuacion linea recta](/Images/Modelo&#32;de&#32;regresion&#32;lineal&#32;simple.png)

Donde el Ei hace referencia al error y es lo que el modelo no puede explicar.  
Ecuación de regresión lineal simple sale de aplicar valor esperado a ambos lados.  
![Ecuacion linea recta](/Images/Ecuación&#32;de&#32;regresión&#32;lineal.png)

Al aplicar un modelo matemático para la muestra de datos siempre hay un error inherente por no tener todos los datos de la población  
![Ecuacion linea recta](/Images/Ecuacion&#32;error&#32;inherente.png)

En todo modelo siempre se debe hacer la prueba de hipotesis para verificar los Beta deben cumplir donde b0 puede ser cero y h1 es diferente de cero  
h0: betai=0
h1: betai!=0

### Coeficiente de Determinación
R^2 Coeficiente de determinación: entre mayor sea, mejor es el modelo, sus valores es 0 a 1

### Prueba e hipotesis
Prueba de hipotesis  
Unilaterial derecha  
h0: u <= k  
h1: u>k  

Unilaterial izquierda 
h0: u >= k  
h1: u < k  

Bilateral  
h0: u = k  
h1: u != k  

El problema planteado es, hallar unos estimadores beta circunflejo sub 0 y beta circunflejo sub 1 tales que la recta que pasa por los puntos (X sub t y Y circunflejo sub t) se ajuste lo mejor posible a los puntos (X sub t y Y sub t). Se denomina error o residuo a la diferencia entre el valor oobservado de la variable endógena y el valor ajustado

**Parametro** Es un valor que es de la población  
**Estimador** es el valor de una muestra que trata de ajustarse al parametro, el estimador para ser bueno debe cumplir:
* **Insesgado** Que sea lo mas objetivo posible, que no esté forzado a que se parezca al parametro, es decir como tomar una muestra de forma aleatoria  
* **Eficiente:**  
* **Consistente**

El objetivo principal de este es buscar la mejor recta que se ajusta mas a los datos (linea de tendencia) y **NO** que los datos se ajusten a la recta

## Supuestos de la regresión
* **Linealidad:** La ecuación de regresión adopta una forma particular. En concreto la variable dependiente es la suma de un conjunto de elementos: el origen de la recta, una combinación lineal de variables independientes o predictoras y dependentes o residuos
* **Independiente:** Los residuos son independientes entre si, es decir, constituyen una variable aleatoria, no dependen las variables entre si
* **Homocedasticidad:** Para cada valor de la variable independiente la varianza de los residuos es constnate, es decir que una variable aleatoria que tomará un valor disitnto cada vez que se ejecute el modelo, siempre se parecerá a la varianza.
* **Normalidad:** Que los varlores se distribuyan ede forma normal, es decir que la recta donde esté pase de cierto modo por la "mitad" de los puntos, no por encima ni por  debajo. Para cada valor de la variable independiente los residuos se distribuyen normalmente con media cero
* **Colinealidad:** No existe una relación exacta entre ninguna de las variables independientes. El incumplimiento de este supeusto da origen a la colinealo multicolinealidad, es decir si los valores salen de uno o del otro pro ejemplo, si una variable x es distnacia en cm y la otra variable x es distancia en metros en esta situación relaemnte se tiene una sola variable (entre las mencionadas). Esto se cumple cuando hay relaciones bajas entre la variable independiente y la dependiente


# Metodo de minimos cuadrados
las operaciones de los errores permite verificar que tan bueno o malo es el modelo
yi-> son los datos
yi circunfleho -> es el estimado, es el modelo que se está buscando

## Los minimos cuadrados
Busca encontrar la curva que mejor se ajuste a una colección de puntos, por lo cual busca minimizar la diferencia que hay entre la curva y todos los puntos, los minimos cuadrados que busca el "error" que hay entre el dato y la curva (o recta), se busca es penalizar el mayor valor. Es una sumatoria de errores

Como lo que se busca el error minimo, para ello se aplica una derivada.
![Ecuacion linea recta](/Images/demostracion&#32;cuadrados.png)

Si en la forma matricial la matriz da su determinante 0 son linealmente dependientes

# Matriz de correlación
La dependencia linea entre dos variables se estudia mediante el coefieciente de relación  
r_jk=S_jk/(S_j*S_k)

covarianza (S_jk), si puede ser negativa, 1- < r_jksi < 1 es cercano a -1 es inversa, si es cercano a 0 no hay relación.

La matriz siempre es simetrica, y su determinante siempre será mayor o igual a cero.
