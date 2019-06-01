# Posibles analisis
COD_MUNIC -> Establecer la concentración en que municipio se ha presentado más el asunto del cancer


## Cluster
https://www.statmethods.net/advstats/cluster.html

## LDA
https://www.apsl.net/blog/2017/07/18/using-linear-discriminant-analysis-lda-data-explore-step-step/
https://medium.com/journey-2-artificial-intelligence/lda-linear-discriminant-analysis-using-python-2155cf5b6398
https://scikit-learn.org/stable/modules/lda_qda.html

## PCA
https://rpubs.com/PachoAlvarez/232979


# Rstudio PCA

## Instalando Requerimientos
* install.packages("psych")
* install.packages("GPArotation")

## Incluir Requerimientos
* library(psych)
* library(GPArotation)


Principal Components Analysis
Call: principal(r = saludCompleta, nfactors = 3, rotate = "none", 
    use = pairwise)
Standardized loadings (pattern matrix) based upon correlation matrix
              PC1   PC2   PC3   h2   u2 com
Lugar_def   -0.20  0.51  0.48 0.53 0.47 2.3
Anno         0.77 -0.02  0.14 0.61 0.39 1.1
Grupo_Edad   0.07 -0.27  0.84 0.79 0.21 1.2
Nivel_Edu   -0.11  0.51  0.23 0.33 0.67 1.5
Etnia       -0.78 -0.22  0.12 0.66 0.34 1.2
Seg_Social  -0.05  0.75 -0.16 0.59 0.41 1.1
Antecedente  0.34  0.17  0.11 0.16 0.84 1.7