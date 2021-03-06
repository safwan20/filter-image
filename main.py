from flask import Flask, render_template, request, jsonify
from mean import mean_color, mean_library
from gaussian import gaussian_color, gaussian_library
from median import median_color, median_library
from sobe import sobe_filter
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET','POST'])
def home() :
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process() :
	if request.method == 'POST' :
		logging.debug("WELCOME !!!!!!!!!!!!!!!!!")
		filtr = request.form["filter"]
		image = request.files['file']
		filename =  image.filename
		folder_name = 'Images/' + filename
		image.save(folder_name)

		if filtr == "mean" :
			logging.debug("MEAN FILTER")
			save_file = mean_library(folder_name)
		elif filtr == "gaussian" :
			logging.debug("GAUSSIAN FILTER")
			save_file = gaussian_library(folder_name)
		elif filtr == "median" :
			logging.debug("MEDIAN FILTER")
			save_file = median_library(folder_name)
		else :
			logging.debug("SOBEL FILTER")
			save_file = sobe_filter(folder_name)
		return jsonify({'filename' : save_file})
	return "Hello"