from flask import Flask
from flask import render_template
from flask import request
from article import summarize_article_at_url
from pdf_gen import generate_pdf_with_data

import json, traceback

app = Flask("News-Summarizer")

@app.route("/")
def index():
    return render_template("index.html", log="")

@app.route("/processURL/")
def test():
    try:
        url = json.loads(request.args["url"])
        return { "status": True, "result": [ summarize_article_at_url(u) for u in url ] }
    except:
        return  { "status": False, "error": traceback.format_exc() }


@app.route('/makePDF/')
def pdf_test():
    data = json.loads(request.args["data"])
    result = generate_pdf_with_data(data)
    if result["status"]:
        return result["content"], 200, {
            'Content-Type': 'application/pdf',
            'Content-Disposition': 'attachment; filename=my_pdf_file.pdf',
        }
    else:
        return { "status": False, "error": traceback.format_exc() }

