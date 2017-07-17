import pyautogui, flask

app = flask.Flask(__name__)


@app.route('/')
def send_index_page():
    return flask.render_template('index.html')


@app.route('/keypress/<keypress>')
def process_key(keypress=None):
    if(keypress):
        print('Received keypress for ' + keypress)
        pyautogui.keyDown(keypress)
        pyautogui.keyUp(keypress)
    else:
        print('Received empty keypress')
    return keypress


if(__name__ == '__main__'):
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)
