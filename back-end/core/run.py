import os

from app import create_app

app = create_app()

def run():
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('DEBUG', True)

    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run()