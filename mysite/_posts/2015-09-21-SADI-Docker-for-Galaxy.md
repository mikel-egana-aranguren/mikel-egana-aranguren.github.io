---
layout: post
title: "SADI-Docker for Galaxy"
date: 2015-09-21
---

<h2>About</h2>
<a href="http://sadiframework.org/content/about-sadi/">SADI</a> is a framework to define Semantic Web Services that consume and produce <a href="http://www.w3.org/standards/techs/rdf">RDF</a>. On the other hand, <a href="http://www.docker.com/whatisdocker/">Docker</a> is a container-based virtualisation environment for deploying applications very easily, without configuration or installation of dependencies. Therefore I have created SADI-Docker, a Docker image containing all the necessary programs and dependencies to invoke SADI services: Galaxy tool-files are also provided to execute such programs as regular Galaxy tools. Therefore, SADI can be used within Galaxy with a minimal installation (only the Docker image and the Galaxy XML files, see bellow). Even more, the SADI-Docker image can be used as a regular Docker image, runing it as a standalone Operating System pre-configured to invoke SADI services.
<h2>Installation</h2>
Install Docker and do the thingy for avoiding sudo access:
<pre> $ sudo apt-get install docker.io
 $ sudo groupadd docker
 $ sudo gpasswd -a your_user docker
 $ sudo service docker.io restart
</pre>
(You might need to log out and back in, and also I had to install apparmor).

Pull the <a href="https://hub.docker.com/r/mikeleganaaranguren/sadi/">SADI-Docker</a> image to your Docker repository:
<pre> $ docker pull mikeleganaaranguren/sadi:v6
</pre>
Check that it has been succesfully pulled:
<pre> $ docker images</pre>
<pre>REPOSITORY TAG IMAGE ID CREATED VIRTUAL SIZE
 mikeleganaaranguren/sadi v6 0bb03066587d 46 hours ago 580.3 MB
</pre>
Download/clone the latest Galaxy version:
<pre> $ git clone https://github.com/galaxyproject/galaxy.git
</pre>
Download/clone this repository and copy the `tools/SADI-Docker` directory to the `tools` directory in your Galaxy installation. You can also install the Galaxy tools from within your Galaxy instance as regular Galaxy tools from the<a href="https://toolshed.g2.bx.psu.edu/view/mikel-egana-aranguren/sadi_docker/54c48f9ca32b"> Galaxy tool shed</a>. There are five Galaxy tools:
<ul>
	<li>SADI-Docker-sadi_client: a SADI client for synchronous SADI services.</li>
	<li>SADI-Docker-RDFSyntaxConverter: a tool to convert between different RDF syntaxes, including from RDF to TSV files.</li>
	<li>SADI-Docker-mergeRDFgraphs: a tool to merge different RDF graphs into one.</li>
	<li>SADI-Docker-SPARQLGalaxy: a tool to perform SPARQL queries against RDF files.</li>
	<li>SADI-Docker-rapper: a tool to convert RDF files to different syntaxes.SADI-Docker-tab2rdf: a tool to produce RDF files from TSV files.</li>
</ul>
Add the following section to `config/tool_conf.xml` to add the tools to Galaxy (first copy `tool_conf.xml.sample` to `tool_conf.xml`):

<a href="https://mikeleganaaranguren.files.wordpress.com/2015/09/sadi-docker-1.png"><img class="alignnone  wp-image-738" src="https://mikeleganaaranguren.files.wordpress.com/2015/09/sadi-docker-1.png?w=300" alt="SADI-docker-1" width="490" height="147" /></a>

Change the Galaxy configuration so that it can run Docker images as if they were regular tools installed in your system. Add a destination, `docker_local`, to your configuration, and make it the default. Copy `config/job_conf.xml.sample_basic` to `config/job_conf.xml` and add these lines to `config/job_conf.xml` (change `docker_memory` if necessary):

<a href="https://mikeleganaaranguren.files.wordpress.com/2015/09/sadsi-docker_2.png"><img class="alignnone  wp-image-737" src="https://mikeleganaaranguren.files.wordpress.com/2015/09/sadsi-docker_2.png?w=300" alt="SADSI-docker_2" width="489" height="225" /></a>

(look at `job_conf.xml.sample_advanced` for more options regarding how Galaxy invokes Docker containers, since there are a lot of options).

Run Galaxy and the tools should appear under `Docker SADI services`:

<a href="https://mikeleganaaranguren.files.wordpress.com/2015/09/tools.png"><img class="alignnone  wp-image-740" src="https://mikeleganaaranguren.files.wordpress.com/2015/09/tools.png?w=300" alt="tools" width="481" height="438" /></a>
<h2>Use case</h2>
In order to test the installation, you can run a pre-defined workflow. Upload the file workflow/UniProt_IDs.txt, to your current Galaxy history. Then you can import the workflow in Galaxy (Workflows; Import or Upload Workflow; choose file workflow/SADI-Docker_use_case.ga). You can also find the workflow at the <a href="http://toolshed.g2.bx.psu.edu/view/mikel-egana-aranguren/sadi_docker_workflow/22be3a551998">tool shed</a>. Then run the workflow, choosing the UniProt_IDs.txt dataset as input for the first step.

The workflow answers the following question: Given a set of UniProt proteins, which ones are related to PubMed abstracts containing the term ``brain'', and what are they KEGG entries? The workflow starts from a simple list of UniProt identifiers, and retrieves different datasets from a regular SADI service (to obtain KEGG entries) and a set of 3 OpenLifeData2SADI services (to obtain PubMed abstracts). The results are then merged and queried to obtain the KEGG entries of proteins that are related to PubMed abstracts that contain the term.

<a href="https://mikeleganaaranguren.files.wordpress.com/2015/09/workflow.png"><img class="alignnone  wp-image-739" src="https://mikeleganaaranguren.files.wordpress.com/2015/09/workflow.png?w=300" alt="workflow" width="491" height="267" /></a>

The SADI services used in the workflow are:
<ul>
	<li>http://sadiframework.org/services/getKEGGIDFromUniProt</li>
	<li>http://biordf.org/cgi-bin/SADI/OpenLifeData2SADI/SADI/hgnc/uniprot_vocabulary_Resource_hgnc_vocabulary_x-uniprot-inverse_hgnc_vocabulary_Resource</li>
	<li>http://biordf.org/cgi-bin/SADI/OpenLifeData2SADI/SADI/hgnc/hgnc_vocabulary_Resource_hgnc_vocabulary_x-omim_omim_vocabulary_Gene</li>
	<li>http://biordf.org/cgi-bin/SADI/OpenLifeData2SADI/SADI/omim/omim_vocabulary_Gene_omim_vocabulary_article_pubmed_vocabulary_PubMedRecord</li>
</ul>
And the SPARQL query to obtain the result:
<pre>
 PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
 PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
 PREFIX sadi: &lt;http://sadiframework.org/ontologies/predicates.owl#&gt;
 PREFIX lsrn: &lt;http://purl.oclc.org/SADI/LSRN/&gt;</pre>
<pre>SELECT ?protein ?label ?KEGG
 WHERE {
 ?protein rdf:type lsrn:UniProt_Record .
 ?protein sadi:isEncodedBy ?KEGG .
 ?protein ?prot2hgnc ?hgnc .
 ?hgnc ?hgnc2omim ?omim .
 ?omim ?omim2pubmed ?pubmed .
 ?pubmed rdfs:label ?label .
 FILTER (regex (?label, 'brain'))
 }
</pre>
<h2>Notes</h2>
This project is a continuation of <a href="http://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker">SADI-Galaxy-Docker</a>, with the inverse approach, hence the name: SADI-Galaxy-Docker was a complete Galaxy server, configured with SADI tools, within a Docker image; SADI-Docker is a Docker image with only SADI tools, and any Galaxy instance can invoke the image.

Tab2rdf is a "fork" of the tool <a href="http://toolshed.g2.bx.psu.edu/view/sem4j/sparql_tools">tab2rdf</a>. This version adds option for the user to define no base URI, i.e. all the entities of the tab file have their own URI.

When using the SADI client on its own, the input dataset's datatypes must be edited, stating that the input is an RDF file.

The docker image can also be built without pulling it, using the Dockerfile:
<pre>
 FROM ubuntu:14.04
 MAINTAINER Mikel Egaña Aranguren &lt;mikel.egana.aranguren@gmail.com&gt;</pre>
<pre># Install the necessary stuff with apt-get</pre>
<pre>RUN apt-get update &amp;&amp; apt-get install -y wget python python-setuptools raptor2-utils libraptor2-0</pre>
<pre># apt-get install python-rdflib is not working so use easy_install instead</pre>
<pre>RUN easy_install rdflib</pre>
<pre># SADI does not like OpenJDK so install Java from http://www.duinsoft.nl/packages.php?t=en</pre>
<pre>RUN wget http://www.duinsoft.nl/pkg/pool/all/update-sun-jre.bin
 RUN sh update-sun-jre.bin</pre>
<pre>RUN mkdir /sadi
 COPY sadi_client.jar /sadi/
 COPY RDFSyntaxConverter.jar /sadi/
 COPY __init__.py /sadi/
 COPY MergeRDFGraphs.py /sadi/
 COPY tab2rdf.py /sadi/
 COPY sparql.py /sadi/
 RUN chmod a+x /sadi/*
 ENV PATH $PATH:/sadi
</pre>
