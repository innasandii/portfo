import os

from flask import Flask, render_template, request, redirect
import csv
# To run: flask --app server run --debug

app = Flask(__name__)
print(__name__)

# flask make our strings as html
# @app.route("/")
# def hello_world():
#     return "<p>Hello, Inna!</p>"

# TO PROVIDE OUR OWN HTML
@app.route("/")
def my_home_fync():
    return render_template("./index.html")  # html file should be in templates folder!

@app.route("/<string:page_name>")  # not to write the same code for different pages
def html_page(page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_data_to_file(data)
            write_to_csv(data)

            return redirect("/thankyou.html")
        except:
            return "error text 9submit form)"
    else:
        return "Something went wrong. Try gain!"

def write_data_to_file(data):
    with open ("database.txt", mode = "a", newline="", ) as  database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject},{message}")

def write_to_csv(data):
    with open("database.csv", "a") as database2:
        write_header = not os.path.exists("database.csv") or os.path.getsize("database.csv") == 0

        email = data["email"]
        subject = data["subject"]
        message = data["message"]


        csv_writer = csv.writer(database2, delimiter=",", quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        if write_header:
            csv_writer.writerow(["email", "subject", "message"])

        csv_writer.writerow([email,subject,message])