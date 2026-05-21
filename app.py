from flask import Flask

app = Flask(__name__)

DOMAIN_NAME = "rivuawspracticesite.site"

@app.route('/')
def home():
    return f"""
    <html>
        <head>
            <title>{DOMAIN_NAME}</title>
        </head>

        <body style="font-family: Arial; text-align:center; margin-top:100px;">
            <h1>🚀 Production CI/CD Running</h1>
            <h2>Welcome to {DOMAIN_NAME}</h2>
            <p>Flask App Successfully Deployed Using Jenkins CI/CD Pipeline</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "running",
        "domain": DOMAIN_NAME
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

