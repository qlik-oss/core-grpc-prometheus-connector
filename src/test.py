import prom

print(prom.fetch('http://localhost:9090', '{job=~"qix.+"}'))
