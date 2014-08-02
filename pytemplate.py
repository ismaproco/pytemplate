import os,sys,string
from template_builder import TemplateBuilder

#Read the incoming file from the argument
file_name =  ""
destination = ""

# the template argument was sent?
if sys.argv[1] != "":
    file_name = sys.argv[1]

    #the location argument was sent?
    if len(sys.argv) > 2:
    	destination = sys.argv[2]

else:
    print "Remember the first argument is the template file"

#opens the template file
template_file = open(file_name, 'r')
text = string.replace(template_file.read(), " ","")

tb =TemplateBuilder( text, destination )



