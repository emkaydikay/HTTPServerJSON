import urllib.request
import json

def post_data_Update():
    print("POST request: Updating next data to HTTPServer......")
    url = "http://localhost:8000"    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    config = json.loads(open('get_received.json').read())
    data = json.dumps(config).encode("utf-8")
    
    print("Sending data to HTTPServer\n",data)    
    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        print("Data received from HTTPServer\n",res.decode())
    except Exception as e:
        print(e)

def get_data_request():
    print("GET request")
    url = "http://localhost:8000"  
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as f:
            httpResponse = f.read()
        print("Data received from HTTPServer\n",httpResponse.decode())
    except Exception as e:
        print(e)
    #Get the value of the key.    
    resp = json.loads(httpResponse.decode())
    latest = resp['latestVersion']
    #Updating to next version and revert back to server
    resp['latestVersion'] = "ABCD010"
    print(latest)   
    with open("get_received.json", "w") as outfile:
        json.dump(resp, outfile)
    
    
######MAIN#####
get_data_request()
post_data_Update()
