Calculo del cociente de posibilidades

odds_1 = P(y=1|x_1=1,x_2=1) / (1-P(y=1|x_1=1,x_2))

odds_1= Calcular la probabilidad de que sea con 1
odds_0 = calcular la probabilidad de que sea con 0

esto anteiror con la formula de 

E(y)=epsilon^(beta_0+beta_1\*x_1+beta_2\*x_2+ ... + beta_p\*x_p) / (1+epsilon^(beta_0+beta_1\*x_1+beta_2\*x_2+ ... + beta_p\*x_p))

el coeficiente se calcula finalmente

odds_1/odds_0

El resultado indica la cantidad de veces que sea probable lo que se está verificando

# Análisis factorial

Todas las técnicas en la estadistica tratan de minimizar la varianza, la varianza e sla distancia que tienen entre si las variables.

Para poder realizar este analisis requeire que las variables tengan mucha relación

## Factor principal
El análisis Factorial (método factor principal) sipone que existe un factor común subyacente a las variables. Este método busca factores que expliquen...

El análisis factorial y el análisis de componentes principales están relacionados entre sí, pero existen varias diferencias:

# Componentes principales
La diferencia entre el análisis de componentes principales y el análisis factorial radica que en el primero se obtienen variables sintéticas combianción de las originales cuyo cálculo es posible gracias a aspectos matemáticos, mientras.


Valor propio: son los valores de un sistema lineal que está relacionado a la ecucación, por ejemplo si se tiene una matriz de 3x3 requeire que tenga 3 vectores.

# Calculo de los vectores propios
|A-lambda*I|

A = es una matriz
lamba = vector de valores propios
I = matriz inversa

|A-lambda*I| = 0 indica que hay una dependencia lineal por lo cual no hay valores propios. Una matriz tiene h <= n valores propios distintos.


https://docs.scipy.org/doc/numpy/user/quickstart.html
https://codeday.me/es/qa/20190220/218982.html