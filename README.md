# Predicción de Precios de Venta de Casas

Este proyecto utiliza un modelo de Machine Learning para predecir el precio de venta de una casa basado en varias características de la propiedad. El modelo está implementado en Django y utiliza el método de Random Forest. Este repositorio incluye el código necesario para cargar y utilizar el modelo desde un formulario web.

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar una herramienta que, a partir de ciertas características de las propiedades, como número de dormitorios, baños, metros cuadrados, entre otros, prediga el precio estimado de venta. Esta herramienta está orientada a usuarios que desean tener una aproximación rápida del valor de una propiedad basándose en sus características físicas y de ubicación.

## Datos de Entrenamiento

El dataset para el entrenamiento de este modelo fue obtenido de: [Kaggle Datasets](https://www.kaggle.com/datasets/aravinii/house-price-prediction-treated-dataset)

El procesio de entrenamiento y creacion del modelo se encuentra documentado en el archivo 'Model_Training.ipynb'.

El modelo fue entrenado con un dataset de propiedades, que incluye 14 variables clave, tales como:

- `bedrooms` (Número de dormitorios)
- `grade` (Calidad de la construcción)
- `has_basement` (Indica si tiene sótano)
- `living_in_m2` (Metros cuadrados habitables)
- `renovated` (Indica si fue renovada)
- `nice_view` (Indica si tiene una buena vista)
- `perfect_condition` (Estado de la propiedad)
- `real_bathrooms` (Número real de baños)
- `has_lavatory` (Indica si tiene medio baño)
- `single_floor` (Indica si es de una sola planta)
- `month` (Mes de la venta)
- `quartile_zone` (Zona en cuartiles de precios)

## Modelo: Random Forest

El modelo de Machine Learning implementado es un **Random Forest**, que consiste en múltiples árboles de decisión para mejorar la precisión de las predicciones. Los parámetros principales que se ajustaron en el modelo son:

- **n_estimators**: Número de árboles en el bosque.
- **max_depth**: Profundidad máxima de cada árbol.
- **min_samples_split**: Número mínimo de muestras necesarias para dividir un nodo interno.
- **min_samples_leaf**: Número mínimo de muestras necesarias en un nodo hoja.

Estos ajustes permiten optimizar el rendimiento del modelo para lograr predicciones más precisas en los datos de prueba.

## Librerías Utilizadas

Las siguientes librerías de Python se utilizaron en el desarrollo de este proyecto:

- `Django`: Framework web utilizado para desarrollar la interfaz de usuario.
- `sklearn`: Para el desarrollo del modelo Random Forest y manejo de datasets.
- `joblib`: Para cargar el modelo previamente entrenado en el entorno de Django.
- `pandas`: Para el manejo y procesamiento de datos en los datasets.
- `numpy`: Para operaciones matemáticas avanzadas necesarias en el preprocesamiento de los datos.

## Cómo Ejecutar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   ```
2. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```
3. Ejecuta el servidor de Django:
  ```bash
  python manage.py runserver
  ```
4. Accede a la aplicación en http://127.0.0.1:8000 y realiza una predicción ingresando los datos de la propiedad en el formulario.

## Uso del Modelo
El modelo precargado se utiliza en la aplicación Django a través de un formulario. Los datos del formulario se pasan al modelo Random Forest, que calcula y devuelve una predicción del precio de la casa en base a las características ingresadas.

##  Contribuciones
Este proyecto está abierto a contribuciones. Si deseas mejorar el modelo, añadir características o corregir errores, eres bienvenido/a a realizar un pull request.

## Licencia
Este proyecto está licenciado bajo la MIT License.
