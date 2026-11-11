import base64, os
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs('/output', exist_ok=True)
with open(os.path.join(here, 'cat.png.b64'), encoding='utf-8') as f:
    data = base64.b64decode(f.read())
with open('/output/entry.png', 'wb') as f:
    f.write(data)
