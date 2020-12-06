from http.server import BaseHTTPRequestHandler,HTTPServer
import http.server
import socketserver
import urllib
try:
    import json
except ImportError:
    import simplejson as json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        #self.send_header('Content-type','text/html')
        self.end_headers()
        config = json.loads(open('response.json').read())
        self.wfile.write(json.dumps(config).encode())
        return
    def do_POST(self):
        print(" POST request. Receiving from client....")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(self.data_string)
        with open("receive.json", "w") as outfile:
            json.dump(data, outfile)
        print("Received data from client = ",data)
        
        
        self.send_response(200)
        self.end_headers()
        config = json.loads(open('post_res.json').read())
        self.wfile.write(json.dumps(config).encode())
        return  

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), RequestHandler)
    print('Starting server at http://localhost:8000')
    server.serve_forever()
