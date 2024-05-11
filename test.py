import requests
from p1337x import py1337x

a = requests.get("http://www.1337x.to")
print(a)
search_engine = py1337x(proxy='1337x.to', cache='py1337xCache', cacheTime=500)
print(search_engine.search("gta"))
