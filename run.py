from flask import Flask
from pyngrok import ngrok
from app import create_app
import config

# Initialize Flask app
app = create_app()

if __name__ == "__main__":
    # Set up ngrok tunnel
    ngrok.set_auth_token(config.NGROK_AUTH_TOKEN)
    public_url = ngrok.connect(config.PORT).public_url
    print(f"🌍 Public URL: {public_url}")

    # Run Flask app
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
