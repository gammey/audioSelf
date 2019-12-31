#!/usr/bin/python
import os

runpath=os.path.abspath(__file__).rstrip(os.path.basename(__file__))

def dirlist(dir,type):
	ans = [];
	rdir = runpath+"/source/"+dir;
	if os.path.exists(rdir):
		for i in os.listdir(rdir):
			if i.split(".")[-1] == type:
				ans.append({"file":"/source/"+dir+"/"+i,"type":type})
		return {"success":True,"data":ans};
	else:
		return {"success":False,"reason":"Empty Dir."};

def audioPathList():
	ans  = [];
	rdir = runpath+"/source/";
	for i in os.listdir(rdir):
		if os.path.isdir(rdir+i):
			ans.append(i);
	return ans;

def typeList(dir):
	typelist = [];
	rdir = runpath+"/source/"+dir;
	if os.path.exists(rdir):
		for i in os.listdir(rdir):
			type = i.split(".")[-1];
			if type not in typelist:
				typelist.append(type);
	return typelist;

if __name__ =="__main__":
	print typeList("testaudio")










