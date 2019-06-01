# Modelo de regresión lineal multiple

y= beta_0 +beta_1*x_1+beta_2*x_2+ ... + beta_p*x_p+epsilon

matricialmente llegará a la formula

y= x*beta + error

La variable dependiente Y se representa como una combinación lineal de un conjunto e k variables x_k, cada una de las cuales va acompaña de un coeficiente b_k, debe tratar que no haya colinealidad

colinealidad = alta correlación entre la variable independiente, es decir que no sean del mismo tipo de variable como hablar en terminos de euros y pesos, ambos son dinero.

## Supuestos del modelo de regresión
* E(epsilon)=0
* La varianza de *epsilon* se denota como *sigma*^2 es la misma para todos los valores de x
* Los valores de epsilon son independientes
* Los errores de *epsilon* siguen una distribución normal


## Ejemplo : RLM
Una compañia de transporte que se dedica a la entrega de mercancía en una ciudad quiere saber si el tiempo de recorrido de un camión depende de las entregas y de las millas recorridas. En una muestra aleatoria de 10 recorridos se obtuvieron los siguientes datos

* Tiempo de recorrido (y) -> variable dependiente
* Entregas x_1
* Distnacia recorrido x_2


# Binario
* X -> Variable independiente
    * 'y' es binaria
    * signma categoria

* y -> Variable binaria
    * como variable dpeendiente

Se tiene una variable 

Regresión logistica binaria nomial y regresión logistica multinomial

```python
from statsmodels.formula.api import ols
model_name = ols('outcome_variable ~ group1 + group2 + groupN', data=your_data).fit()
model_name = ols('outcome_variable ~ C(group_variable)', data=your_data).fit()
```

## johnson ejemplo
reemplezar 

yGorrito= InterceptCoef+MothnsCoef-Type

## Ejemplo footbal
yestimado = coefintercept + coefX1 por Posicion + coefX2 por peso + X3 por tiempo
yestimado = 11.9556 - 0,73224 por Posicion + 0.02222 por Peso - 2.2775 por tiempo

t -> % Significancia

En este modelo se determina que le falta mas potencia (mas variables)

R^2 determina que el 60% estaria en algo que no puede explicar (0.475 para R^2)

Entre mas cerca sea R^2 a 1 será mejor el modelo, entre menor será peor, al quitar variables dependiendo como cambie determina que tanto aportan las variables al modelo

# Revisar
Regresion Logistica Binaria
https://becominghuman.ai/machine-learning-using-logistic-regression-in-python-with-code-ab3c7f5f3bed
