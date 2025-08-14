from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    video_name = '245.mp4'
    return render_template("about.html", video_name=video_name)

@app.route('/ucapan')
def ucapan():
    return render_template('ucapan.html', title='Ucapan')

@app.route("/apology")
def apology():
    video_name = 'Aquarium.mp4'
    return render_template("apology.html", video_name=video_name)

if __name__ == "__main__":
    app.run(debug=True)