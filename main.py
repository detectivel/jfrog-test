from flask import Flask
from flask_restful import Api, Resource
import os, platform
import subprocess as sub

app = Flask(__name__)
api = Api(app)

ip_list = ['google.com']


def pinger(ip_list):
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            return f"Local network is up and internet is pingable. Ping to '{ip}' was successful"
        else:
            return f"Local network is down and internet isn't pingable. Ping to '{ip}' was unsuccessful"


class SysInfo(Resource):
    def __init__(self):
        pass

    def get(self):
        system = platform.system()
        release = platform.release()
        version = platform.version()
        return f"This is {system} {release} OS. It's version is {version}"


class Pinger(Resource):
    def __init__(self):
        pass

    def get(self):
        for ip in ip_list:
            response = os.popen(f"ping {ip}").read()
            if "Received = 4" in response:
                return f"Local network is up and internet is pingable. Ping to '{ip}' was successful"
            else:
                return f"Local network is down and internet isn't pingable. Ping to '{ip}' was unsuccessful"


api.add_resource(SysInfo, "/sysinfo")
api.add_resource(Pinger, "/pinger")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
