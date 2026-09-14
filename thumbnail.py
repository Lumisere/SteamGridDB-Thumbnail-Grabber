import io
import json
import sys
import urllib.request
import urllib.parse

from PIL import Image, ImageOps


API_KEY = "PUT_YOUR_API_KEY_HERE"
APP_ID = sys.argv[1]

api_url = f"https://www.steamgriddb.com/api/v2/grids/steam/{APP_ID}"

params = urllib.parse.urlencode({
    "dimensions": "920x430"
})

req = urllib.request.Request(
    f"{api_url}?{params}",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

with urllib.request.urlopen(req) as response:
    data = json.load(response)

grids = data["data"]

if not grids:
    print("No image found")
    sys.exit()

# Use the highest rated grid
grid = max(grids, key=lambda x: x.get("score", 0))

image_req = urllib.request.Request(grid["url"])

with urllib.request.urlopen(image_req) as response:
    image_data = response.read()

image = Image.open(io.BytesIO(image_data)).convert("RGB")

image = ImageOps.fit(
    image,
    (1280, 720),
    Image.Resampling.LANCZOS
)

filename = f"{APP_ID}.jpg"

image.save(filename, quality=90)

print(f"Saved {filename}")
