from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)

#python3 -m venv virtual: run this code in terminal to create a virtual environment
#Chukwyenum-MacBook-Pro:mysite chukwuyenumopone$ python3 -m venv virtual
#Chukwyenum-MacBook-Pro:mysite chukwuyenumopone$ virtual/bin/python3
#Chukwyenum-MacBook-Pro:mysite chukwuyenumopone$ virtual/bin/pip install flask