from flask import Flask, render_template, url_for, request, redirect
from db import db
from User import User
from sqlite3 import IntegrityError


app = Flask(__name__)


@app.route('/')
def homepage():
    database = db()
    return render_template('home.html', times=database.getTimes())


@app.route('/signup/<time_id>', methods=['post', 'get'])
def signup(time_id):
    if request.method == 'POST':
        ph = request.form.get('phone_number')
        database = db()
        try:
            user = User(time_id, ph)
            database.addUser(user)
        except IntegrityError:
            return render_template('alreadyregistered.html')
        except IOError:
            return render_template('invalidnumber.html')
        except:
            return 'uh oh! something that was not supposed to happen just did'

        return render_template('success.html')
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)

