# SteamGridDB Thumbnail Grabber

Small Python script that grabs a horizontal image from SteamGridDB using a Steam AppID, crops it to 16:9, and saves it as a `1280x720` JPG.

I made this mostly because I wanted a quick way to get consistent game thumbnails without manually searching for artwork every time (and to show a site how easy it is to do this)

## What it does

Give it a Steam AppID and it will:

* look for a `920x430` SteamGridDB grid
* pick the highest-rated result
* download the full-quality image
* crop it to 16:9
* resize it to `1280x720`
* save it as `<appid>.jpg`

For example:

```bash
python thumbnail.py 570
```

will save:

```text
570.jpg
```

## Requirements

You'll need Python 3 and Pillow.

Install Pillow with:

```bash
pip install pillow
```

You'll also need a SteamGridDB API key.

You can get one from your SteamGridDB account settings.

https://www.steamgriddb.com/profile/preferences/api

## Setup

Open the script and replace:

```python
API_KEY = "PUT_YOUR_API_KEY_HERE"
```

with your actual key:

```python
API_KEY = "your_key_here"
```

Then you're good to go.

## Usage

Run the script and pass a Steam AppID:

```bash
python thumbnail.py APPID
```

Example:

```bash
python thumbnail.py 730
```

Output:

```text
730.jpg
```

The final image will be:

```text
1280x720
```

## Finding a Steam AppID

The AppID is usually visible in the game's Steam URL.

For example:

```text
https://store.steampowered.com/app/570/Dota_2/
```

The AppID is:

```text
570
```

## Notes

The script currently looks for `920x430` artwork on SteamGridDB.

It uses the highest-rated image it finds, so the result may not always be the exact artwork you'd personally choose.

The image is cropped rather than stretched, so depending on the original artwork, a little bit may be cut off around the edges.

## API Key

The API key is currently hardcoded because this is meant to be a simple personal script.

If you're planning to upload your own copy publicly, don't commit your real API key.

You can add the script to a private repo, use an environment variable instead, or just replace the key with a placeholder before pushing.

## License

Do whatever you want with the script.

SteamGridDB artwork belongs to its respective creators and owners.
