from flask import Flask, render_template, request

app = Flask(__name__)

def build_table(n: int, upto: int = 10):
    return [(i, i * n) for i in range(1, upto + 1)]

@app.route("/", methods=["GET", "POST"])
def index():
    number = request.form.get("number", type=int, default=5)
    upto = request.form.get("upto", type=int, default=10)

    # Input validation
    number = max(-10_000, min(10_000, number))
    upto = max(1, min(1000, upto))

    table = build_table(number, upto)
    return render_template("index.html", number=number, upto=upto, table=table)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
