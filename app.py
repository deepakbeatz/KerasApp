from bottle import get,post,route,run,template,TEMPLATE_PATH,request,redirect,static_file
import os
import math
import numpy as np

TEMPLATE_PATH.insert(0,"./views")
root=os.getcwd()

#----------------------------------------------------------------------
#DATABASE CONNECTIVITY
#----------------------------------------------------------------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#----------------------------------------------------------------------
#ROUTES
#----------------------------------------------------------------------

@route('/static/<filepath:path>')
def serve_static(filepath):
    myroot=os.path.join(root,"static")
    return static_file(filepath,root=myroot)

#----------------------------------------------------------------------
#SERVER
#----------------------------------------------------------------------	
run(host="localhost",port=8997,debug=True)

