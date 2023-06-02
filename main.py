# import all other files
from spotify_api import *
from config import *

# Start the callback server
with socketserver.TCPServer(('localhost', PORT), CallbackHandler) as httpd:
    print('Callback server listening on port', PORT)
    httpd.handle_request()

