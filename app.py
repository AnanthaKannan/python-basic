from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def initial_check():
    print('pyton inside')
    return "Inital check is sccess."


@app.route('/check', methods=['GET'])
def get_tasks():
    return "success"

if __name__ == '__main__':
    app.run()