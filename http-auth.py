from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username1' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return decorated

@app.route('/')
def hello_world():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password' :
        return 'You are logged in'

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


@app.route('/page')
@auth_required
def page():
    return 'You are on the page'


if __name__ == '__main__':
    app.run()
