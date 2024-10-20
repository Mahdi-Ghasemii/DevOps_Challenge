import re
import json
from urllib.request import urlopen
from flask import Flask , render_template , redirect , request

def get_location_using_ip_add(ip_addr):
    base_url = 'https://ipinfo.io'
    response = urlopen(f"{base_url}/{ip_addr}/json")
    data = json.load(response)
    IP=data['ip']
    city = data['city']
    country=data['country']
    region=data['region']
    print('Your IP detail\n ')
    print('Region : {0} \nCountry : {1} \nCity : {2} \nIP : {3}'.format(region,country,city,IP))


app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/ip_check/<ip_addr>' , methods={"POST"})
def ip_check(ip_addr):
   get_location_using_ip_add(ip_addr)
   return redirect('/')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0' , port=4000)