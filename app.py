from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name="AKSHAY")


@app.route('/profile')
@app.route('/profile/<int:user_id>')
def profile(user_id=None):
	data = {
		'user_data': {
			1: { 'name': 'Megan Fox', 'image': 'megan.jpg' },
			2: { 'name': 'Elsa Hosk', 'image': 'elsa.jpg' },
			3: { 'name': 'Candice Swanepoel', 'image': 'candice.jpg' },
			4: { 'name': 'Doutzen Kroes', 'image': 'doutzen.jpg' },
			5: { 'name': 'Lana Del Rey', 'image': 'lana.jpg' }
		},
		'user_id': user_id
	}
	return render_template('profile.html', data=data)


if __name__ == '__main__':
	app.run()