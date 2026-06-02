#!/usr/bin/env python3

import subprocess
from pathlib import Path

TEMPV = Path.home() / "iPodSync" / "tempv"
CHANGEDV = Path.home() / "iPodSync" / "changedv"

TEMPV.mkdir(parents=True, exist_ok=True)
CHANGEDV.mkdir(parents=True, exist_ok=True)

print("=" * 40)
print("iPodSync Gen5")
print("=" * 40)
print()

url = input("YouTube URL: ").strip()

if not url:
 print("No URL entered.")
 raise SystemExit

print()
print("Downloading...")
print()

subprocess.run([
"yt-dlp",
"-f",
"bestvideo[height<=480]+bestaudio/best[height<=480]",
"-o",
str(TEMPV / "%(title)s [%(id)s].%(ext)s"),
url
])

print()
print("Converting...")
print()

for file in TEMPV.iterdir():

 print("FOUND:", file)

 if file.suffix.lower() not in [
    ".webm",
    ".mkv",
    ".mp4",
    ".avi"
]:
    continue

output = CHANGEDV / f"{file.stem}_iPod.m4v"

print(f"Converting: {file.name}")
print("INPUT :", file)
print("OUTPUT:", output)

result = subprocess.run([
    "ffmpeg",
    "-y",
    "-i", str(file),
    "-vf",
    "scale=320:240:force_original_aspect_ratio=decrease,pad=320:240:(ow-iw)/2:(oh-ih)/2",
    "-c:v", "libx264",
    "-profile:v", "baseline",
    "-level", "3.0",
    "-pix_fmt", "yuv420p",
    "-r", "30",
    "-b:v", "700k",
    "-maxrate", "768k",
    "-bufsize", "1536k",
    "-c:a", "aac",
    "-b:a", "128k",
    "-ar", "44100",
    "-movflags", "+faststart",
    str(output)
])

print("RETURN CODE:", result.returncode)

if result.returncode == 0:
    print(f"Finished: {output.name}")
else:
    print(f"Failed: {file.name}")

print()
print("All conversions completed.")
