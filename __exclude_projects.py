#!/usr/bin/env python3

import fnmatch
import re
import xml.etree.ElementTree as ET

with open("exclude_list") as fin:
  exclude_list = set(map(str.strip, fin.readlines()))
  exclude_regex = [re.compile(fnmatch.translate(e)) for e in exclude_list]

parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
tree = ET.parse("default.xml", parser)
root = tree.getroot()

remove_list = list()
for child in root:
  if child.tag == "project":
    for regex in exclude_regex:
      prj_name = child.attrib["name"]
      if regex.match(prj_name):
        remove_list.append(child)

for r in remove_list:
  root.remove(r)

tree.write("default.xml", encoding="utf-8", xml_declaration=True)
