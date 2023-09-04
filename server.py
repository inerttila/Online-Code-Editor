from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template("./index.html")

@app.route("/javascript/", methods=['GET'])
def js():
    return render_template("./j.html")

@app.route('/runcode', methods=['POST'])
def run_code():
    python_code = request.form['code']
    try:
        # Execute the Python code using subprocess and capture the output and errors
        process = subprocess.Popen(['python', '-c', python_code],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            return jsonify({'output': stdout, 'error': None})
        else:
            return jsonify({'output': None, 'error': stderr})
    except Exception as e:
        return jsonify({'output': None, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5500)