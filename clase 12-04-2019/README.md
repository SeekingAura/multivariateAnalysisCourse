
# Revisar
Regresion Logistica Binaria
https://becominghuman.ai/machine-learning-using-logistic-regression-in-python-with-code-ab3c7f5f3bed

# Regresión logistica
## Introducción
En sesiones anteriores hablamos de la regresión lineal simple y multiple que son técnica que se usan cuando la variable dpeendiente es cuantitativa, pero ¿Qué pasa cuando la variable dependiente es binaria o puede tomar un valor de 0 o 1?

En muchas de las aplicaciones de la regresión la  variable dependiente asume sólo dos varoles discretos. Por ejemplo un banco necesita indicar la probailidad para darle la tarjet de credito a alguien

### Ejemplo
Una empresa v aa ralizar una promoción por correo. Es una cadena nacial de ropa para dama y ha mandado a imprimir 5000 costosos catálogos de venta a cuatro colores y en cada catalogo incluye un cupón de $50 de descuento en la compra de $200 o más, Como el catálogo es costoso, la empresa desea enviarlo *sólo a auqellos clientes que tengan mayor probabilidad de usar el cupón*. Los gerentes consideran que la cantidad gastada anualmente por el cliente en la tienda, así como si posee o no una tarjeta de créditos con marca de la tienda son dos variables que pueden servir para predecir si ese cliente usará el cupón o no.

X_1 → Gasto → Tipo cuantitativa  
X_2 → Si tiene una tarjeta → Tipo cualitativa
* 0 No tarjeta
* 1 tajerta

## Modelo matematico

E(y)=epsilon^(beta_0+beta_1\*x_1+beta_2\*x_2+ ... + beta_p\*x_p) / (1+epsilon^(beta_0+beta_1\*x_1+beta_2\*x_2+ ... + beta_p\*x_p))

El resultaod de la ecucación anteiror es una probabilidad


https://scikit-learn.org/stable/install.html


Caso perdido: es si no tiene algún valor en variable  
https://stackoverflow.com/questions/47045025/how-to-find-beta-values-in-logistic-regression-model-with-sklearn

## Cociencite de posibilidades
Mide el efecto de probabildiad sobre una variable dpeendiente.

Conciente de posibilidades =(odds_1/odds_0)

Por ejemplo, se desea ver la posibilidad de que ocurra un suceso. Cuantas veces más es posible de que ocurra algo con respecto a otra situación.


odds_1 = P(y=1|x_1=1,x_=1)/1-P(y=1|x_1=1,x_2=1)

odds_0 = P(y=1|x_1=1,x_=0)/1-P(y=1|x_1=1,x_2=1) ...

Se calculan las probabilidades en las diferentes circuntancioas dependiendo de lo que se desea verificar

odds_1
P(Y)=0,4095
1-P(Y)=0,5904

odds_1=0,6931

odds_0
P(Y)=0,1877
1-P(Y)=0,8122

odds_0=0,2311

cociente = 2,93 -> indica que es 3 veces más probable que ocurra odds_1 que odds_0