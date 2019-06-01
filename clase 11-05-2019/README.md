# Rstudio PCA

## Instalando Requerimientos
* install.packages("psych")
* install.packages("GPArotation")

## Incluir Requerimientos
* library(psych)
* library(GPArotation)

## Ejecución
* VariableAGuardar<-principal(dataFrame, nfactors=#, rotate = "none", use=pairwise)
* CProtado<-principal(punto1, nfactors=2, rotate = "varimax")

El # es la cantidad de factores que tiene el dataframe para el analisis

## Punto 1

### Análisis de componentes principales sin rotar con 8 factores 

             PC1   PC2   PC3   PC4   PC5   PC6   PC7   PC8 h2      u2 com
Lengua      0.92 -0.32 -0.06 -0.12  0.05 -0.09  0.11 -0.06  1 2.2e-16 1.3
Matemáticas 0.40  0.89  0.08 -0.04 -0.15  0.12  0.09  0.00  1 1.3e-15 1.6
Física      0.48  0.84  0.04 -0.12  0.18  0.03 -0.10 -0.04  1 1.0e-15 1.8
Inglés      0.91 -0.30 -0.01 -0.26 -0.05  0.00 -0.03  0.08  1 1.4e-15 1.4
Filosofía   0.88 -0.25 -0.26  0.23  0.17  0.09  0.03  0.03  1 2.0e-15 1.6
Historia    0.90 -0.34 -0.04  0.14 -0.20  0.02 -0.10 -0.05  1 1.6e-15 1.5
Química     0.47  0.85 -0.03  0.16 -0.04 -0.15  0.00  0.04  1 1.4e-15 1.7
Ed Física   0.33 -0.19  0.92  0.07  0.05  0.00  0.01  0.01  1 1.4e-15 1.4

                      PC1  PC2  PC3  PC4  PC5  PC6  PC7  PC8
SS loadings           4.0 2.63 0.93 0.20 0.13 0.05 0.04 0.02
Proportion Var        0.5 0.33 0.12 0.03 0.02 0.01 0.01 0.00
Cumulative Var        0.5 0.83 0.95 0.97 0.99 0.99 1.00 1.00
Proportion Explained  0.5 0.33 0.12 0.03 0.02 0.01 0.01 0.00
Cumulative Proportion 0.5 0.83 0.95 0.97 0.99 0.99 1.00 1.00


### Análisis de componentes rotado y con 2 factores

            RC1   RC2   h2    u2 com
Lengua      0.97  0.10 0.96 0.043 1.0
Matemáticas 0.00  0.97 0.95 0.052 1.0
Física      0.08  0.97 0.94 0.059 1.0
Inglés      0.95  0.11 0.92 0.080 1.0
Filosofía   0.91  0.14 0.84 0.159 1.1
Historia    0.96  0.06 0.93 0.071 1.0
Química     0.07  0.97 0.95 0.052 1.0
Ed Física   0.38 -0.04 0.15 0.854 1.0

                       RC1  RC2
SS loadings           3.76 2.87
Proportion Var        0.47 0.36
Cumulative Var        0.47 0.83
Proportion Explained  0.57 0.43
Cumulative Proportion 0.57 1.00


### graficar
factanal(dataframe, factors=2, rotation="varimax", scores="regression")$scores


# Punto 2
## Instalación
* Paquete para cambiar row names : install.packages("tidyverse")
* 

## Compilación
https://rpubs.com/PachoAlvarez/232979
summary(res.ca)
## A
Eigenvalues
                       Dim.1   Dim.2   Dim.3   Dim.4   Dim.5
Variance               0.163   0.036   0.006   0.003   0.000
% of var.             78.476  17.138   3.032   1.236   0.119
Cumulative % of var.  78.476  95.613  98.645  99.881 100.000

Rows
                         Iner*1000    Dim.1    ctr   cos2    Dim.2    ctr   cos2    Dim.3    ctr   cos2  
Ingeniería Sistemas    |    28.000 | -0.231  5.524  0.322 | -0.332 52.355  0.665 |  0.029  2.222  0.005 |
Ingeniería Industrial  |    57.421 | -0.609 33.109  0.940 |  0.119  5.769  0.036 |  0.096 21.322  0.023 |
Ingeniería Comercial   |    13.874 | -0.359  7.228  0.849 |  0.088  1.992  0.051 | -0.092 12.379  0.056 |
Ingeniería Civil       |    17.624 | -0.338  6.763  0.625 |  0.223 13.409  0.271 | -0.117 20.801  0.074 |
Ingeniería Eléctrica   |    26.345 |  0.436 15.160  0.938 |  0.063  1.462  0.020 |  0.075 11.681  0.028 |
Ingeniería Mecánica    |    27.996 |  0.482 14.953  0.870 |  0.154  6.950  0.088 |  0.086 12.174  0.027 |
Ingeniería Física      |    20.046 |  0.353 11.393  0.926 |  0.071  2.111  0.037 | -0.064  9.581  0.030 |
Ingeniería Mecatrónica |    16.366 |  0.289  5.869  0.584 | -0.222 15.951  0.347 | -0.073  9.839  0.038 |

Columns
                         Iner*1000    Dim.1    ctr   cos2    Dim.2    ctr   cos2    Dim.3    ctr   cos2  
Innovador              |    39.200 | -0.452 19.889  0.827 | -0.153 10.385  0.094 |  0.139 48.737  0.078 |
Empresario             |    72.866 | -0.610 36.968  0.827 |  0.271 33.525  0.164 | -0.061  9.672  0.008 |
Investigador           |    36.771 |  0.453 21.669  0.960 |  0.078  2.912  0.028 | -0.009  0.201  0.000 |
Creativo               |    18.782 | -0.026  0.080  0.007 | -0.298 47.573  0.901 | -0.092 25.718  0.086 |
Metódico               |    24.981 |  0.509 13.681  0.893 |  0.118  3.343  0.048 |  0.106 15.337  0.039 |
Analítico              |    15.074 |  0.234  7.713  0.834 |  0.059  2.262  0.053 | -0.010  0.335  0.001 |

# Punto 3
## A
Eigenvalues
                       Dim.1   Dim.2   Dim.3
Variance               0.013   0.000   0.000
% of var.             99.951   0.046   0.003
Cumulative % of var.  99.951  99.997 100.000

Rows
             Iner*1000    Dim.1    ctr   cos2    Dim.2    ctr   cos2    Dim.3    ctr   cos2  
Producto_A |     1.325 | -0.065 10.528  1.000 |  0.000  0.061  0.000 |  0.001 58.267  0.000 |
Producto_B |     3.209 |  0.209 25.472  0.999 |  0.007 66.984  0.001 |  0.000  0.182  0.000 |
Producto_C |     1.846 | -0.065 14.674  1.000 |  0.000  0.259  0.000 | -0.001 41.465  0.000 |
Producto_D |     6.208 |  0.186 49.325  1.000 | -0.003 32.696  0.000 |  0.000  0.086  0.000 |

Columns
             Iner*1000    Dim.1    ctr   cos2    Dim.2    ctr   cos2    Dim.3    ctr   cos2  
Brillo     |     2.801 | -0.110 22.263  1.000 |  0.000  0.166  0.000 |  0.001 45.002  0.000 |
Duración   |     0.238 | -0.033  1.893  0.999 | -0.001  5.095  0.001 |  0.000  0.335  0.000 |
Olor       |     1.439 | -0.079 11.432  1.000 |  0.001  5.368  0.000 | -0.001 50.471  0.000 |
Comodidad  |     4.440 |  0.157 35.274  1.000 | -0.003 37.151  0.000 |  0.000  0.387  0.000 |
Limpieza   |     3.669 |  0.162 29.137  0.999 |  0.005 52.219  0.001 |  0.000  3.805  0.000 |

# Punto 4

https://www.statmethods.net/advstats/cluster.html

plot(fit) # display dendogram
column_to_rownames(punto3, var = "Producto")