from flask import Flask, request, jsonify
from nlp_pipeline import NLPPipeline

app = Flask(__name__)

pipeline = NLPPipeline()


@app.route("/")
def home():

    return jsonify({
        "service": "NLP Pipeline REST API",
        "status": "running",
        "endpoints": [
            "/preprocess",
            "/entities",
            "/sentiment",
            "/analyze"
        ]
    })


# -----------------------------------
# PREPROCESS API
# -----------------------------------

@app.route("/preprocess", methods=["POST"])
def preprocess():

    data = request.get_json()

    text = data.get("text", "")

    if not text:
        return jsonify({
            "error": "Text is required"
        }), 400

    result = pipeline.preprocess(text)

    return jsonify(result)


# -----------------------------------
# ENTITY API
# -----------------------------------

@app.route("/entities", methods=["POST"])
def entities():

    data = request.get_json()

    text = data.get("text", "")

    if not text:
        return jsonify({
            "error": "Text is required"
        }), 400

    result = pipeline.extract_entities(text)

    return jsonify({
        "entities": result
    })


# -----------------------------------
# SENTIMENT API
# -----------------------------------

@app.route("/sentiment", methods=["POST"])
def sentiment():

    data = request.get_json()

    text = data.get("text", "")

    if not text:
        return jsonify({
            "error": "Text is required"
        }), 400

    result = pipeline.sentiment(text)

    return jsonify(result)


# -----------------------------------
# COMPLETE NLP API
# -----------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    text = data.get("text", "")

    if not text:
        return jsonify({
            "error": "Text is required"
        }), 400

    result = pipeline.analyze(text)

    return jsonify(result)


def start_server():

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )