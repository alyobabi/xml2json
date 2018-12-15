from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import xmljson
app = Flask(__name__)

"""
Server app based on microframework Flask

This app waits for POST request with xml data and
returns this data in json format

"""

@app.route('/')
def index():
	"""
	return hello-message
	"""
	return '<h1>Send POST requset to /xml to transform xml data to json<h1>'
	
@app.route('/xml', methods = ['POST', 'GET'])
def xml2json():
	"""
	Gets POST request, transforms xml data in json with 6 diffrent schemes and 
	return json: {'sheme_name': 'converted data'}
	
	In case of GET request return info message
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify({
			'abdera' : xmljson.abdera.data(req_payload),
			'badgerfish' : xmljson.badgerfish.data(req_payload),
			'cobra' : xmljson.cobra.data(req_payload),
			'gdata' : xmljson.gdata.data(req_payload),			 
			'parker' : xmljson.parker.data(req_payload),
			'yahoo' : xmljson.yahoo.data(req_payload),									 
				  })
	if request.method == 'GET':
		return '<h1>Send xml data on this adres to tranform it to json<h1>'
	return

@app.route('/xml_abdera', methods = ['POST'])
def xml2json_abdera():
	"""
	Gets POST request, transforms xml data in json with abdera sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.abdera.data(req_payload))
	return

@app.route('/xml_badgerfish', methods = ['POST'])
def xml2json_badgerfish():
	"""
	Gets POST request, transforms xml data in json with badgerfish sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.badgerfish.data(req_payload))
	return

@app.route('/xml_cobra', methods = ['POST'])
def xml2json_cobra():
	"""
	Gets POST request, transforms xml data in json with cobra sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.cobra.data(req_payload))
	return

@app.route('/xml_gdata', methods = ['POST'])
def xml2json_gdata():
	"""
	Gets POST request, transforms xml data in json with gdata sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.gdata.data(req_payload))
	return

@app.route('/xml_parker', methods = ['POST'])
def xml2json_parker():
	"""
	Gets POST request, transforms xml data in json with parker sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.parker.data(req_payload))
	return

@app.route('/xml_yahoo', methods = ['POST'])
def xml2json_yahoo():
	"""
	Gets POST request, transforms xml data in json with yahoo sheme and
	return it
	"""
	if request.method == 'POST':
		req_payload = ET.fromstring(request.get_data(as_text = True))
		return jsonify(xmljson.yahoo.data(req_payload))
	return
	
	
app.run(host = '0.0.0.0', port = 80)
