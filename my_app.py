from flask import Flask, render_template, request, jsonify
from inquire_kg import query,get_answer_profile
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')
@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data=query(str(name))
    return jsonify(json_data)
@app.route('/get_profile',methods=['GET','POST'])
def get_profile():
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)
    return jsonify(json_data)

if __name__ == '__main__':
    app.debug=True
    app.run()