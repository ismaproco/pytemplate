import os,sys,string
from template_builder import TemplateBuilder


#Read the incoming file
file_name =  ""
if sys.argv[1] == "":
    file_name = "template.tf"
else:
    file_name = sys.argv[1]

f = open(file_name, 'r')
text = string.replace(f.read(), " ","")

tb =TemplateBuilder(text)



