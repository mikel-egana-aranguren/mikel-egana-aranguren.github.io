---
layout: post
title: "Three levels of reproducibility: Docker, Galaxy, Linked Data"
date: 2016-06-23
---

[Originally posted at <a href="https://www.linkedin.com/pulse/three-levels-reproducibility-docker-galaxy-linked-mikel?trk=prof-post">LinkedIn</a>]
<div class="prose">

I have just stumbled upon this thread on why one should use Galaxy (<a href="https://www.biostars.org/p/50034/" target="_blank" rel="nofollow">https://www.biostars.org/p/50034/</a>). One of the reasons posted is reproducibility, but Galaxy only solves one level of reproducibility, "functional reproducibility" (What I did with the data). There is at least two other levels, one "bellow" Galaxy and another one "above" Galaxy:
<ul>
 	<li>Bellow: computational environment: Operating System, library dependencies, binaries.</li>
 	<li>Above: semantics. What the data means.</li>
</ul>
In order to be completely reproducible, one has to be reproducible on the three levels:
<ol>
 	<li>Computational: Docker.</li>
 	<li>Functional: Galaxy.</li>
 	<li>Semantics: URIs, RDF, SPARQL, OWL.</li>
</ol>
And how to do it is described in our GigaScience paper, "Enhanced reproducibility of SADI Web Service Worfkflows with Galaxy and Docker" :-) (<a href="http://www.gigasciencejournal.com/content/4/1/59" target="_blank" rel="nofollow">http://www.gigasciencejournal.com/content/4/1/59</a>)

</div>
<div id="floating-share-button">Just to emphasize and clarify, the 3 levels would be:</div>
<div></div>
<div>3.- Semantics: what the data means.</div>
<div>2.- Functional: what I did with the data.</div>
<div>1.- Computational: how I did it.</div>
<div class="article-content-footer"></div>
