import prom

result = prom.fetch('http://localhost:9090', '{__name__=~".+"}')

metadata = prom.build_metadata(result)
chunks = prom.build_chunks(result, metadata)

print([x.name for x in metadata.fieldInfo])
for chunk in chunks:
    print(chunk.stringBucket)
    print(chunk.doubleBucket)
    break