import xml.etree.ElementTree as ET
import os

'''This is the path to the folder containing all the xml files'''
directory = r"Your path to XML FOLDER GOES HERE"

fieldnames = []

'''iterate through xml files'''
for filename in os.listdir(directory):

    '''get xml file path here to get root'''
    mytree = ET.parse(f"Your path to XML FOLDERE GOES HERE/{filename}")
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
                fieldnames.append(sets)
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

'''Create document with most used fields and number of uses'''
myset = set()
for x in fieldnames:
    if fieldnames.count(x) > 5:
        myset.add(x + f"      Number of times used: {fieldnames.count(x)}")

'''creates the title and creates the txt file'''
f = open("duplicates.txt", "w")

for y in myset:
    f.write("\n" + "\n" + y)
    f.write("\n" + '------------------------------')

f.close()





