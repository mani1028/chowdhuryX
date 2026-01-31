# Entry point for WSGI servers (e.g., Gunicorn)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()