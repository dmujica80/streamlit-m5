import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import codecs

st.title('Streamlit Reto Daniel Mújica')

DATA_URL = 'EmployeesReto.csv'

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL,'rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    return data

@st.cache
def filter_data_by_empleados(valorBuscar, columna):
    doc = codecs.open(DATA_URL,'rU','latin1')
    data = pd.read_csv(doc)
    filtered_data_empleados = data[data[columna].str.upper()==valorBuscar]
    return filtered_data_empleados

@st.cache
def filter_data_by_empleados_nivel(valorBuscar, columna):
    doc = codecs.open(DATA_URL,'rU','latin1')
    data = pd.read_csv(doc)
    filtered_data_empleados = data[data[columna]==valorBuscar]
    return filtered_data_empleados

data_load_state = st.text('Loading data...')
employees = load_data(500)
data_load_state.text("Done !!!")

if st.sidebar.checkbox('Mostrar todos los registros'):
    st.subheader('Todos los registros')
    st.write(employees)

st.markdown("___")

#Buscador por Id Empleado
idEmpleados = st.sidebar.text_input('ID Empleado :')
btnBuscar = st.sidebar.button('Buscar empleados')

if (btnBuscar):
   data_idEmpleados = filter_data_by_empleados(idEmpleados.upper(),'Employee_ID')
   count_row = data_idEmpleados.shape[0]  # Gives number of rows
   st.write(f"Total Empleados mostrados : {count_row}")
   st.write(data_idEmpleados)

#Buscador por Hometown
hometown = st.sidebar.text_input('Hometown :')
btnBuscarHome = st.sidebar.button('Buscar por hometown -> ')

if (btnBuscarHome):
   data_empleadosHome = filter_data_by_empleados(hometown.upper(),'Hometown')
   count_row = data_empleadosHome.shape[0]  # Gives number of rows
   st.write(f"Total Empleados Hometown mostrados : {count_row}")
   st.write(data_empleadosHome)

#Buscador por Unit
unit = st.sidebar.text_input('Unit :')
btnBuscarUnit = st.sidebar.button('Buscar por unit -> ')

if (btnBuscarUnit):
   data_empleadosUnit = filter_data_by_empleados(unit.upper(),'Unit')
   count_row = data_empleadosUnit.shape[0]  # Gives number of rows
   st.write(f"Total Empleados Unit mostrados : {count_row}")
   st.write(data_empleadosUnit)

doc = codecs.open(DATA_URL,'rU','latin1')
full_data = pd.read_csv(doc)

st.markdown("___")

selected_nivel = st.sidebar.selectbox("Selecciona Nivel Educativo", full_data['Education_Level'].unique())
btnFilterbyNivelEdu = st.sidebar.button('Filtrar nivel educativo ')

if (btnFilterbyNivelEdu):
   filterbynivel = filter_data_by_empleados_nivel(selected_nivel,'Education_Level')
   count_row = filterbynivel.shape[0]  # Gives number of rows
   st.write(f"Total empleados : {count_row}")

   st.dataframe(filterbynivel)

st.markdown("___")
edades = full_data[['Employee_ID','Age']].groupby(['Age']).count()
st.header('Empleados por Edad')
fig_edad = px.histogram(full_data['Age'])
st.plotly_chart(fig_edad)

st.markdown("___")
st.header('Empleados por Unidad')
fig_unit=px.histogram(full_data, x="Unit")
st.plotly_chart(fig_unit)

st.markdown("___")
fig3, ax3 = plt.subplots()
dfhometown = full_data[['Attrition_rate','Hometown']].groupby(['Hometown']).count()
ax3.plot(dfhometown)
st.header('Ciudades Mayor Índice Deserción')
st.pyplot(fig3)

st.markdown("___")
fig4, ax4 = plt.subplots()
dfedad = full_data[['Age','Attrition_rate']]
ax4.barh(dfedad['Age'],dfedad['Attrition_rate'])
ax4.set_ylabel("Edad")
ax4.set_xlabel("Índice Deserción")
st.header('Edades y Mayor Índice Deserción')
st.pyplot(fig4)


st.markdown("___")
fig5, ax5 = plt.subplots()
ax5.scatter(full_data['Time_of_service'], full_data['Attrition_rate'])
ax5.set_xlabel("Tiempo Servicio")
ax5.set_ylabel("Tasa de deserción")
st.header("Grafica relación entre el tiempo de servicio y la tasa de deserción")
st.pyplot(fig5)