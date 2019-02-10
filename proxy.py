import urllib.request as request

# disable proxy by passing an empty
proxy_handler = request.ProxyHandler({})
# alertnatively you could set a proxy for http with
# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})

opener = request.build_opener(proxy_handler)

url = 'https://www.w3schools.com/'

# open the website with the opener
req = opener.open(url)
data = req.read().decode('utf8')
print(data)