import json


class JSONEditor:


    def __init__(self, jsonFilePath):

        '''Constructor'''

        self.file = jsonFilePath

        with open(jsonFilePath, "r+") as fp:

            texts = fp.read()

            try:

                json.loads(texts)
            
            except json.decoder.JSONDecodeError:

                self.__clear_and_write({})



    def read(self)->dict:

        '''Read Datas of the json file.'''

        with open(self.file,"r") as fp:

            try:

                return json.loads(fp.read())

            except json.decoder.JSONDecodeError:

                return {}
        

    def __clear_and_write(self, dictionary:dict):

        '''Private method for other functionalities. If you are core developer change the source code and make it public but it can make it unusable'''

        with open(self.file,"w") as fp:

            fp.write(json.dumps(dictionary))


    def add_items(self, dictionary:dict):

        '''Add key and value'''

        new_dict = self.read()

        for key,value in dictionary.items():

            new_dict[key] = value

        self.__clear_and_write(new_dict)


    def remove_items(self, keys:list):

        '''Remove key and value'''

        newdict = self.read()

        for key in keys:

            newdict.pop(key)

        self.__clear_and_write(newdict)


    def set_value(self,key,value):

        '''Set value of a key.'''

        self.remove_items([key])

        self.add_items({key:value})


    def get_value(self, key):

        '''Get value of a key.'''

        return self.read()[key]

    
    def flush(self):
        
        '''Empty the json database.'''

        self.__clear_and_write({})




editor = JSONEditor("test.json")

print(editor.read())


editor.add_items({"shuddho":"100","seyam":"200"})

print(editor.read())


editor.remove_items(["shuddho"])

print(editor.read())


print(editor.get_value("seyam"))


editor.set_value("seyam",editor.get_value("seyam")+"00")

print(editor.read())


# To clear a json file use flush method.

editor.flush()

print(editor.read())







        

