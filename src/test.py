import prom

print(prom.fetch('http://localhost:9090', '{__name__=~".+"}'))
