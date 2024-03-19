from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>
Top Companies List
</title>
</head>
<table align="center" border="4" cellspacing="5" cellpadding="10" height="100" width="800">
<caption align="center"><B>Top Companies Lists</B></caption>
<tr>
<th align="center">Rank</th>
<th align="center">Company</th>
<th align="center">Country</th>
<th align="center">Sales</th>
<th align="center">Profits</th>
<th align="center">Assets</th>
<th align="center">Market Value</th>
</tr>
<tr>
  <td align="center">41</td>
  <td align="center">Microsoft</td>
  <td align="center">United States</td>
  <td align="center">$72.9 B</td>
  <td align="center">$15.5 B</td>
  <td align="center">$128.7 B</td>
  <td align="center">$234.8 B</td>
</tr>
<tr>
  <td align="center">102</td>
  <td align="center">Oracle</td>
  <td align="center">United States</td>
  <td align="center">$37.1 B</td>
  <td align="center">$ 10.6 B</td>
  <td align="center">$79.4 B</td>
  <td align="center">$172 B</td>
</tr>
<tr>
  <td align="center">211</td>
  <td align="center">SAP</td>
  <td align="center">Germany</td>
  <td align="center">$20.9 B</td>
  <td align="center">$3.6 B</td>
  <td align="center">$35.5 B</td>
  <td align="center">$103.9 B</td>
</tr>
<tr>
  <td align="center">718</td>
  <td align="center">Symantee</td>
  <td align="center">United States</td>
  <td align="center">$6.8 B</td>
  <td align="center">$1.1 B</td>
  <td align="center">$1.4 B</td>
  <td align="center">$16.9 B</td>
</tr>
<tr>
  <td align="center">993</td>
  <td align="center">CA</td>
  <td align="center">United States</td>
  <td align="center">$4.7 B</td>
  <td align="center">$0.9 B</td>
  <td align="center">$11.6 B</td>
  <td align="center">$11.6 B</td>
</tr>
<tr>
  <td align="center">879</td>
  <td align="center">VMware</td>
  <td align="center">United States</td>
  <td align="center">$4.6 B</td>
  <td align="center">$0.7 B</td>
  <td align="center">$10.6 B</td>
  <td align="center">$35.9 B</td>
</tr>
<tr>
  <td align="center">1237</td>
  <td align="center">Fiserv</td>
  <td align="center">United States</td>
  <td align="center">$4.5 B</td>
  <td align="center">$0.6 B</td>
  <td align="center">$8.5 B</td>
  <td align="center">$11.4 B</td>
</tr>
<tr>
  <td align="center">995</td>
  <td align="center">Adobe Systems</td>
  <td align="center">United States</td>
  <td align="center">$4.4 B</td>
  <td align="center">$0.7 B</td>
  <td align="center">$10.2 B</td>
  <td align="center">$20.6 B</td>
</tr>
<tr>
  <td align="center">1099</td>
  <td align="center">Intuit</td>
  <td align="center">United States</td>
  <td align="center">$4.2 B</td>
  <td align="center">$0.8 B</td>
  <td align="center">$5.1 B</td>
  <td align="center">$19.4 B</td>
</tr>
<tr>
  <td align="center">1534</td>
  <td align="center">HCL Technologies</td>
  <td align="center">India</td>
  <td align="center">$3.8 B</td>
  <td align="center">$0.4 B</td>
  <td align="center">$3.2 B</td>
  <td align="center">$10.2 b</td>
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