from flask import Flask , render_template_string
import os
app = Flask(__name__)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>  
<head>
    <title>DevOps CI/CD Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
            background-color: linear-gradient(#135eg, #667eea 0%, #764ba2 100%);
            color:white;
        }
        .container {
            background-color: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            }

        h1 { font-size: 3em; margin-bottom: 20px; }
        .version { font-size: 1.2em;  opacity: 0.8; }
    </style>
</head>

        <div class="container">
    <h1>Welcome to the DevOps CI/CD Demo!</h1>
    <p>Succesfully depoloyed via Jenkins -> Docker -> AWS </p>
    <div class="version">Version: 1.0</div>
    <p>Build: {{ build_number }}</p>
    </div>
    </body>
</html>
'''
@app.route('/')
def home():
    build_number = os.getenv('BUILD_NUMBER', 'local')
    return render_template_string(HTML_TEMPLATE, build_number=build_number)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    