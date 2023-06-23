from fastapi import FastAPI
import pandas as pd
import numpy as np
#import json
#import ast
#from pandas.io.json import json_normalize
#import calendar

movies = pd.read_csv('Movies ETL.csv', sep=',') 
credits = pd.read_csv('Credits ETL.csv', sep=',')
cast = pd.read_csv('Cast.csv', sep=',')
director = pd.read_csv('Director.csv', sep=',')

app = FastAPI()

#@app.get("/")
#def titulo():
#    return {'Bienvenidos': 'al modelo de recomendación de películas'}

@app.get("/cantidad_filmaciones_mes/{Mes}")
def cantidad_filmaciones_mes(Mes):
#Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente

    # Convertir el mes a minúsculas y capitalizar la primera letra
    Mes = Mes.lower().capitalize()

    #Cargo el DF
    movies = pd.read_csv('Movies ETL.csv', sep=',')

    # Convertir la columna 'release_date' a tipo de dato datetime
    movies['release_date'] = pd.to_datetime(movies['release_date'])

    # Filtrar las películas que coinciden con el mes consultado. Para que reconozca los meses en Español tengo que usar el parámetro 'es_ES.utf8'.
    filmaciones_mes = movies[movies['release_date'].dt.month_name(locale='es_ES.utf8') == Mes]
    
    # Obtener la cantidad de filmaciones en el mes
    cantidad = len(filmaciones_mes)

    return {'Mes': Mes, 'Cantidad de películas': cantidad}
    #f'{cantidad} cantidad de películas fueron estrenadas en el mes de {Mes}'


@app.get('/cantidad_filmaciones_dia{Dia}')
def cantidad_filmaciones_dia( Dia ):
#Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente
   
    # Convertir el mes a minúsculas y capitalizar la primera letra
    Dia = Dia.lower().capitalize()

    #Cargo el DF
    movies = pd.read_csv('Movies ETL.csv', sep=',')

    # Convertir la columna 'release_date' a tipo de dato datetime
    movies['release_date'] = pd.to_datetime(movies['release_date'])

    # Filtrar las películas que coinciden con el mes consultado. Para que reconozca los meses en Español tengo que usar el parámetro 'es_ES.utf8'.
    filmaciones_dia = movies[movies['release_date'].dt.day_name(locale='es_ES.utf8') == Dia]
    
    # Obtener la cantidad de filmaciones en el mes
    cantidad = len(filmaciones_dia)

    return {'Día': Dia, 'Cantidad de películas': cantidad}
    #f'{cantidad} cantidad de películas fueron estrenadas en el mes de {Dia}'


@app.get('/score_titulo/{titulo_de_la_filmación}')
def score_titulo(titulo_de_la_filmación):
#Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score    
    #Paso a minúscula para que luego coincida con los valores del Dataframe.
    titulo_de_la_filmación = titulo_de_la_filmación.lower()

    #cargo el DF
    movies = pd.read_csv("Movies ETL.csv", sep= ',')

    #En el df movies, pasar todos los títulos a minúsculas 
    movies['title'] =  movies['title'].str.lower()

    # Filtrar los datos por el título de la filmación
    filtro = movies['title'] == titulo_de_la_filmación
    pelicula = movies.loc[filtro]

    # Verificar si se encontró alguna película con el título dado
    if pelicula.empty:
        return "No se encontró ninguna película con ese título."

    # Obtener el título, año de estreno y score de la película encontrada
    titulo = pelicula['title'].values[0]
    año_estreno = pelicula['release_year'].values[0]
    score = pelicula['popularity'].values[0]    

    return {'La película': titulo, 'fue estrenada en el año': año_estreno, 'con un score/popularidad de': score} 
    #f"La película {titulo} fue estrenada en el año {año_estreno} con un score/popularidad de {score}."


@app.get('/votos_titulo/{titulo_de_la_filmación}')
def votos_titulo( titulo_de_la_filmación ):
#Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
#La misma variable deberá de contar con al menos 2000 valoraciones, 
#caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.


    #Paso a minúscula para que luego coincida con los valores del Dataframe.
    titulo_de_la_filmación = titulo_de_la_filmación.lower()

    #cargo el DF
    movies = pd.read_csv("Movies ETL.csv", sep= ',')

    #En el df movies, pasar todos los títulos a minúsculas 
    movies['title'] =  movies['title'].str.lower()


    # Filtrar por título de la filmación
    filtro_titulo = movies['title'] == titulo_de_la_filmación
    pelicula = movies.loc[filtro_titulo]

    # Verificar la cantidad de votos
    if pelicula['vote_count'].values[0] > 2000:

        # Obtener los valores requeridos
        titulo = pelicula['title'].values[0]
        votos = pelicula['vote_count'].values[0]
        promedio = pelicula['vote_average'].values[0]

        return {'La película': titulo, 'cuenta con una cantidad total de votos de': votos, 'con un promedio de': promedio}
        #f"La película {titulo} cuenta con un total de {votos} valoraciones, con un promedio de {promedio}"

    else:
        #Mensaje si vote_count < 2000
        return {'La película': 'no cuenta con al menos 2000 valoraciones'} 
        #f'La película no cuenta con al menos 2000 valoraciones'


@app.get('/get_actor/{nombre_actor}')
def get_actor( nombre_actor ):
#Se ingresa el nombre de un actor debiendo devolver el éxito del mismo medido a través de la suma de los retornos obtenidos en todas sus películas. 
#Además, debe devolver la cantidad de películas que en las que ha participado y el retorno promedio por película.

    #convierto la variable a minúsculas para independizarme de la forma en que el usuario escribe el nombre
    nombre_actor = nombre_actor.lower()

    #Tengo que unir Movies ETL.csv y Cast.csv a través de id
    df_cast = pd.merge(movies, cast, on='id')

    #Convierto los valores de la columna cast_name a minúscula.
    df_cast['cast_name'] =  df_cast['cast_name'].str.lower()

    #Creo un DF con los datos que necesito
    get_actor = pd.DataFrame(data= df_cast, columns=['cast_name', 'id', 'return'])

    #Filtro el DF por el nombre que ingresó el usario
    get_actor = get_actor[get_actor['cast_name'] == nombre_actor]

    #Hago los cálculos
    count = get_actor['id'].count() #Cuento la cantidad de películas en la que participó el actor.
    total_return = get_actor['return'].sum() #Éxito del actor, medido por la suma del retorno
    avg_return = get_actor['return'].mean() #Se incluye también el retorno promedioen función de las películas en las que actuó.

    return {'El actor': nombre_actor, 'ha participado de': count, 'filmaciones. Ha conseguido un retorno de': total_return, 'con un promedio por película de': avg_return} 
    #f'El actor {nombre_actor} ha participado de {count} cantidad de filmaciones, el mismo ha conseguido un retorno de {total_return} con un promedio de {avg_return} por filmación'


@app.get('/get_actor/{nombre_director}')
def get_director( nombre_director ):
#Esta función pide com parámetro el nombre de un director.
#Debe devolver el éxito del mismo medido como la suma de los retornos de todas las películas que dirigió.
#Además, debe devolver el nombre de cada película que dirigió junto con su correspondiente fecha de lanzamiento (release_date), retorno individual (return), costo (bugdet) y ganancia (revenue)

    #convierto la variable a minúsculas para independizarme de la forma en que el usuario escribe el nombre
    nombre_director = nombre_director.lower()

    #Tengo que unir Movies ETL.csv y Director.csv a través de id
    df_director = pd.merge(movies, director, on='id')

    #Convierto los valores de la columna cast_name a minúscula.
    df_director['crew_name'] =  df_director['crew_name'].str.lower()

    #Creo un DF con los datos que necesito
    get_director = pd.DataFrame(data= df_director, columns=['id', 'crew_name' , 'title', 'release_date', 'return', 'budget', 'revenue'])

    #Filtro el DF por el nombre que el usuario puso
    get_director = get_director[get_director['crew_name'] == nombre_director]

    #Sumo el total_return
    dir_total_return = get_director['return'].sum()

    #Agrego al df la columna con el total_return
    get_director['director_total_return'] = get_director['return'].sum()

    #Devuelvo el return total y una tabla con el detalle de cada película
    return get_director

        #(
        #f"El director {nombre_director} ha conseguido un retorno total de {dir_total_return}.",
        #f"A continuación se muestra un detalle de todas las películas que digrigió:",
        #get_director
        #)





#############################################################################################


# ML
#@app.get('/recomendacion/{titulo}')
#def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
#    return {'lista recomendada': respuesta}