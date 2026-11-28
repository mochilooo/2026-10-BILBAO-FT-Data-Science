
# AGENTS.md — Data Science, Machine Learning e Inteligencia Artificial

## 1. Perfil del usuario

El usuario es ingeniero electrónico especializado en automatización industrial y está desarrollando competencias profesionales en Data Science e Inteligencia Artificial.

Tiene experiencia e interés en:
- Python y programación.
- Análisis exploratorio de datos (EDA).
- Estadística y visualización.
- Machine Learning.
- Deep Learning.
- Ingeniería de datos.
- Bases de datos SQL.
- Power BI.
- Aplicaciones industriales y análisis de sensores.

Su objetivo es desarrollar proyectos rigurosos, reproducibles y útiles para su portfolio profesional.

## 2. Entorno de desarrollo

Equipo principal:
- MacBook Air M5.
- 16 GB de RAM.
- macOS.
- Visual Studio Code.
- Miniforge / Conda.
- Git y GitHub.

Librerías habituales:
- NumPy.
- Pandas.
- Matplotlib.
- Seaborn.
- Scikit-learn.
- XGBoost.
- LightGBM.
- Jupyter.

Reglas:
1. Comprobar siempre el entorno Conda activo.
2. No instalar paquetes en el entorno base sin necesidad.
3. Respetar las versiones existentes.
4. Comprobar compatibilidad antes de instalar o actualizar librerías.
5. Evitar dependencias innecesarias.
6. Considerar las limitaciones de memoria del equipo.
7. No asumir que una librería está instalada.

## 3. Python y calidad del código

Priorizar:
- Código modular y reutilizable.
- Funciones con responsabilidades claras.
- PEP 8.
- Nombres descriptivos.
- Docstrings cuando aporten valor.
- Gestión de excepciones.
- Tipado cuando resulte útil.
- Separación entre lógica, visualización y configuración.

Evitar:
- Código duplicado.
- Funciones excesivamente largas.
- Variables innecesarias.
- Dependencias injustificadas.
- Código difícil de mantener.

No complicar soluciones sencillas con arquitecturas innecesarias.

## 4. Análisis exploratorio de datos (EDA)

Antes de modelar, realizar un análisis estructurado.

### Inspección inicial
- Dimensiones del dataset.
- Tipos de variables.
- Valores nulos.
- Registros duplicados.
- Valores únicos.
- Estadísticas descriptivas.
- Distribuciones.
- Posibles inconsistencias.

### Análisis estadístico
- Distribuciones y asimetrías.
- Correlaciones.
- Relaciones entre variables.
- Detección de valores atípicos.
- Análisis temporal cuando corresponda.
- Identificación de patrones.

### Visualización
Priorizar:
- Histogramas.
- Boxplots.
- Scatterplots.
- Heatmaps.
- Gráficos de distribución.
- Series temporales.

Cada visualización debe responder a una pregunta analítica.

No generar gráficos sin justificar su utilidad.

## 5. Tratamiento de datos

1. No modificar los datos originales.
2. Mantener separados los datos originales y procesados.
3. Documentar las transformaciones.
4. Justificar el tratamiento de valores nulos.
5. Comprobar duplicados.
6. Revisar tipos de datos.
7. Detectar valores imposibles o inconsistentes.
8. Evitar eliminar observaciones sin justificación.
9. Mantener trazabilidad de las transformaciones.

No asumir que todos los valores atípicos son errores.

## 6. Machine Learning

Antes de entrenar un modelo:

1. Definir claramente el problema.
2. Identificar variable objetivo.
3. Determinar si es clasificación, regresión o clustering.
4. Analizar las variables disponibles.
5. Establecer una estrategia de validación.
6. Crear una línea base (baseline).

### Preparación de datos

Utilizar cuando corresponda:
- StandardScaler.
- MinMaxScaler.
- OneHotEncoder.
- OrdinalEncoder.
- SimpleImputer.
- ColumnTransformer.

Seleccionar las técnicas según la naturaleza de los datos y del algoritmo.

### Modelos

Considerar cuando proceda:
- Linear Regression.
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Gradient Boosting.
- XGBoost.
- LightGBM.
- K-Nearest Neighbors.
- Support Vector Machines.
- K-Means.

No utilizar modelos complejos sin compararlos con alternativas más sencillas.

## 7. Pipelines y validación

Priorizar Pipeline y ColumnTransformer de Scikit-learn cuando sean adecuados.

Reglas fundamentales:
- Evitar data leakage.
- Ajustar los transformadores únicamente con los datos de entrenamiento.
- Mantener separado el conjunto de test.
- Utilizar validación cruzada cuando corresponda.
- Aplicar GridSearchCV o RandomizedSearchCV cuando tenga sentido.
- No utilizar el conjunto de test para seleccionar hiperparámetros.

Explicar qué hace cada etapa del pipeline y por qué se utiliza.

## 8. Evaluación de modelos

No utilizar accuracy como única métrica de evaluación.

### Clasificación
Considerar:
- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion Matrix.
- ROC-AUC.
- PR-AUC.

### Regresión
Considerar:
- MAE.
- MSE.
- RMSE.
- R².

Seleccionar métricas en función del problema y de las consecuencias de los errores.

Comparar los modelos utilizando las mismas condiciones de validación.

No afirmar que un modelo es mejor únicamente porque obtiene una métrica superior sin analizar el contexto.

## 9. Reproducibilidad

Priorizar:
- Semillas aleatorias controladas.
- Versiones de dependencias documentadas.
- Separación de datos y código.
- Pipelines reproducibles.
- Registro de experimentos.
- Documentación de resultados.

Cuando sea posible, utilizar:
- requirements.txt.
- environment.yml.
- pyproject.toml.
- Git.

Los resultados deben poder reproducirse en otro entorno compatible.

## 10. Estructura de proyectos

Respetar la estructura existente.

Cuando sea necesario diseñar un proyecto nuevo, considerar:

- data/raw: datos originales.
- data/interim: datos intermedios.
- data/processed: datos procesados.
- notebooks: análisis exploratorio.
- src: código fuente.
- models: modelos entrenados.
- reports: resultados e informes.
- figures: visualizaciones.
- tests: pruebas.
- README.md: documentación.

No crear todas las carpetas automáticamente si no son necesarias.

## 11. Gestión de archivos y Git

1. Inspeccionar el repositorio antes de modificarlo.
2. Leer README.md y AGENTS.md aplicables.
3. No sobrescribir datos originales.
4. No eliminar archivos sin autorización.
5. Evitar subir datasets pesados a GitHub.
6. Considerar Git LFS cuando corresponda.
7. No incluir credenciales ni información sensible.
8. Mantener documentadas las modificaciones importantes.

## 12. Metodología de trabajo

Antes de comenzar una tarea:

1. Comprender el objetivo.
2. Inspeccionar los archivos disponibles.
3. Analizar la estructura del proyecto.
4. Identificar dependencias.
5. Detectar posibles problemas.
6. Proponer una solución razonada.

No modificar archivos antes de comprender su función.

No asumir que una transformación o modelo es correcto sin comprobarlo.

## 13. Aprendizaje y comunicación

El usuario está desarrollando sus conocimientos en Data Science y Machine Learning.

Por tanto:

- Responder en español.
- Explicar los conceptos técnicos de manera progresiva.
- No limitarse a entregar código.
- Explicar qué hace cada algoritmo.
- Justificar las decisiones técnicas.
- Utilizar ejemplos prácticos cuando ayuden.
- Diferenciar conceptos que puedan confundirse.
- No ocultar errores ni simplificar en exceso conceptos importantes.

Cuando se solicite código, proporcionar una solución funcional y explicar las partes relevantes.

## 14. Entrega de resultados

Al finalizar una tarea, indicar:

1. Qué se ha realizado.
2. Qué archivos se han creado o modificado.
3. Qué decisiones técnicas se han tomado.
4. Qué pruebas se han ejecutado.
5. Qué resultados se han obtenido.
6. Qué problemas quedan pendientes.

Nunca afirmar que una prueba se ha ejecutado si realmente no se ha ejecutado.
