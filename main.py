from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index')
def index():
	return render_template('index.html',title='Blog App Home')

@app.route('/add')
def add():
	return render_template('Addblog.html',title='Blog App Add')

@app.route('/support')
def support():
	return render_template('support.html' ,title='Feedback or Query')


@app.route('/blogs')
def blogs():
	return render_template('blogs.html', title='Blog Page')

if __name__=='__main__':
	app.run(debug=True,port=8000)