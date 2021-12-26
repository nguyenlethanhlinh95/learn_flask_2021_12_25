from flask import Flask, request, jsonify, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def top():
    return 'Hello world'


@app.route('/session', methods=['GET'])
def newSession():
    session['myname'] = 'linh'
    redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'], defaults={'username': 'Default'})
@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
    # if 'name' in session:
    #     name = session['name']
    # else:
    #     name = 'NotSession'
    return 'Hello {}, from home, my name is'.format(username)


@app.route('/process-json', methods=['POST'])
def processJson():
    data = request.get_json()
    name = data['name']
    return jsonify({'result': 'success', 'name': name})


@app.route('/redirect', methods=['GET'])
def redirectToHome():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.secret_key = b'400b73374871a365817f1d81dcb63b4e1c7528e73721dd6c223b162a3a175580'
    app.debug = True
    app.run(host="0.0.0.0", debug=True)
