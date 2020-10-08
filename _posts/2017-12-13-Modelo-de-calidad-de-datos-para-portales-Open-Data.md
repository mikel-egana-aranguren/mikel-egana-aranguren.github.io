---
layout: post
title: "Modelo de calidad de datos para portales Open Data"
date: 2017-12-13
---

&nbsp;

Según mi experiencia muchos portales Open Data contienen datasets con errores graves. Esos errores se introducen al producir el dato en cada departamento (medio ambiente, economía, etc) y no hay un control directo. Sin embargo, ese el problema más importante a resolver, ya que si los datos no son de una calidad mínima no son reusables, por muy sofisticadas que sean las tecnologías con las que se sirven los datos (API REST, Linked Data, etc.).

Es un problema de muy difícil solución, ya que no hay manera de obligar a los departamentos a producir datos de calidad. Sin embargo, una cosa que igual sí se podría hacer, es definir un modelo de calidad de datos con unos niveles de este estilo:

<u><b>Nivel 1:</b></u> nadie ha supervisado los datos, pueden tener todo tipo de errores (o no, a saber).

<u><b>Nivel 2:</b></u> un desarrollador ha mirado los datos, y se ha asegurado de que por los menos el "formato" sea correcto, aunque no haya analizado los datos en sí: por ejemplo que no haya celdas bailadas.

<u><b>Nivel 3:</b></u> un experto en el dominio concreto de los datos (ej. calidad del aire) los ha mirado, y aparte de asegurarse de que se cumple con el nivel 2, se ha asegurado también de que los datos en sí son de calidad. Por ejemplo, una celda que tiene una concentracion de NO2 de 5000 cumpliría con el "formato" de los datos, por que la columna se llama NO2, pero igual el valor 5000 es erróneo dese el punto de vista de los datos en sí (Igual debería ser 4500 teniendo en cuenta la estación del año).

De modo que se podrían crear badges para meter en cada ficha del dataset, para que el reusador por lo menos sepa qué tiene entre manos. También sería una manera de presionar a cada productor de datos para que los produzca de mejor calidad.

&nbsp;
