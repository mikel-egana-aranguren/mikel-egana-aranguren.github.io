---
layout: post
title: "Docker image for SADI-Galaxy"
date: 2015-01-07
---

<h2>About</h2>
<a href="http://sadiframework.org/content/about-sadi/">SADI</a> is a framework to define Semantic Web Services that consume and output <a href="http://www.w3.org/standards/techs/rdf">RDF</a>, and <a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy">SADI-Galaxy</a> makes SADI services available in the popular <a href="http://galaxyproject.org/">Galaxy</a> platform. Thus, SADI-Galaxy is a nice SADI client to invoke SADI services in an environment that Biologists use often.

On the other hand, <a href="http://www.docker.com/whatisdocker/">Docker</a> is a sort of "virtualisation" environment for deploying applications very easily, without configuration. Therefore I have created a Docker image for deploying a Galaxy instance already containing SADI-Galaxy, so anyone interested in SADI-Galaxy can try it out easily within having to configure Galaxy and SADI-Galaxy.
<h2><a id="user-content-deploying-the-container" class="anchor" href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker#deploying-the-container"></a>Deploying the container</h2>
Install Docker and do the thingy for avoiding sudo access:
<pre><code>$ sudo apt-get install docker.io
$ sudo groupadd docker
$ sudo gpasswd -a your_user docker
$ sudo service docker.io restart
</code></pre>
(You might need to log out and back in).

Pull the <a href="https://registry.hub.docker.com/u/mikeleganaaranguren/sadi-galaxy">SADI-Galaxy Docker image</a>:
<pre><code>$ docker pull mikeleganaaranguren/sadi-galaxy
</code></pre>
Check that it has been succesfully pulled:
<pre><code>$  docker images

REPOSITORY                        TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
mikeleganaaranguren/sadi-galaxy   latest              xxxxxxxxxxx        3 days ago          895.8 MB
</code></pre>
Run the container (Make sure that the port 8080 is listening and free in the host machine, or use a different one and map it to the container, e.g. 8389:8080):
<pre><code>$ docker run -d -p 8080:8080 mikeleganaaranguren/sadi-galaxy
</code></pre>
If you go with your web browser to <a href="http://127.0.0.1:8080/">http://127.0.0.1:8080</a> (or the IP of the host machine) there should be a Galaxy server runing. The SADI tools are under <code>SADI services</code>, on the left pane.

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/galaxy_main.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/galaxy_main.png" alt="Galaxy main" /></a>

Login (in the <code>User</code> menu on the top; user:<code>user@user.com</code>, password:<code>useruser</code>) and a history should appear on the right pane.

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/history.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/history.png" alt="Galaxy history" /></a>

In the <code>Workflow</code> menu, there is only one workflow, <code>OpenLifeData2SADI SADI</code>. You can have a look by clicking on the workflow name and then clicking <code>edit</code>:

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/workflow_screen.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/workflow_screen.png" alt="Galaxy workflow" /></a>

Run the workflow.

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/workflow.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/workflow.png" alt="Galaxy workflow" /></a>

Use dataset 1 from the history as input for the workflow (<code>UniProt_IDs.txt</code>).

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/run_workflow.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/run_workflow.png" alt="Galaxy run workflow" /></a>

When the worfklow has finished new steps will appear in the history (20-37).

<a href="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/blob/master/workflow_done.png" target="_blank"><img src="https://github.com/mikel-egana-aranguren/SADI-Galaxy-Docker/raw/master/workflow_done.png" alt="Galaxy workflow done" /></a>

You can use the workflow, by inspecting the steps, to become familiar with SADI-Galaxy.
