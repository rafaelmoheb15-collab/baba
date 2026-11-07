from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        in_out = request.form.get("in out")
        name = request.form.get("name")
        time = request.form.get("time")

        data = f"in or out = {in_out}\nname = {name}\ntime = {time}\n=============================\n"

        file = open("data base.txt","a")
        file.write(data)
        file.close()

    return render_template('baba.html')

if __name__ == "__main__":
    app.run(debug=True)