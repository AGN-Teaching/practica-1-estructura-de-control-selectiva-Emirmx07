[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rMafNWiN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18627383)
# Práctica 1. Estructura de control selectiva

Presentación del problema
En esta práctica, se nos ha pedido desarrollar un programa en Python que calcule el sueldo neto que recibe un empleado de una empresa, considerando diferentes factores como:

El salario por hora.

Las horas trabajadas en el mes y los respectivos incrementos salariales por horas extras.

Los impuestos sobre la renta (ISR) aplicados de manera progresiva según la tabla del SAT.

Las deducciones por seguridad social y aportaciones a la caja de ahorros de la empresa.

La participación opcional en el fondo de ahorro solidario.

El objetivo es solicitar al usuario los datos necesarios, calcular su sueldo bruto, aplicar las deducciones correspondientes y mostrar su sueldo neto.

Comentarios sobre el diseño del algoritmo
Para abordar este problema, diseñamos el algoritmo de la siguiente manera:

Solicitamos al usuario los datos de entrada: salario por hora, horas trabajadas, tipo de ahorro y participación en el fondo solidario.

Calculamos el sueldo bruto considerando las reglas de pago por horas trabajadas y horas extras.

Determinamos el ISR basándonos en la tabla progresiva del SAT.

Calculamos las deducciones por seguridad social y ahorros voluntarios.

Restamos todas las deducciones al sueldo bruto para obtener el sueldo neto.

Finalmente, mostramos un resumen con todos los cálculos realizados.

El programa se estructura mediante funciones modulares, lo que mejora la organización y la reutilización del código.

Comentarios sobre la implementación en Python
El código en Python se implementó siguiendo buenas prácticas de programación:

Se utilizaron funciones para segmentar el cálculo del sueldo bruto, ISR y deducciones.

Se usaron estructuras de control selectivas para determinar la categoría salarial del usuario en la tabla de ISR.

Se emplearon operaciones matemáticas para los cálculos de deducciones y sueldo neto.

Se incluyeron entradas del usuario y validaciones básicas para garantizar que los valores ingresados sean correctos.

El programa cumple con los requisitos de la práctica y proporciona un desglose detallado del cálculo del sueldo neto de un empleado.

