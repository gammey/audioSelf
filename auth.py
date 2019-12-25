#!/usr/bin/python
import redis
import json
import random,string

tokenExpire=24*60*60;
def genRandomString(slen=16):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))


class authToken:
  def __init__(self,userfile,rediscon):
	f = open(userfile,"r");
	self.userinfo = json.loads(f.read());
	self.tokenStore = rediscon;
  def legalUser(self,username,password):
	userinfo = {"username":username,"password":password};
	if userinfo in self.userinfo:
		return True;
	else:
		return False;
  def createToken(self,username,password):
	if self.legalUser(username,password):
		keyName = "token_"+username;
		tokenStr = genRandomString()
		self.tokenStore.set(keyName,tokenStr);
		self.tokenStore.expire(keyName,tokenExpire)
		return {"success":True,"data":{"key":keyName,"token":tokenStr,"expire":tokenExpire}}
	else:
		return {"success":False,"data":{"reason":"Username or Password incorrect."}}
  def legalToken(self,username,token):
	tokenKey = "token_"+username;
	stoken = self.tokenStore.get(tokenKey);
	if stoken == token:
		return True;
	else:
		return False;

