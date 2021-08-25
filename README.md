Neuro Test
=====================================

Table of Contents
-----------------

* [Introduction](#introduction)
* [Usage](#usage)
* [Requirement](#Requirement)
* [Reference](#reference)


Introduction
-----------------
This flask app is created for interview purpose.
It will receive location address through HTTP request and calculate distance between MKAD and that address.

Setup
-----------------
Please install requirement: <br />
```javascript
pip install -r requirements.txt
```

Usage
-----------------
```javascript
cd app/ && export FLASK_APP=__init__.py
flask run
```
We can use CURL to send HTTP POST request:<br />
```javascript
curl -d '{"Address": "put_your_address_here"}' -X POST http://localhost:5000/distance
```
Example
-----------------
```javascript
2450 $ curl -d '{"Address": "Ha Noi"}' -X POST http://localhost:5000/distance

6719.920575539681Km
2451 $ curl -d '{"Address": "MKAD"}' -X POST http://localhost:5000/distance                                                                                               
This address is located in the MKAD area
```

Document
-----------------
- Turfpy:
	https://turfpy.readthedocs.io/en/latest/
- Flask:
	https://flask.palletsprojects.com/en/2.0.x/
