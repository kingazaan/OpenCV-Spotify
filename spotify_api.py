
import http.server
import socketserver
import requests
from urllib.parse import urlparse, parse_qs
from config import *
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET) #, redirect_uri=redirect_uri)
sp = spotipy.Spotify(client_credentials_manager)


# def authenticate_spotify_api(client_id, client_secret, authorization_code, redirect_uri):
#     # Set up the authorization code grant flow parameters
#     auth_url = 'https://accounts.spotify.com/api/token'
#     headers = {'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')}
#     data = {
#         'grant_type': 'authorization_code',
#         'code': authorization_code,
#         'redirect_uri': redirect_uri,
#     }

#     try:
#         # Make a POST request to the Spotify API token endpoint to exchange the authorization code for an access token
#         response = requests.post(auth_url, headers=headers, data=data)
#         response.raise_for_status()

#         # Extract the access token from the response
#         token_data = response.json()
#         access_token = token_data.get('access_token')

#         if access_token:
#             return access_token
#         else:
#             raise Exception('Access token not found in the authentication response')

#     except requests.exceptions.HTTPError as e:
#         # Handle HTTP errors
#         print('HTTP Error:', e)
#         raise

#     except Exception as e:
#         # Handle other exceptions
#         print('Error:', e)
#         raise

# class CallbackHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         query_components = parse_qs(urlparse(self.path).query)
        
#         # Extract the authorization code from the query parameters
#         if 'code' in query_components:
#             authorization_code = query_components['code'][0]
            
#             # Pass the authorization code to the authentication function
#             access_token = authenticate_spotify_api(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, authorization_code, redirect_uri)

#             # Send a response back to the browser
#             self.send_response(200)
#             self.send_header('Content-type', 'text/html')
#             self.end_headers()
#             self.wfile.write(b'Authorization code received. You can close this page now.')

# # Set the desired port for the callback server
# PORT = 8000

# print(authorization_code)

# # Start the callback server
# with socketserver.TCPServer(('localhost', PORT), CallbackHandler) as httpd:
#     print('Callback server listening on port', PORT)
#     httpd.serve_forever()

