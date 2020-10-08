---
layout: post
title: "Transforming CSV data to RDF with Grafter"
date: 2016-07-08
---

Part of my work is to develop pipelines to transform already existing Open Data (Usually CSVs in some data portal, like CKAN) into RDF and hopefully Linked Data. If I have to do the transformation myself, interactively, I normally use Google Refine with the RDF plugin. However, what I need now is a batch pipeline that I can plug into a bigger Java platform.

Therefore, I'm looking at <a href="http://grafter.org/">Grafter</a>. Even though I have never programmed in Clojure (or any other functional language whatsoever!), Grafter's approach seems very sensible and intuitive. Additionally, I have always wanted to use <a href="https://github.com/phillord/tawny-owl">Tawny-OWL</a>, so probably it will be easier if I learn a bit of Clojure with Grafter first. Coming from Java/Perl/Python, the functional approach felt a bit weird in the beggining, but it actually makes more sense when defining pipelines to process data.

I have gone through the Grafter guide using Leiningen in Ubuntu 14.04. So far so good (I had to install Leiningen manually though, since Ubuntu's Leiningen package was very outdated). In order to run the Grafter example in Eclipse (Mars), or any other Clojure program, one needs to install first the <a href="http://doc.ccw-ide.org/">CounterClockWise</a> plugin. Note that if you want to also use GitHub, like me, there is <a href="https://bugs.eclipse.org/bugs/show_bug.cgi?id=324145">bug</a> that prevents the project from being properly cloned, when you choose the "New project wizard": I cloned with the General project wizard, copied the files from another Grafter project, and surprisingly it worked (trying to convert the project to Leiningen/Clojure didn't work!).

My progress converting data obtained in <a href="http://www.gipuzkoairekia.eus/eu/datu-irekien-katalogoa/-/openDataSearcher/search/true">Gipuzkoa Irekia</a> to RDF can be seen at <a href="https://github.com/mikel-egana-aranguren/demografia">GitHub</a>. Also, I'm aiming at adding <a href="https://www.w3.org/TR/vocab-data-cube/#wf-rules">Data Cube SPARQL constraints</a> as Clojure test, <a href="https://github.com/mikel-egana-aranguren/grafterdatacube">here</a>.

&nbsp;
