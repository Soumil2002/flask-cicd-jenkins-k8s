from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Love App</title>
            <style>
                body {
                    background-color: #ffebee;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: 'Arial', sans-serif;
                }
                h1 {
                    color: #e91e63;
                    font-size: 50px;
                    text-shadow: 2px 2px 4px #000000;
                }
            </style>
        </head>
        <body>
            <h1>❤️ Sending Love to the World! ❤️</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
