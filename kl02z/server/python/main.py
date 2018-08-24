from flask import Flask, request;
import struct;

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/kl02z', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form);
        reStr = request.form['reStr'];
        # buf = struct.unpack(reStr, request.form['val']);
        buf = request.form['val'];
        buf = struct.unpack(reStr, buf.encode());
        print(reStr, buf);
        # do_the_login()
        return 'The Post page'
    else:
        # show_the_login_form()
        print("test kl02z Get");
        return 'The Get Page'
    

if __name__ == '__main__':
    app.run()