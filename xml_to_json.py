# -*- coding: utf-8 -*-
import json
import xmltodict
import os



def read_text_from_file(file_path):

    with open(file_path, encoding='utf8') as f:
        text = f.read()
        return text
def write_to_file(text, file_path):

    with open(file_path, 'wb') as f:
        f.write(text.encode('utf8', 'ignore'))
        
        
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
path='C:/Users/siddh/OneDrive/Desktop/pills-object-detection-master/pills-object-detection-master/images/test/anno/'
dir_list=os.listdir(path)

for x in dir_list:
    with open(path+x,encoding='utf8') as xml_file:
     
        data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
        json_data = json.dumps(data_dict)

    # Write the json data to output
    # json file
        with open('C:/Users/siddh/OneDrive/Desktop/pills-object-detection-master/pills-object-detection-master/images/test/anno_json/'+x+".json","w") as json_file:
            json_file.write(json_data)
        # json_file.close()