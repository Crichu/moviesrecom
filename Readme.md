# <h1 align=center> **Sistema de análisis y recomendación de películas** </h1>

# <h1 align=center>**`Proyecto Individual de final de Bootcamp: Machine Learning Operations (MLOps)`**</h1>

**`Autor: Cristian Biava`**

## **Propuesta de trabajo**</h2>
La propuesta es desarrollar un sistema de recomendación de películas basado en el Dataset cuyo link de acceso se facilita más abajo.

La propuesta incluye:

**`Realizar la Transformación de los datos originales`** con el objetivo de lograr un **´MVP´** (_Minimum Viable Product_).
* Tecnología y librerías utilizadas: Python, Pandas, Numpy, ast

**`Desarrollar una API`** en donde se puedan hacer consultar relacionadas con el mundo cinematigráfico y, en partiucular, con la información contenida en el Dataset
* Tecnología y librerías utilizadas: Python, FastAPI, Render

**`Desarrollar un sistema de recomendación`** de películas en base a las preferencias del usuario.
* Tecnología y librerías utilizadas: Python, Pandas, Numpy, Seaborn, Matplotlib, sklearn



## **Trabajo realizado**</h2>

### **`Proceso de ETL`**</h3>

En la carpeta Dataset se encuentran dos archivos .csv (movies_dataset.csv y credits.csv) que contienen los datos a ser procesados y un Diccionario con algunas descripciones de las columnas dosponibles.

***ETL de movies_dataset.csv***</h4>

En este archivo está la información detallada de cada película (año de lanzamiento, beneficios, presupuesto, género, productora, idiomas, etc)

En primer lugar se analizó el archivo movies_dataset.csv. Luego de un breve analisis exploratorio, se procede a realizar las transformaciones que incluyen:

    * Eliminar columnas sin utilidad.
    * Reemplazar o eliminar valores nulos y NA.
    * Convertir las columnas de fechas a formato fecha.
    * Agregar columnas con cálculos. En esta caso, la columna 'return' (retorno) que se obtiene de dividir 'revenue' (beneficios) y 'budget' (presupuesto).
    * Desanidar los campos que contienen diccionarios o listas como valores.

El Dataframe resultante se exportó como 'Movies ETL.csv'.

Más detalles: 'Movies ETL.ipynb'

***ETL de credits***</h4>

En este archivo hay información sobre actores, pesonajes y staff (incluyuendo directores) de cada película.

Al igual que en el caso, luego de un breve analisis exploratorio, se hicieron las siguientes transformaciones:

    * Elimar los duplicados de la columna id.
    * Desanidar campos que contienen diccionario o listas como valores.

A partir del Dataframe resultante, se generaron dos Dataframes que luego fueron exportados como cvs:

1) 'Director.csv' que contiene información sobre los directores de cada película

2) 'Cast.csv' que contiene información sobre los actores de cada película.

Más detalles: Credits ETL.ipynb


### **`Desarrollo de API`**</h3>

***Desarrollo de funciones***</h4>

Se proponen 6 consultas. Para cada una de ellas, se crea una función que serán los endpoints que se consumirán en la API.

A continuación se listan las 6 funciones generadas:

+ **def cantidad_filmaciones_mes( Mes )**: Se ingresa un mes en idioma Español. Se devuelve la cantidad de películas que fueron estrenadas históricamente en el mes consultado.

+ **def cantidad_filmaciones_dia( Dia )**: Se ingresa un día en idioma Español. Se devuelve la cantidad de películas que fueron estrenadas históricamente en el día consultado.

+ **def score_titulo( titulo_de_la_filmación )**: Se ingresa el título de una película. Se devuelve el título, el año de estreno y el score (utilizo la columna 'popularity' que es el score de popularidad asignado por la TMDB (TheMoviesDataBase)).

+ **def votos_titulo( titulo_de_la_filmación )**: Se ingresa el título de una filmación. Se devuelve el título, la cantidad de votos y el valor promedio de las votaciones. 

    Si la película consultada no cuenta con al menos 2000 valoraciones, se devuelve un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.

+ **def get_actor( nombre_actor )**: Se ingresa el nombre de un actor. Se devuelve el éxito del mismo medido a través del retorno. 

    Además, la cantidad de películas en las que ha participado y el promedio de retorno.
    
+ ** def get_director( nombre_director )**: Se ingresa el nombre de un director. Se devuelve el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

Más detalles: 'Desarrollo de funciones.ipynb'


***Desarrollo de API***</h4>

Las funciones creadas se copiaron en el archivo 'main.py' en donde se desarrolla la API utilizando la librería FastAPI.

En este archivo, se genera un ruta raíz (@get.app'/') y los decoradores para cada una de las 6 funciones.

Esto permite crear una url para consulta.

En este punto, antes de continuar con el deploy, se probó la API generada de manera local utilizando uvicorn.

***Desarrollo del deployment***</h4>

Luego de que las pruebas locales fueran exitosas, se implementa la app alojandola en render.com.

Aquí se presentaron algunos desafíos relacionados con la limitación que plantea la versión gratuita de render.com.

Entre otras cosas, fue necesario volver al codigo base en 'main.py' con el objetivo de optimizar el uso de memoria, ya que en la versión gratuita de render la disponibilidad de recursos es limitada.

También fue necesario cambiar manualmente la versión de algunas librerías ya que en render no se cuenta con las últimas versiones.

**`Desarrollo del sistema de recomendación`**</h3>

***EDA***</h4>

***Modelo***</h4>

## **Links de interés**
***Dataset***</h4>

***Repositorio Github***</h4>

***API***</h4>

***Video demostración***</h4>