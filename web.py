from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>
Top five Revenue generating Software Companies.
</title>
</head>
<table border="2" cellspacing="5" cellpadding="10" height="100" width="800">
<caption align="center"><B>Top five Revenue generating Software Companies</B></caption>
<tr>
<th align="center">Rank</th>
<th align="center">Company</th>
<th align="center">Sales</th>
<th align="center">HQ</th>
<th align="center">Market Value</th>
</tr>
<tr>
  <td align="center">1</td>
  <td align="center">Microsoft</td>
  <td align="center">198.3B$</td>
  <td align="center">US</td>
  <td align="center">1,780.0B$</td>
</tr>
<tr>
  <td align="center">2</td>
  <td align="center">Google</td>
  <td align="center">282.11B$</td>
  <td align="center">US</td>
  <td align="center">1195.0B$</td>
</tr>
<tr>
  <td align="center">3</td>
  <td align="center">IBM</td>
  <td align="center">77.87B$</td>
  <td align="center">US</td>
  <td align="center">131.9B$</td>
</tr>
<tr>
  <td align="center">4</td>
  <td align="center">Oracle</td>
  <td align="center">39.6B$</td>
  <td align="center">US</td>
  <td align="center">240.51B$</td>
</tr>
<tr>
  <td align="center">5</td>
  <td align="center">SAP</td>
  <td align="center">29.1B$</td>
  <td align="center">Germany</td>
  <td align="center">132.01B$</td>
</tr>
</table>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()