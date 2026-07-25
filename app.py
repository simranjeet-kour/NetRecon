from flask import Flask, render_template, request, send_file
from scanner import scan_target, calculate_risk
from report import generate_report
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    risk = {}
    target = ""
    scan_type = "Quick Scan"

    if request.method == "POST":

        target = request.form["target"]
        scan_type = request.form["scan_type"]

        try:

            results = scan_target(target, scan_type)
            risk = calculate_risk(results)

        except Exception as e:

            results = [{"error": str(e)}]

    return render_template(
        "index.html",
        results=results,
        risk=risk,
        target=target,
        scan_type=scan_type
    )


@app.route("/download", methods=["POST"])
def download():

    target = request.form["target"]
    scan_type = request.form["scan_type"]

    results = scan_target(target, scan_type)
    risk = calculate_risk(results)

    filepath = generate_report(target, scan_type, results, risk)

    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)