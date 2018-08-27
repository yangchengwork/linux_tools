from flask import Flask, request, make_response, jsonify;
import struct;

app = Flask(__name__)

outx = 0;
outy = 0;
outz = 0;

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
    global outx, outy, outz
    if request.method == 'POST':
        # print(request.form);
        length = int(request.form['len']);
        reStr = "@%dh" % (length * 3);
        buf = request.form['val'];
        # buf = buf.encode('utf-8',"ignore");
        # print(length, len(buf));
        # for id in buf:
        #     print(ord(id));
        # buf = bytearray(buf);
        # print(length, buf);
        buf = struct.unpack(reStr, buf.encode('ISO-8859-1'));
        # print(length, len(buf[:length]), len(buf[length: 2*length]), len(buf[2*length:]));
        x = 0;
        y = 0;
        z = 0;
        for i in buf[:length]:
            x += i;
            # print('x', i);
        for i in buf[length: 2*length]:
            y += i;
            # print('y', i);
        for i in buf[2*length:]:
            z += i;
            # print('z', i);
        outx = int(x/length);
        outy = int(y/length);
        outz = int(z/length);
        # print(x, y, z);
        # do_the_login()
        return 'value x=%d y=%d z=%d' % (outx, outy, outz);
    else:
        # show_the_login_form()
        # print("test kl02z Get");
        result_text = {"statusCode": 200,
        "x": '%d' % outx,
        "y": '%d' % outy,
        "z": '%d' % outz,
        }
        response = make_response(jsonify(result_text))
        # response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        return response;
    

if __name__ == '__main__':
    app.run()