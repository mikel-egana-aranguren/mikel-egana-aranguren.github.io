#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re

tree = ET.parse('mikeleganaaranguren039sblog.wordpress.2020-10-02.001.xml')
root = tree.getroot()
channel = root[0]
for item in channel.findall('item'):
    link = item[1].text
    x = re.findall("\d{4}\/\d{2}\/\d{2}", link)
    if x:
        date = x[0].replace("/","-")
        title = item[0].text
        content = item[6].text
        with open(date + "-" + title.replace(" ", "-") + ".md", 'a') as the_file:
            the_file.write('---\n')
            the_file.write('layout: post\n')
            the_file.write('title: \"' + title.encode('utf-8') + '\"\n')
            the_file.write('date: ' + date +  '\n')
            the_file.write('---\n')
            the_file.write('\n')
            the_file.write(content.encode('utf-8'))
            the_file.write('\n')

            



