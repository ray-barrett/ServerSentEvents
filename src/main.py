import time
import uuid

from flask import Flask, Response, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/basic_example")
def basic_example():
    return render_template("stream1.html")


@app.route("/stream")
def stream():
    def event_stream():
        uid = uuid.uuid4()
        for i in range(30):
            time.sleep(2)
            print(uid, i)
            yield "id: {}\ndata: {:>2}\n\n".format(uid, i)

    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
