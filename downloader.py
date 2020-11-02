from flask import Flask, send_file
import csv, io, json


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <H3>Welcome</H3>

    <p><a href="/inmemcsv" class="navbar-item">This</a> context route gives you a csv file from memory.</p>

    <p><a href="/fromdisk/test.csv" class="navbar-item">This</a> context route gives you a csv file from disk!</p>

    <p><a href="/inmemjson" class="navbar-item">This</a> context route gives you a json file from memory!</p>

    <p><a href="/fromdisk/test.json" class="navbar-item">This</a> context route gives you a json file from disk!</p>

    """

InMemData = [
    ['0','webserver','windows'],
    ['1','appserver','linux'],
    ['2','dnsserver','linux']
]

@app.route('/inmemcsv')
def inmemcsv():
    proxy = io.StringIO()
    writer = csv.writer(proxy)
    writer.writerow(['id','server','type'])
    for s in InMemData:
        writer.writerow([s[0],s[1],s[2]])                        
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    proxy.close()
    return send_file(mem, as_attachment=True, attachment_filename=f'InMemCSV.csv', mimetype='text/csv' )

@app.route('/inmemjson')
def inmemjson():
    response = []
    for s in InMemData:
        response.append({'id':s[0],'server':s[1],'type':s[2]})

    mem = io.BytesIO()
    mem.write(json.dumps(response).encode('utf-8'))
    mem.seek(0)
    return send_file(mem, as_attachment=True, attachment_filename=f'InMemJSON.json', mimetype='text/json' )

@app.route('/fromdisk/<file>')
def generated(file = None):
    if file:
        return send_file(file, as_attachment=True, attachment_filename=f"FromDisk.{('csv' if 'csv' in file else 'json')}", mimetype=('text/csv' if 'csv' in file else 'text/json') )
    else:
        return 'You need to specify a filename aswell.'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000, debug = True)