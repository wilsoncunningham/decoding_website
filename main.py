
from flask import Flask, request, render_template, jsonify
from decode import decode, decode_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    input_type = request.form['input_type']
    complexity = int(request.form['complexity'])
    input_body = request.form['input_body']

    # Process input based on type (text or URL)
    if input_type == 'text':
        password = decode(input_body, complexity)
    elif input_type == 'url':
        password = decode_url(input_body, complexity)
    else:
        password = "Invalid input type!"

    # return render_template('submission.html', password=password)
    print(password)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
