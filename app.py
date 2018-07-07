#!/usr/bin/python

from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)
myJsonData = json.loads(open('./foot.json').read())


footAData = myJsonData["footA"]
footBData = myJsonData["footB"]

@app.route("/footA", methods=['GET'])
def get_footA():
	footAList = []
	for element in footAData:
		footAList.append(element)
	return render_template("footA.html", display_data=footAList)

@app.route("/footB", methods=['GET'])
def get_footB():
	footBList = []
	for element in footBData:
		footBList.append(element)
	return render_template("footB.html", display_data=footBList)

@app.route("/footA/<String:Time>/", methods=['GET'])
def get_footA_time(time):
	myyrlist = []
	for element in footAData:
		if element["Time"] == Time:
			myyrlist.append(element)
	return render_template("footA.html", display_data=myyrlist)

@app.route("/footB/<String:Time>/", methods=['GET'])
def get_footB_time(time):
	myyrlist = []
	for element in footBData:
		if element["Time"] == Time:
			myyrlist.append(element)
	return render_template("footB.html", display_data=myyrlist)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
