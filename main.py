"""Cutest cat entry: the kitten image is stored as base64 text (cat.png.b64)
because the image itself is binary. Decoding it is deterministic, so every
run writes the same PNG bytes to /output/entry.png. No network."""

import base64, os

here = os.path.dirname(os.path.abspath(__file__))
os.makedirs('/output', exist_ok=True)
with open(os.path.join(here, 'cat.png.b64'), encoding='utf-8') as f:
    data = base64.b64decode(f.read())
if not data.startswith(b'\x89PNG\r\n\x1a\n'):
    raise ValueError('decoded bytes are not a PNG')
with open('/output/entry.png', 'wb') as f:
    f.write(data)
