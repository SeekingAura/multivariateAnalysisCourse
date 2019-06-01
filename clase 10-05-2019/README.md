https://towardsdatascience.com/an-introduction-to-clustering-algorithms-in-python-123438574097
# Analisis clúster
* Basado en proximidades, utilizando distancias
    * Entre mas cercanas estén son más homogeneos 
    * entre mas separados estén son mas heterogeneos
* El objetivo es clasificar grupos

Lo que se se busca es buscar al interior de cada grupo es los parecidos entre sí, pero que difieran en otras unidades

## Definición
Esas agrupaciones que se pretenden identificar, deben buscar que en el interior de cada grupo o clasificación existan elementos que sean muy parecidos entre si, y que difieran lo más posible en relación a los elementos de otro grupo; y parte de éstas clasificaciones las podemos encontrar hoy dentro de un conjunto de técnicas que conocemos como análisis cluster.

## Donde se usa
* Segmentación y posicionamiento
* Estudio de perfiles
* Comprotmaiento dle consumidor
* Selección de mercados de prueba
* Detección de problemas
* Desarrollo de nuevos productos

## Principios del análisis clúster
* Su finalidad es revelar concentraciones en los datos para su agrupamiento en clústers según su homogeneidad
* El agrupamiento se puede hacer para casos como para variables y estas pueden ser cualitativas o cuantiativas
* Los grupos de casos o variables se realizan de acuerdo a la proximidad o lejanía, por lo tnato es esencial el uso del concepto de la distancia
* Es fundamental que los elementos dentro de un clúster sean homogéneos y lo más diferente de otros clúster
* El número de clúster no se conocen de antemano y los grupos se crean de acuerdo

## Condiciones del clústers
* Si las variables de aglomeración están en escalas muy diferentes se hace necesario estandarizar las variables
* Es necesario tener en cuenta los valores atípicos por que los métodos jerárquicos se pueden deformar por que las distancias se deforman y producen clúster unitarios.
* Los grupos finales serán tan distintos como permitan los datos   

## Dendograma
La representación gráfica de estas etapas de formación de grupos a modo de árbol invertido, se denomina dendrograma.

## ¿Qué mas busca el cluster?
De acuerdo a las variables que hay en el grupo de datos busca que tanta similitud hay en él conjunto de datos. Es una técnica para clasificar los individuos en categorías, más usado para identificar a que grupo se pertenece los datos

A diferencia del analisis de discriminante en este se conoce la categoria desde antes, así como cuando se lleva el carro al mecanico y empieza a clasificarlo de acuerdo a los sintomas que presenta el auto.


* Vecino mas cercano
* Arbol mas cercano
* Busquedas  

Clusters
* Jerarquico
* 
