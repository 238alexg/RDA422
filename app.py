#app.py

from flask import Flask, render_template, request as req, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/request")
def ask():
    return render_template('request.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/buttonPress', methods=['POST'])
def buttonPress():
    print("BUTTON HAS BEEN PRESSED")
    name = req.form.get('usr')
    id = req.form.get('id')
    phone = req.form.get('phone')
    pickup = req.form.get('pick_up')
    dropoff = req.form.get('drop_off')
    hour = req.form.get('hour')
    min = req.form.get('min')
    numRiders = req.form.get('riders')
    specRequests = req.form.get('spec')
    print(name)
    print(id)
    print(phone)
    print(pickup)
    print(dropoff)
    print(hour)
    print(min)
    print(numRiders)
    print(specRequests)
    
    return render_template('success.html')

if __name__ == "__main__":
	app.run()