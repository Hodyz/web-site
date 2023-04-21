from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output.html", methods=["POST"])
def output():
    input_value = request.form.get("input-field")
    return render_template("output.html", input_value=input_value)

if __name__ == "__main__":
    app.run()
