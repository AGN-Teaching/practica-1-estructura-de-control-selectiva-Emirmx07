[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rMafNWiN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18627383)
# Práctica 1. Estructura de control selectiva

## Presentación del Problema
En esta práctica, se diseñó un programa en Python para calcular el sueldo neto de una persona empleada en una empresa. Se consideraron diferentes factores como el número de horas trabajadas, las reglas de pago de horas normales y extras, el cálculo del Impuesto Sobre la Renta (ISR), aportaciones a seguridad social y participación en fondos de ahorro.

El objetivo principal fue aplicar estructuras de control selectivas para determinar correctamente las deducciones y percepciones de cada empleado, obteniendo finalmente el sueldo neto.

## Diseño del Algoritmo
Para resolver este problema, se utilizaron los siguientes conceptos:

### 1. **Listas**
   - Se usaron listas para almacenar la tabla del ISR de forma estructurada, permitiendo recorrerla con un ciclo y seleccionar el porcentaje adecuado según el sueldo bruto.

### 2. **Strings**
   - Se emplearon cadenas de texto para manejar la entrada del usuario en opciones como el tipo de ahorro en la caja de ahorro de la empresa.

### 3. **Estructura de Control Secuencial**
   - Se aplicó una secuencia de instrucciones en la que se capturan los datos del usuario, se realizan los cálculos en orden lógico y finalmente se muestran los resultados.

### 4. **Estructura de Control Selectiva Simple**
   - Se usó para verificar la elección del usuario en las opciones de caja de ahorro y ahorro solidario, asignando los valores adecuados a las variables.

### 5. **Estructura de Control Selectiva Anidada**
   - Se implementó para calcular el sueldo bruto considerando las reglas de pago de horas normales y extras. Dependiendo del número de horas trabajadas, se aplicaban diferentes fórmulas de cálculo.

### 6. **Estructura de Control Selectiva Múltiple**
   - Se utilizó `if-elif-else` para determinar el rango del sueldo bruto dentro de la tabla de ISR y calcular el impuesto correspondiente.

## Implementación en Python
El programa solicita al usuario los siguientes datos de entrada:
- Salario por hora.
- Número de horas trabajadas.
- Tipo de participación en la caja de ahorro.
- Porcentaje de ahorro solidario.

Luego, realiza los cálculos correspondientes usando las estructuras de control mencionadas y finalmente imprime un resumen de la nómina con el sueldo bruto, deducciones y sueldo neto.

## Comentarios sobre la Implementación
El uso de listas me permitió manejar la tabla del ISR de manera más estructurada y eficiente. Además, las estructuras de control selectivas facilitaron la toma de decisiones en cada etapa del cálculo. Se recomienda mantener un código modular y organizado para facilitar su mantenimiento y futuras modificaciones.

En conclusión, la práctica permitió reforzar el uso de estructuras selectivas en Python y su aplicación en un contexto real como el cálculo de sueldos me di cuenta lo util que son las actividades que vimos en clase, y me interesa saber y aprender mas sobre esta clase.


