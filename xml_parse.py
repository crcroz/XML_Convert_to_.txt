import xml.etree.ElementTree as ET
import os
import os.path

'''This is the path to the folder containing all the xml files'''
directory = r"/Users/connorcrozier/Downloads/permissionsets"

'''iterate through xml files'''
for filename in os.listdir(directory):

    '''get xml file path here to get root'''
    mytree = ET.parse(f"/Users/connorcrozier/Downloads/permissionsets/{filename}")
    myroot = mytree.getroot()

    '''creates the title and creates the txt file'''
    f = open(f"{filename[:-3] + 'txt'}", "w")

    x = 0
    while True:

        mylist = []
        fieldlist = []
        keyslist = []

        '''Loop gets the field and key and adds it to list/cuts out root from element tag'''
        for elements in myroot[x]:
            mylist.append(elements.tag.split('}',1)[1] + " : " + elements.text)


        '''rearranges the sets so that fields is capatalized and first'''
        for sets in mylist:

            if sets[0] == 'f': 
                fieldlist.append(sets.upper())
            else:
                keyslist.append(sets)

        '''prints the final and ordered list'''
        printlist = fieldlist + keyslist
        for i in printlist:
            f.write("\n" + "\n" + i)

        '''For spacing'''
        f.write("\n" + "\n" + '------------------------------')    

        x += 1
        if x == len(myroot):
            f.close()
            break





