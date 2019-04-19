#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import commands
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_test():
	if request.method == 'GET':
        	return "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"\" method =\"post\"><p>What's your num?<input type =\"test\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"
        if request.method == 'POST':
                #!/usr/bin/python
                if request.form['firstname']=="":
                        return "You didn't input anything else!\nRewrite you number please!\n"+"<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"\" method =\"post\"><p>What's your num?<input type =\"test\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"


		if (request.form['firstname']).isdigit() == False:
			return "You put String or negative number!\nplease write your number over 1\n"+"<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"\" method =\"post\"><p>What's your num?<input type =\"test\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"

                n = int(request.form['firstname'])

                ans=1
                f0=0
                f1=1

                for n in range(1,n):
                        ans=f1+f0
                        f0=f1
                        f1=ans

                return "Your num is, "+ str(ans) +"!\n" + "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"\" method =\"post\"><p>What's your num?<input type =\"test\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"
  

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('--listen-port',  type=str, required=True, help='REST service listen port')
        args = parser.parse_args()
        listen_port = args.listen_port
    except Exception, e:
        print('Error: %s' % str(e))

    ipaddr=commands.getoutput("hostname -I").split()[0]
    print "Starting the service with ip_addr="+ipaddr
    app.run(debug=False,host=ipaddr,port=int(listen_port))


