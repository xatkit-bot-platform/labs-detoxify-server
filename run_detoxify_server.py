from flask import Flask, request
from detoxify import Detoxify
import logging

logging.basicConfig(level=logging.INFO)

model_original = 'original'
model_unbiased = 'unbiased'
model_multilingual = 'multilingual'

"""
Set model_name to model_original, model_unbiased or model_multilingual
"""
model_name = model_original

logging.info("Loading " + model_name + " model from Detoxify")
model = Detoxify(model_name)
logging.info(model_name + " model loaded")

app = Flask(__name__)

@app.route('/analyzeRequest', methods=['POST'])
def analyzeRequest():    
    body = request.get_json()
    results = model.predict(body["input"])
    results = {k.upper():str(v) for (k,v) in results.items()}
    return results, 200
