from flask import Flask, render_template
import datetime
from csv_handler import csv_reader


app = Flask(__name__)


@app.route('/')
def home():
    lucky_users = csv_reader()
    today = datetime.datetime.now().strftime("%A" ", " "%B" " " "%Y")
    return render_template("index.html",
                           today=today,
                           lucky_users=lucky_users,
                           len = len(lucky_users))


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0")