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

+ Eliminar columnas sin utilidad.
+ Reemplazar o eliminar valores nulos y NA.
+ Convertir las columnas de fechas a formato fecha.
+ Agregar columnas con cálculos. En esta caso, la columna 'return' (retorno) que se obtiene de dividir 'revenue' (beneficios) y 'budget' (presupuesto).
+ Desanidar los campos que contienen diccionarios o listas como valores.

El Dataframe resultante se exportó como ['Movies ETL.csv'](https://github.com/Crichu/moviesrecom/blob/main/Movies%20ETL.csv).

Más detalles: ['Movies ETL.ipynb'](https://github.com/Crichu/moviesrecom/blob/main/Movies%20ETL.ipynb)

***ETL de credits***</h4>

En este archivo hay información sobre actores, pesonajes y staff (incluyuendo directores) de cada película.

Al igual que en el caso, luego de un breve analisis exploratorio, se hicieron las siguientes transformaciones:

+ Elimar los duplicados de la columna id.
+ Desanidar campos que contienen diccionario o listas como valores.

A partir del Dataframe resultante, se generaron dos Dataframes que luego fueron exportados como cvs:

1) ['Director.csv'](https://github.com/Crichu/moviesrecom/blob/main/Director.csv) que contiene información sobre los directores de cada película

2) ['Cast.csv'](https://github.com/Crichu/moviesrecom/blob/main/Cast.csv) que contiene información sobre los actores de cada película.

Más detalles: ['Credits ETL.ipynb'](https://github.com/Crichu/moviesrecom/blob/main/Credits%20ETL.ipynb)

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
    
+ **def get_director( nombre_director )**: Se ingresa el nombre de un director. Se devuelve el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

Más detalles: ['Desarrollo de funciones.ipynb'](https://github.com/Crichu/moviesrecom/blob/main/Desarrollo%20de%20Funciones.ipynb)


***Desarrollo de API***</h4>

Las funciones creadas se copiaron en el archivo ['main.py'](https://github.com/Crichu/moviesrecom/blob/main/main.py) en donde se desarrolla la API utilizando la librería FastAPI.

En este archivo, se genera un ruta raíz (@get.app'/') y los decoradores para cada una de las 6 funciones.

Esto permite crear una url de consulta para cada una de las  funciones.

En este punto, antes de continuar con el deploy, se probó la API generada de manera local utilizando uvicorn.

***Desarrollo del deployment***</h4>

Luego de que las pruebas locales fueran exitosas, se implementa la app alojandola en render.com.

Aquí se presentaron algunos desafíos relacionados con la limitación que plantea la versión gratuita de render.com.

Entre otras cosas, fue necesario volver al codigo base en 'main.py' con el objetivo de optimizar el uso de memoria, ya que en la versión gratuita de render la disponibilidad de recursos es limitada.

También fue necesario cambiar manualmente la versión de algunas librerías ya que en render no se cuenta con las últimas versiones.

Más detalles: ['main.py'](https://github.com/Crichu/moviesrecom/blob/main/main.py)

### **`Desarrollo del sistema de recomendación`**</h3>

***EDA***</h4>

Con el objetivo de conocer aún más los datos y detectar patrones y outliers que pudieran interferir en el modelado del sistema de recomendación, se realizó un Analisis Eploratorio de los Datos (EDA).

+ **Nube de palabras**

Se comparan las palabras más frecuentes en los títulos y las más frecuentes en los overview. Lo cual puede dar una idea de cuán representativos son lo overview respecto a los títulos.

Es importante relevar esto a la hora de construir un sistema de recomendación basado en contenido.

Los resultados fueron los siguientes:

*Títulos*

Las palabras que más aparecen en los títulos son 'Love' y 'Man'.
También 'Life', 'Girl', 'Day' y 'Nigth' son bastante comunes.

<p align=center><img src=https://github.com/Crichu/moviesrecom/blob/main/Nube%20de%20palabras%20Titulo.png><p>


*Overview*

'life' y 'find' son las palbras más comunes en los overview. Además, 'love', 'live' y 'family' también son muy populares.

<p align=center><img src=https://github.com/Crichu/moviesrecom/blob/main/Nube%20de%20palabras%20Overview.png><p>

***Conclusión***

Estas plabras se relacionan en cierto sentido con las palabras encotradas en el gráfico de nubes de títulos. Con lo cual, podemos concluir que, de manera general, los títulos por sí mismos son representativos de los temas que tratan las películas.


+ **Análisis de franquicias**

Interesa conocer el puntaje de popularidad asignado por la TDMB de cada franquicia. Podría ser útil a la hora de recomendar películas de la misma saga.

<p align=center><img src=https://github.com/Crichu/moviesrecom/blob/main/Franquicias%20populares.png><p>

***Conclusión***

El top5 de colecciones más populares (ordenados por sum) son:
1) Despicable Me Collection	
2) James Bond Collection		
3) Wonder Woman Collection		
4) Pirates of the Caribbean Collection		
5) Planet of the Apes (Reboot) Collection


+ **Popularidad: Analisis de distribución y detección de outliers**

La popularidad de cada película podría ser utilizada para ordenar las recomendaciones.

En concecuencia, sería útil analizar los datos numéricos que contiene esta columna y detectar ouliers.

Una distribución de frecuencia de valores de popularidad arroja que hay valores muy alejados del resto de los datos.

<p align=center><img src=https://github.com/Crichu/moviesrecom/blob/main/Histograma%20popularidad.png><p>

Entremos más en detalle: *¿Cuáles son las películas que tienen popularidades tan altas?*

<p align=center><img src=https://github.com/Crichu/moviesrecom/blob/main/listado%20de%20peliculas%20populares.png><p>

***Conclusión***

Vemos que los títulos con mayor popularidad, valores que llamabamos outliers, son películas muy conocidas que rompieron muchos record en cines y streaming. Por lo tanto, pueden ser considerados como valores atípicos pero válidos. Y, por ende, no se quitarán del dataset.


*Notese que durante el EDA se hizo mucho hincapié en la popularidad.*

*Esto se debe a que, al tratarse de un sistema de recomendación, se prioriza la popularidad por sobre otras variables porque es más probable que el usuario haya escuchado hablar de las películas con mayor ranking de popularidad y sería más factible que, al aparecer en un listado de recomendaciones éste las consuma.*

Más detalles: ['EDA.ipynb'](https://github.com/Crichu/moviesrecom/blob/main/EDA.ipynb)


***Sistema de recomendación***</h4>

La propuesta es crear un modelo de recomendación de películas basado en contenido.

El usuario deberá ingresar el título de una película. Se devuelven 5 películas similares.

En línea con las conclusiones del EDA, se construye un modelo basado en contenido, teniendo en cuenta el overview de las películas.

También se priorizan las películas más populares por lo explicado más arriba.

Para ello se hace uso de un modelo de KNN y se calificarán los ítems de acuerdo a similitud de cosenos.

+ **Paso 1: Preparar los datos**

Durante esta etapa se trabajó con ['Movies ETL.csv'](https://github.com/Crichu/moviesrecom/blob/main/Movies%20ETL.csv) como dataset de origen.

Debido a las limitaciones de recursos de Render.com, que fueron ya mencionadas anteriormente, surje la necesidad de reducir el dataset.

Con este objetivo, primero se ordena el dataframe de acuerdo a la popularidad ('popularity') y se extraen los primeros 5.000 registros.

+ **Paso 2: Vectorización**

Se crea una matriz numérica a partir de la columna 'overview'. Esta matriz contiene información numérica que representa la importancia relativa de cada palabra en cada resumen de película. Esto permite cuantificar la relevancia de las palabras en cada registro en relación con el conjunto completo de datos.

+ **Paso 3: Construncción del modelo KNN**

Aquí simplemente se instancia el modelo y se entrena.

Se utiliza el módulo NearestNeighbors de la librería sklearn.

+ **Paso 4: Crear la función de recomendación**

Ingresado el título de una película, el algoritmo trabaja con el dataset reducido y la matriz numérica definida en el paso 2, creando una lista de 5 elementos (películas afines) ordenadas de mayor a menor en función a score que el modelo determina.


## **Links de interés**
[**Dataset**](https://drive.google.com/drive/folders/1nvSjC2JWUH48o3pb8xlKofi8SNHuNWeu)

[**API**](https://movies-master-app.onrender.com/docs)

[**Video demostración**]()