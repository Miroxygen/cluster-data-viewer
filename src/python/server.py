from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from functions.k_means import k_means

hostname = "localhost"
serverPort = 8083

class DataHandlerServer(BaseHTTPRequestHandler):
  def do_GET(self):
        if self.path == '/':
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          self.wfile.write(bytes("Welcome!", "utf8"))
        if self.path == '/get-kmeans':
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          data_json = json.dumps(k_means)
          self.wfile.write(bytes(data_json, "utf-8"))
        else:
          self.send_response(404)

with HTTPServer((hostname, serverPort), DataHandlerServer) as server:
  print(f'Starting server on port {serverPort}')
  server.serve_forever()