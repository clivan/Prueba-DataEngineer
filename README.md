# Prueba técnica - Data Engineer

## Objetivo
Construir una solución End-to-End que cubra:
- Lectura de datos desde un CSV
- Limpieza y estandarización
- Análisis
- API REST
- Visualización de métricas clave

## Estructura del proyecto
- Directorio *app*, que contiene los archivos de python con el proyecto end-to-end
- Directorio *data*, con el csv original, y un parquet con los datos procesados
- Directorio *db*, que contiene el archivo de base de datos.
- Directorio *sql*, con el DDL de sql
- Directorio *Notebooks*, con el cuaderno de trabajo.

## Etapas
### Lectura de datos
#### Problemas detectados
- Símbolo de pesos ($)
- Separador de miles
- Inconsistencia en formato de fechas
- Valores duplicados
- Valores nulos
- Totales incorrectos

#### Estrategias aplicadas
- Conversión usando regex para datos numéricos
- Estandarización de fechas a YYY-MM-DD
- Normalización de la columna *customer_name* (convertir a maypusculas y aplicar trim)
- Eliminación de duplicados
- Recalcular totales
- Control de valores NULL

### Análisis
Se crearon las tablas *fact_sales*, *dim_customer*, *dim_date*, con el fin de simplificar las segregaciones, optimizar consultas analíticas, facilita escalabilidad futura.
Se eligió SQLite, dado que el dataset es pequeño (10, 000 registros), en este ejemplo no hay concurrencia, portable.

### API REST
Se implementó FastAPI, y se tomaron los endpoint *GET /sales/monthly*, así como *GET /sales/top*. Se limpiaron los valores no compatibles con JSON, así como los valores NULL.
El acceso se da mediante
´´´
{
http:localhost:8000/docs
}
´´´

### Visualización
A través de un script, se generan las dos gráficas necesarias, y ambas se guardan en la carpeta outpu:
![pending](/output/pending.png)
![sales_trend](/output/sales_trend.png)
De la misma forma, se emplea una Notebook de Jupyter para mostrar el proceso de limpieza, la validación de valores, consumo de API, visualización.

### Dockerización
Para esta prueba se utilizó Docker para garantizar reproductibilidad y portabilidad, aislar el entorno, aislar dependencias locales. Se ejecuta desde
´´´
{
docker compose up --build
}
´´´


