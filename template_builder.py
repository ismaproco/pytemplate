import os,sys,string
from path_tree import PathTree

#Main class to build the template
class TemplateBuilder:
    
    """docstring for PyTemplate"""
    def __init__(self, text):
        
        self.text = text

        # Variable initilization for the file parsing
        word_dictionary = []
        word = ""
        path = []

        #flag to know when to break the word
        break_word = False

        #Tokens to split the file
        open_tokens = ['[','{','(']
        close_tokens = [']','}',')']
        general_tokens = [',','/','\\','\n','\t']

        
        #states
        #s -> none, folder, file, end_token
        type_state = []

        reading_token = False

        identifier = 0
        temp_state_identifier = ""
        
        pop_folder = False

        # loop through the text
        for c in self.text:

            # The chatacter is a Token?
            if  general_tokens.count(c) > 0 or open_tokens.count(c) > 0 or close_tokens.count(c) > 0:
                reading_token = True
                break_word = True
            else:
                reading_token = False

            # is a word to add?
            if break_word:
                # is not empty?
                if word != "":

                    f = PathTree()
                    
                    # set the values of the PathTree object
                    f.identifier = identifier
                    f.name = word
                    f.creation_type = type_state[-1]
                    f.Father = None

                    # append the object to the dictionary of words                 
                    word_dictionary.append(f)

                    # is a folder?
                    if type_state[-1] == "folder":
                        if(len(type_state) == len(path)):
                            path.pop()
                        #add the current word to the path array
                        path.append(word)

                    #build the path for the Path Tree file
                    f.path = self.build_path(path)

                    # is a file
                    if type_state[-1] == "file":
                        #add the word to the path string
                        f.path += word

                    #clear the word
                    word = ""

                    #increment the identifier
                    identifier += 1

            # Check the open tokens
            if c == "[":
                type_state.append("folder")
            elif c == "{":
                type_state.append("file")

            # Check the closing tokens
            if c == "]":
                type_state.pop()
                path.pop()
            elif c == "}":
                type_state.pop()

            # is not a breaking token, add char to the string
            if not reading_token and type_state[-1] != "none":
                word += c
            
            #clear the current status
            reading_token = False
            break_word = False

        # loop all the words
        for f in word_dictionary:
            #is a folder?
            if f.creation_type == "folder":
                final_path = os.path.dirname(os.path.abspath(__file__)) +"\\"+ f.path
                if not os.path.exists(f.path):os.makedirs(final_path)
            #is a file?
            if f.creation_type == "file":
                open(f.path,"w+")

    """ Return a string of the templating object """
    def __str__(self):
        return str(self.identifier) + " " + self.creation_type + " " + self.name + " " + self.path

    """ Return a string of the path array """
    def build_path(self,path):
        s_path = ""
        for i in path:
            s_path += i + "\\"
        return s_path