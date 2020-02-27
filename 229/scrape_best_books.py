import requests_html
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}
URL = "https://bookauthority.org/books/best-programming-books"
session = requests_html.HTMLSession()
request = session.get(url=URL, headers=HEADERS)
request.html.render(timeout=0, wait=2)
response = request.html.html
breakpoint()
print(request.headers) 
with open("page_rendered.html","w+") as p:
    p.write(response)

