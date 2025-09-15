---
layout: post
title: "Crítica a Linked Data en Open Data Euskadi (III) Actualización"
date: 2015-07-01
---

Desde la <a href="http://wp.me/pEIjo-9p">primera crítica</a> constructiva que hice sobre la versión "Linked Data" de Open Data Euskadi algunas URIs han cambiado, pero los problemas descritos persisten (En el Open Data Day 2014 propusimos <a href="https://mikeleganaaranguren.wordpress.com/2014/02/26/critica-a-linked-data-en-open-data-euskadi-ii-solucion/">una solución</a>). Añado aquí las URIs nuevas:

<ol>
	<li>Web de datasets: <a href="http://opendata.euskadi.eus/w79-contdata/es/contenidos/ds_localizaciones/consulados/es_euskadi/index.shtml">http://opendata.euskadi.eus/w79-contdata/es/contenidos/ds_localizaciones/consulados/es_euskadi/index.shtml</a></li>
	<li>En el dataset en turtle, URI del consulado de Suiza: http://www2.irekia.euskadi.eus/es/entities/1047</li>
	<li>Negociación contenido simulando ser navegador web: curl http://www2.irekia.euskadi.eus/es/entities/1047. Resultado: HTML (OK)</li>
        <li>Negociación contenido simulando ser agente automático que quiere RDF/XML: curl --header "Accept: application/rdf+xml" http://www2.irekia.euskadi.eus/es/entities/1047. Resultado: HTML (not OK). </li>
</ol>

El problema es que la URI principal solo lleva a la página web, y dentro de la página web, hay una URL con un archivo RDF (http://www2.irekia.euskadi.eus/es/entities/1047-consulado-suiza.rdf). Eso viola el principio básico (Linked Data e incluso REST en general) de que las URIs denotan entidades, no sus representaciones. Tampoco hay enlaces (predicados) a, por ejemplo, Suiza en DBPedia.

Probamos con otro dataset, esta vez sacado de la bola <a href="http://datahub.io/dataset/open-data-euskadi">Open Data Euskadi</a> de la nube <a href="http://lod-cloud.net/versions/2014-08-30/lod-cloud_colored.svg">Linked Open Data</a>. El primer dataset de la lista es Farmacias de euskadi: http://opendata.euskadi.eus/contenidos/ds_localizaciones/farmacias_de_euskadi/opendata/r01DataSet.rdf. Pero el dataset no es sobre farmacias, es sobre metadatos de datos de farmacias, y el único enlace que parece significativo (es decir, tendría datos reales de farmacias) es http://opendata.euskadi.eus/contenidos/ds_localizaciones/farmacias_de_euskadi/farmacia/farmacias y no funciona (ni para humanos ni para agentes). El resto son triples sobre Dublin Core etc., más que predicados a otros datos. El resto de lo datasets siguen el mismo patrón: más que datos son metadatos, y los enlaces no funcionan.



 




