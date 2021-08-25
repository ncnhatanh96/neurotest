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
	pip install -r requirements.txt

Usage
-----------------
We can use CURL to send HTTP POST request:<br />
	curl -d '{"Address": "put_your_address_here"}' -X POST http://localhost:5000/distance

Document
-----------------
- Turfpy:
	https://turfpy.readthedocs.io/en/latest/
- Flask:
	https://flask.palletsprojects.com/en/2.0.x/
