import sys

path = '/home/jeevithakannan/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import app as application  # Use the Flask app instance

if __name__ == "__main__":
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
