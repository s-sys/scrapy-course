import requests 
import lxml.html 
req = requests.get("http://www.dourados.ms.gov.br/") 
tree = lxml.html.fromstring(req.text) 
for event in tree.xpath("//*[@id='mostra-eventos-home']/ul/li/h5/a"): 
    name = event.xpath("text()") 
    url = event.xpath("@href") 
    print(name) 
    print(url) 
