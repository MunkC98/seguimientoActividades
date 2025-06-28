import pandas as pd
import streamlit as st
import datetime as dt
import os

hoy = dt.date.today()
nombre_dia = hoy.strftime('%A')
path_data = 'data/data.csv'
dias_laborales = ['Monday', 'Wednesday', 'Thursday', 'Friday']
martes = 'Tuesday'

lista_actividades_1 = ['Levantarme', 'Desayuno', 'Trabajo1', 'Comida', 'Trabajo2', 'Tesis','Cena', 'Box', 'Dormir']
lista_actividades_2 = ['Levantarme', 'Desayuno', 'Trabajo1', 'Comida', 'Trabajo2', 'Tesis','Cena', 'Jugar con amigos', 'Dormir']
lista_actividades_3 = ['Levantarme', 'Desayuno', 'Tarkowndo', 'Comida', 'Tesis','Cena', 'Dormir']
lista_de_horas_1 = ['7:00am', '8:00am', '9:00am', '2:00pm', '3:00pm', '6:00pm', '7:00pm', '9:00pm', '11:00pm']
columnas = ['Fecha', 'Actividades', 'Completada']


df = pd.read_csv(path_data)


if hoy in df.Fecha:
	pass
elif nombre_dia in dias_laborales:
	fecha = [hoy] * len(lista_actividades_1)
	completada = [False] * len(lista_actividades_1)
	datos = {
	"Fecha": fecha,
	"Actividad": lista_actividades_1,
	"Completada": completada
	}

	actualizacion = pd.DataFrame(datos)
	df = pd.concat([df,actualizacion], axis = 0)

elif nombre_dia == martes:
	fecha = [hoy] * len(lista_actividades_2)
	completada = [False] * len(lista_actividades_2)
	datos = [fecha, lista_actividades_2, completada]
	actualizacion = pd.DataFrame(datos, columns=columnas)
	df = pd.concat([df,actualizacion])
elif nombre_dia in fines_de_semana:
	fecha = [hoy] * len(lista_actividades_3)
	completada = [False] * len(lista_actividades_3)
	datos = [fecha, lista_actividades_3, completada]
	actualizacion = pd.DataFrame(datos, columns=columnas)
	df = pd.concat([df,actualizacion])

st.title("Seguimiento de las actividades - " + f'{hoy}')

st.header(nombre_dia)

def lista_actividades(dia_semana):
	col_hora, col_tarea = st.columns([1,3])
	with col_hora:
		st.markdown('## Hora')
	with col_tarea:
		st.markdown('## Tarea')
	if dia_semana in dias_laborales:
		for hora in lista_de_horas_1:
			with col_hora:
				st.markdown(hora)
		for actividad in lista_actividades_1:
			with col_tarea:
				st.checkbox(actividad, value=False, key=actividad)

lista_actividades(nombre_dia)

