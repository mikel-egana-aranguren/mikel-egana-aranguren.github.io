---
layout: post
title: "Publicar datos RDF con Amazon EC2 + Virtuoso"
date: 2014-06-20
---

<strong>Introducción</strong>

Para <a href="http://mikeleganaaranguren.wordpress.com/2013/10/22/critica-a-linked-data-en-open-data-euskadi/">publicar datos en Linked Data</a> necesitamos un servidor web potente con un <a href="http://en.wikipedia.org/wiki/Triplestore">Triple Store</a> como <a href="http://virtuoso.openlinksw.com/">Virtuoso</a>. A veces nos puede salir mejor utilizar un servicio tipo cloud como <a href="http://aws.amazon.com/es/ec2/">Amazon EC2</a> (por ejemplo <a href="http://gallir.wordpress.com/2009/12/30/como-montamos-meneame-en-amazon-ec2/">meneame lo usa</a>) que tener nuestro propio servidor (de hecho, muchas veces!). En este <a href="https://gist.github.com/mikel-egana-aranguren/83480630b2835f89080a">mini tutorial</a> vamos a publicar un dataset RDF implementando un triple store Virtuoso en una instancia Amazon EC2. Amazon tiene una oferta "free tier" que supongo que será para todo el mundo (puede ser que la tenga por ser usuario premium?); en cualquier caso la instancia que vamos a usar es la que menos prestaciones tiene asi que sera baratísima si no tienes "free tier". La idea es que con este primer paso luego ya puedes implementar algo más potente, con auto-scale, balanceadores de carga y todo eso. 

<strong>Crear instancia Amazon EC2</strong>

Nos hacemos una cuenta en <a href="http://aws.amazon.com/">Amazon Web Services</a> y entramos. Vamos a Services y EC2. Ahi Launch Instance (debajo de create instance). En el menú podriamos elegir una imagen que ya contiene Virtuoso, pero viene con CentOS que es un poco lo peor asi que elegimos Ubuntu Server 64 bits (deberia ser free tier). En el siguiente paso elegimos la instancia t1.micro y le damos a configurar: aquí solo asegurarse de que la instancia tendra una IP publica, "Automatically assign a public IP address to your instances". En el paso add storage los valores por defecto valen, pero se pueden añadir hasta 30 GB con el free tier, asi que los añadimos (también podemos elegir SSD en vez de magnetico, pero en realidad para lo que vamos hacer aquí da un poco igual todo esto del rendimiento I/O). En tag instance ponemos lo que sea. En security groups hay que añadir las siquientes reglas:

- Una regla para acceder mediante SSH (Yo aqui puse "My computer" por que tengo una IP fija).

- Otra regla "Custom TCP rule", "port range=8890", "anywhere" (para que usuarios externos accedan a virtuoso y podamos testear el sistema con consultas SPARQL).

- Otra regla "HTTP anywhere", por si queremos añadir un servidor <a href="http://wifo5-03.informatik.uni-mannheim.de/pubby/">Pubby</a>, por ejemplo, para implementar <a href="https://github.com/OpenDataDayBilbao/Linked-Data-Open-Data-Euskadi">Linked Data mediante negociacion de contenido</a>.

Creamos la instancia y generamos una clave .pem para poder acceder mediante SSH.  

<strong>Instalar y configurar Virtuoso</strong>

Hacemos <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html">SSH</a> a nuestra instancia activa y:

- Instalar Virtuoso: <code>sudo apt-get install virtuoso-opensource</code>

- Editar <code>/etc/virtuoso-opensource-6.1</code> y añadir el path del directorio donde estara el RDF que queremos cargar (nuestra home en la instancia EC2): <code>DirsAllowed = ., /usr/share/virtuoso-opensource-6.1/vad, /home/ubuntu</code>.

- Reiniciar virtuoso: <code>sudo service virtuoso-opensource-6.1 restart</code>.

<strong>Cargar RDF en virtuoso</strong>

- Como dataset ejemplo, usamos una proteina de UniProt: <code>wget http://www.uniprot.org/uniprot/P08251.rdf</code>.

- Ejecutamos isql con el usuario por defecto dba:<code>isql-vt -U dba</code></ul>

- Añadimos todos los archivos que se encuentren en /home/ubuntu, que terminen en ".rdf", al grafo http://genomic-resources.eu/uniprot: <code>SQL&gt; ld_dir('/home/ubuntu','*.rdf','http://genomic-resources.eu/uniprot');</code></ul>

- Ejecutar el trabajo propiamente dicho (este proceso es el que tarda si el dataset es grande): <code>SQL&gt; rdf_loader_run ();</code>.

<strong>Consultas contra el RDF dataset almacenado en Virtuoso</strong>

Si vamos a la IP publica, al SPARQL endpoint (ej. 54.201.244.233:8890/sparql), deberia aparacer un formulario para ejecutar consultas SPARQL. Probamos con: 

<a href="pantaila-argazkia-2014-06-20-164406.png"><img src="pantaila-argazkia-2014-06-20-164406.png?w=300" alt="Pantaila-argazkia 2014-06-20 16:44:06" width="300" height="183" class="alignnone size-medium wp-image-644" /></a>

Deberia dar una larga lista de triples. Happy hacking!



