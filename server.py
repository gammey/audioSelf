#!/usr/bin/python
import json
import redis
import os
from flask import Flask, request, make_response
from auth import authToken
from audioList import dirlist

tokenStore = redis.Redis();
runpath=os.path.abspath(__file__).rstrip("server.py")
userfile = runpath+"user.json";



app = Flask(__name__);
@app.route("/auth/token/",methods=["POST","GET"])
def getToken():
	if request.method == "POST":
		dataStr = request.get_data();
		try:
			data = json.loads(dataStr);
		except:
			return json.dumps({"success":False,"reason":"Incorrect Post info."})
		tkmgr = authToken(userfile,tokenStore);
		return json.dumps(tkmgr.createToken(data["username"],data["password"]));
	elif request.method == "GET":
		username = request.headers["USER"];
		token = request.headers["TOKEN"];
		tkmgr = authToken(userfile,tokenStore);
		return json.dumps({"success":tkmgr.legalToken(username,token)});	

@app.route("/source/<path:filename>",methods=["GET"])
def viewStatic(filename):
	if request.headers.has_key("USER") and request.headers.has_key("TOKEN"):
		username = request.headers["USER"];
        	token = request.headers["TOKEN"];
	else:
		try:
			username = request.args.get("USER");
			token = request.args.get("TOKEN");
		except:
			return json.dumps({"success":False,"reason":"Token cannot be not found in your request."})
	if username and token:
		tkmgr = authToken(userfile,tokenStore);
	else:
		return json.dumps({"success":False,"reason":"Token cannot be not found in your request."})
	if tkmgr.legalToken(username,token):
		try:
			static_data = open(runpath+"source/"+filename,"r").read();
		except:
			return json.dumps({"success":False,"reason":"File Not Found"})
		response = make_response(static_data);
		return response;
	else:
		return json.dumps({"success":False,"reason":"inlegal token info."})

@app.route("/resource/list/<string:path>/<string:type>/",methods=["GET"])
def resList(path,type):
	return json.dumps(dirlist(path,type));

#@app.route("/pathtest/<path:tpath>")
#def testpath(tpath):
#	return tpath;



@app.route("/index/<string:page>",methods=["GET"])
def indexStaticPage(page):
	try:
		static_data = open(runpath+"index/"+page).read();
	except:
		return "";
	response = make_response(static_data);
	return response;

if __name__ =="__main__":
	app.run(debug=True,host="0.0.0.0",port="5005");
		
