import os,sys,string

file_name =  ""
if sys.argv[1] == "":
    file_name = "template.tf"
else:
    file_name = sys.argv[1]

path = []

def build_path():
    s_path = ""
    for i in path:
        s_path += i + "\\"
    return s_path

type_state = []

def manage_state(word,operation):
    if operation == "append":
        type_state.append(word)
    elif (operation == "pop"):
        type_state.pop()

class f_tree:
    identifier = 0
    level = 0
    name = ""
    creation_type = ""
    path = ""
    father = None

    def __str__(self):
        return str(self.identifier) + " " + self.creation_type + " " + self.name + " " + self.path

f = open(file_name, 'r')

text = string.replace(f.read(), " ","")

word_dictionary = []
word = ""

open_tokens = ['[','{','(']
close_tokens = [']','}',')']
general_tokens = [',','/','\\','\n','\t']

break_word = False
#states
#s -> none, folder, file, end_token

reading_token = False

identifier = 0
temp_state_identifier = ""
pop_folder = False

for c in text:

    if general_tokens.count(c) > 0 or open_tokens.count(c) > 0 or close_tokens.count(c) > 0:
        reading_token = True
        break_word = True
    else:
        reading_token = False

    if break_word:
        if word != "":
            f = f_tree()
            f.identifier = identifier
            f.name = word
            f.creation_type = type_state[-1]

            f.Father = None
            
            word_dictionary.append(f)

            if type_state[-1] == "folder":
                if(len(type_state) == len(path)):
                    path.pop()
                path.append(word)

            f.path = build_path()
            if type_state[-1] == "file":
                f.path += word

            word = ""
            identifier += 1

    if c == "[":
        type_state.append("folder")
    elif c == "{":
        type_state.append("file")

    if c == "]":

        type_state.pop()
        path.pop()

    elif c == "}":

        type_state.pop()

    if not reading_token and type_state[-1] != "none":
        word += c
    
    reading_token = False
    break_word = False

for f in word_dictionary:
    if f.creation_type == "folder":
        final_path = os.path.dirname(os.path.abspath(__file__)) +"\\"+ f.path
        if not os.path.exists(f.path):os.makedirs(final_path)
    if f.creation_type == "file":
        open(f.path,"w+")
