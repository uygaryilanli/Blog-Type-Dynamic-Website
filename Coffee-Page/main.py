from flask import Flask, render_template, request, redirect, url_for
import csv
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    current_day = datetime.datetime.now().strftime("%d-%m-%Y")
    return render_template("index.html", current_day=current_day)


@app.route("/cafes")
def cafes():
    cafes_data = []
    with open("cafes.csv", mode="r", encoding="utf-8") as files:
        reader = csv.reader(files)
        for row in reader:
            cafes_data.append(row)
    return render_template("cafes.html", cafes_data=cafes_data)


@app.route("/add_cafe", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        cafe_name = request.form.get("cafe_name")
        coffee_quality = request.form.get("coffee_quality")
        wifi_quality = request.form.get("wifi_quality")
        with open("cafes.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([cafe_name, coffee_quality, wifi_quality])
        return redirect(url_for("cafes"))
    else:
        return render_template("add_cafe.html")




if __name__ == "__main__":
    app.run(debug=True)