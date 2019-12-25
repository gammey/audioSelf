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


#if __name__ =="__main__":
#	print dirlist("testaudio","ogg")










