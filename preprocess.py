from datetime import datetime
from os import error
from urllib import request

import subprocess

import csv

import pandas as pd

import ast

import time

# import the PostgreSQL adapter for Python

import psycopg2

from psycopg2 import sql

start_time = time.time()


# Section 1
# Downloading the latest weather file from https://dd.weather.gc.ca/nowcasting/matrices


now = str(datetime.utcnow())

month = now[5:7]
day = now[8:10]
hour = now[11:13]

url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')

local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])

print(local_file)

try:
    request.urlretrieve(url, local_file)

except error:
    
    # Error checks for hours 
    
    if int(hour) > 1 and int(hour) <= 23:
        
        hour = str("0" + str(int(hour) - 1))
        if len(hour) == 3:
            hour = hour[1:]
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)
        
            
    elif int(hour) == 0:
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    elif int(hour) == 1:
        hour = "00"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    # Month error checks

    # January
    elif (int(month) == 1 and int(day) == 1 and int(hour) == 0):
        month = "12"
        day = "31"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    # March
    elif (int(month) == 3 and int(day) == 1 and int(hour) == 0):
        month = "02"
        day = "28"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)


    # April, June, and September
    elif (int(month) == 4 and int(day) == 1 and int(hour) == 0 
    or int(month) == 6 and int(day) == 1 and int(hour) == 0
    or int(month) == 9 and int(day) == 1 and int(hour) == 0):
        month = str("0" + str(int(month) - 1))
        day = "31"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    # August
    elif (int(month) == 8 and int(day) == 1 and int(hour) == 0):
        month = "07"
        day = "31"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)


    # November
    elif (int(month) == 11 and int(day) == 1 and int(hour) == 0):
        month = "10"
        day = "31"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    # December
    elif (int(month) == 12 and int(day) == 1 and int(hour) == 0):
        month = "11"
        day = "30"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)


     
    elif (int(month) == 5 and int(day) == 1 and int(hour) == 0
    or int(month) == 7 and int(day) == 1 and int(hour) == 0 
     
    or int(month) == 10 and int(day) == 1 and int(hour) == 0):
        month = str(str(int(month) - 1))
        day = "30"
        hour = "23"
        url = str('https://dd.weather.gc.ca/nowcasting/matrices/SCRIBE.NWCSTG.' + month + '.' + day + '.' + hour + 'Z.n.Z')
        local_file = str('C:\CollaborativeProject\output\\results\\' + url[45:])
        request.urlretrieve(url, local_file)

    

    



# Section 2
# Unzipping and renaming the weather file into a txt file

# creating variables to add into the command line code using string manipulation
unzipped = str('"' + local_file.replace(".Z", "") + '"')
txt_file = local_file.replace("n.Z", "txt")
print(txt_file)
txt_file = txt_file[39:]
print(txt_file)
txt_file = str('"' + txt_file + '"')
print(txt_file)
# setting up a command line code to unzip files using 7zip
# the output file path will need to be congifured
one = str('7z e ' + local_file + ' -oC:\CollaborativeProject\output\\results')

# setting up a command line code to rename the unzipped file into a txt file
two = str('rename ' + unzipped + " " + txt_file)
print(two)
subprocess.run(one, shell=True)
subprocess.run(two, shell=True)

# example of what the above command line code would look like
# subprocess.run('7z e C:\CollaborativeProject\output\SCRIBE.NWCSTG.05.22.03Z.n.Z  -oC:\CollaborativeProject\output', shell=True)
# subprocess.run('rename "C:\CollaborativeProject\output\SCRIBE.NWCSTG.05.22.03Z.n" "SCRIBE.NWCSTG.05.22.03Z.txt"', shell=True)

# Section 3
# Reading the text file and writing the contents to a new file

# csv to list: https://www.codespeedy.com/csv-to-list-in-python/



with open('on_stn_codes.csv') as stn:
    reader = csv.reader(stn)
    my_list = list(reader)


my_list[0] = ['CYAM']

list2 = str(my_list).replace("[",'').replace("'",'').replace("]",'')


list3 = [i[0] for i in my_list]

list4 = [" " + i for i in list3 if len(i) == 3]
list5 = [i for i in list3 if len(i) == 4]    

list4.extend(list5)


count = 0

txt_file2 = str('C:\CollaborativeProject\output\\results\\' + txt_file.replace('"',""))

print(txt_file2)


# Connect to the PostgreSQL database server

postgresConnection = psycopg2.connect("dbname=ontario_weather user=postgres password='postgres'")

# Get cursor object from the database connection

cursor = postgresConnection.cursor()
print(txt_file)
name_Table = txt_file.replace(".txt", "").replace(".", "")
print(name_Table)
# Create table statement

sqlCreateTable = "create table "+name_Table+" (STN VARCHAR(4), DATE VARCHAR(8), HOUR VARCHAR(4), TEMP FLOAT, WIND FLOAT, GEOM GEOMETRY(Point, 4326));"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTable)


with open(txt_file2, "r") as file:  
    
    for line in file:

        try:
            if line[5:9] in list4:
                count += 1
                for x in range(26):
                    next(file)
                current = file.readline()
                #sqlInsert = ("INSERT INTO "+name_Table+" (STN, DATE, HOUR, TEMP, WIND) VALUES ("+(line[5:9])+", "+current[0:8]+", "+current[9:13]+", "+current[65:70].replace(" ", "")+", "+current[81:84].replace(" ", "")+")").format()
                sqlInsert = sql.SQL("INSERT INTO {name} (STN, DATE, HOUR, TEMP, WIND) VALUES({one}, {two}, {three}, {four}, {five})".format(
                    name = name_Table, one = ("'"+(line[5:9].replace(" ", ""))+"'"), 
                two = (current[0:8]), three = (current[9:13]), four = (current[65:70].replace(" ", "")), 
                five= (current[81:84].replace(" ", ""))))

                cursor.execute(sqlInsert)
                
        except IndexError:
            for x in range(30):
                next(file)


sqlAlter = "UPDATE "+name_Table+" SET GEOM = ST_SetSRID(ST_MakePoint(ws.lon, ws.lat), 4326) FROM ws WHERE ws.id = "+name_Table+".stn;"

cursor.execute(sqlAlter)

postgresConnection.commit()


weather_file = txt_file2.replace(".txt", ".csv")

#txt_file2 = txt_file.replace('"',"")
weather_file = weather_file.replace('"',"")


header = ['STN', 'DATE','HR', 'TEMP', 'WIND', 'Y', 'X']

df = pd.read_csv('latlon.csv')

first_column = df[df.columns[0]]
second_column = df[df.columns[1]]
print(first_column)
print(second_column)

count = 0

with open(txt_file2, "r") as file, open(weather_file, "w", encoding='UTF8', newline='') as new_file:  
    
    writer = csv.writer(new_file)
    writer.writerow(header)
    
    for line in file:

        try:
            if line[5:9] in list4:
                
                for x in range(26):
                    
                    next(file)
                
                current = file.readline()
                
                writer.writerow([line[5:9], current[0:8], current[9:13], ast.literal_eval(current[65:70].replace(" ", "")), 
                ast.literal_eval(current[81:84].replace(" ", "")), first_column[count], second_column[count]])

                # writer.writerow([line[5:9], current[0:8], current[9:13], 
                # first_column[count], second_column[count]])
                
                count += 1

        except IndexError:
            for x in range(30):
                next(file)



import sys
from qgis.core import *


# Supply path to qgis install location
QgsApplication.setPrefixPath("'C:/OSGEO4~1/apps/qgis'", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

sys.path.append(r'C:\OSGeo4W64\apps\qgis\python\plugins')

import processing
from processing.core.Processing import Processing
Processing.initialize()



l = weather_file

output = l.replace(".csv", ".gpkg")
print(output)

# Create points layer from table
alg_params = {
    'INPUT': l,
    'MFIELD': '',
    'OUTPUT': output,
    'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
    'XFIELD': 'X',
    'YFIELD': 'Y',
    'ZFIELD': '',
    'OUTPUT': output
}

processing.run('native:createpointslayerfromtable', alg_params)


layer=QgsVectorLayer(output)

from PyQt5.QtCore import QVariant

layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField("T",QVariant.Double)])
layer_provider.addAttributes([QgsField("W",QVariant.Double)])
layer.updateFields()
print(layer.fields().names())


expression1 = QgsExpression('"TEMP"')
expression2 = QgsExpression('"WIND"')

context = QgsExpressionContext()
context.appendScopes(\
QgsExpressionContextUtils.globalProjectLayerScopes(layer))



with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['T'] = expression1.evaluate(context)
        f['W'] = expression2.evaluate(context)
        layer.updateFeature(f)
    
raster = output.replace(".gpkg", ".tif")    

param = { 'DISTANCE_COEFFICIENT' : 4,
 'EXTENT' : '-95.154825942,-74.343495817,41.681435425,56.859036233 [EPSG:4326]', 
 'INTERPOLATION_DATA' : str(output + '|layername=SCRIBE::~::0::~::8::~::0'),
 'OUTPUT' : raster, 'PIXEL_SIZE' : 0.1 }


processing.run("qgis:idwinterpolation", param)


# { 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : True, 'DATA_TYPE' : 0, 
# 'EXTRA' : '', 
# 'INPUT' : 'C:/CollaborativeProject/output/SCRIBE.NWCSTG.06.06.17Z.tif', 
# 'KEEP_RESOLUTION' : False, 'MASK' : 'C:/CollaborativeProject/ontario.gpkg|layername=ontario', 
# 'MULTITHREADING' : False, 
# 'NODATA' : None, 
# 'OPTIONS' : '', 
# 'OUTPUT' : 'C:/CollaborativeProject/output/clip_test.tif', 
# 'SET_RESOLUTION' : False, 'SOURCE_CRS' : QgsCoordinateReferenceSystem('EPSG:4326'), 
# 'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:4326'), 
# 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None }



qgs.exitQgis()



print("--- %s seconds ---" % (time.time() - start_time))