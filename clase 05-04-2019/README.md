# Modelo de regresion
el modelo de regresión nos permite calcular la función que determina la tendencia del ambiente al caso. El modelo de regresión se compone de las siguientes tres sumatorias:

ygorrito -> Y estimado  
SCT=sum (y_i-Ygorrito)^2 -> Suma de cuadrados Totales  
SCE=sum (y_i-ygorrito)^2 -> Suma de cuadrados del error  
SCR=sum(ygorrito-Ygorrito)^2 -> Suma de cuadrados de la regresión  

SCT= SCR+SCE

Si la recta pasa por todos los puntos el SCE (error) será muy pequeño, el error es lo que el modelo no puede explicar

## Mejor escenario
SCE!=0
SCT=SCR

## Peor escenario
SCE >>> 0
SCT=SCE

k -> Número de variable de independientes
n -> número de datos
Tabla anova para regresión lineal simple

|Fuente variación|Suma de cuadrados|Grados de libertad|CuadradoMedio|F|
|----------------|-----------------|------------------|-------------|-|
|Regresión       | SCR             |k                 |             | |


## Prueba estadistica F

H_0 : beta_i = 0  
H_a : beta_i != 0   
Si beta_i es 0 -> indica que la variable no soporta el modelo  
Esta prueba evalúa si existe o no una regresión lineal entre las variables X y Y . Es decir si exite una relación a nivel global.

La prueba H_0 : beta_i = 0   se hace con la prueba F que es

F = CMR/CME

CMR, CME -> Varianzas

## Prueba t de significancia
Esta prueba busca demostrar que si 'x' y 'y' están relacioandas enotnces el parámetro beta_1 es diferente de cero, las hipótesis para esta prueba son

H_0 : beta_1 = 0  
H_a : beta_1 != 0   

ygorrito=b_0+b_1x_1 -> regresión lineal simple
ygorrito=b_0+b_1x_1+b_2x_2 ... b_nx_n -> regresión lineal multiple

## Estadistico de prueba para t
t= b_1/s_b_1 -> proviene de la distribución T student (hecha para muestras pequeñas)
b_1 -> El valor pendiente o valor que acompaña a x_1
donde

s_b_1= s/(sum((x_i-xmedia)^2))^(1/2)

s=(SCE/(n-2))^(1/2)

Yestimado es reemplazar punto por punto en la función

Error tipico

### Analisis de la varianza
Regresion = Número de variables independientes
Residuos número de variables dependientes


1= R^2 + (SCE/SCT)

R^2=1-(SCE/SCT)