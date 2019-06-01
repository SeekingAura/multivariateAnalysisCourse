# Distancia
## Distancia euclidiana
Otra forma de estudiar la variablidad de las observaciones es el concepto de distancia entre dos puntos. En el caso escalar, la distancia entre un valor de la variable y su medida: 

raizCuadrada((x_i-xBarra)^2)

Tambien conocida como la distnacia euclidiana

## Varianza
La varianza es un promedio de las distancias entre un punto y su medida

S^2=sum(x_1-xBarra)^2/n

## Propiedades de la distancia
1. Dados dos puntos en el espacio de dimensión p su distnacia es un número no negativo, d(x_i, x_j) >= 0
2. d(x_i, x_j)=0 la distnacia entre un elemento y el mismo es cero
3. d(x_i, x_j)=d(x_j, x_i) la distancia es una función simétrica en sus argumentos
4. d(x_i,x_j)<=d(x_i, x_p)+d(x_p, x_j) esta desigualdad se conoce como la desigualdad triangular.

---
*heuristica:* La heuristica es un valor que trata de encontrar "rapidamente" un valor optimo, pero no se garantiza que sea la mejor de todas las soluciones, es decir es un maximo o minimo local.  
*meta-heuristica:* Es una mejora de la herustica el cual trata de asegurar aun más la mejor solución

---

## Distnacia Euclidiana ejemplo
Se tiene los siguientes puntos en metros y kgs
A=(1.80, 80)
B=(1.70, 72)
C=(1.65, 81)


Calcular la distancias entre A y B = [[8.00062498]]
Calcular la distancias entre A y C = [[1.01118742]]

lo anterior era si los datos fueran en metros, ahora miremos is fueran en centimetros

A=(180, 80)
B=(170, 72)
C=(165, 81)


Calcular la distancias entre A y B = [[12.80624847]]
Calcular la distancias entre A y C = [[15.03329638]]

Cuando es en metros la distancia A y C es menor a la de A y B pero en centimetros la distancia de A y C es mayor y A y B es menor esto indica que la distnacia Euclidiana es subceptible a las unidades de medición

Por esa razón se hace una estandarización, la estandarización es el hecho de dividir por la desviación estandar, al hacer la división suprime el efecto que hace las diferentes unidades entre si. La estandarización tambien se conoce como Normalkización

# Vectores propios
La matrix de vectores propios se obtiene por medio del uso de la matriz lambda asi

|X1|X2|X3|
|---|---|---|
|1-lambda|1|-1
|