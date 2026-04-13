from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def radio():
    result = ""

    if request.method == "POST":
        gender = request.form.get("gender")
        result = f"Siz tanlandingiz: {gender}"

    return render_template('radio.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
