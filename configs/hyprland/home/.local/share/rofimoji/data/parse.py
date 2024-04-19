import json5
import requests

OUT_FILE = "nerdfont.csv"

r = requests.get("https://www.nerdfonts.com/cheat-sheet")

start_text = "const glyphs = "
if start_text not in r.text:
    raise ValueError("Icons list not found")

start = r.text.find(start_text) + len(start_text)
end = r.text.find('}', start)
data = r.text[start:end+1]

with open(OUT_FILE, 'w', encoding="utf-8") as f:
    for name, icon in json5.loads(data).items():
        f.write(
            chr(int.from_bytes(bytes.fromhex(icon if not len(icon) % 2 else '0'+icon))) + ' '
            + name.rsplit('-', maxsplit=1)[-1].replace('_', ' ') + '\n'
        )

print("Icons parsed")
