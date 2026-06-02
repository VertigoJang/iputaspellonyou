#!/usr/bin/env python3
 
import subprocess
import shutil
from pathlib import Path
 
TEMPV    = Path.home() / "iPodSync" / "tempv"
CHANGEDV = Path.home() / "iPodSync" / "changedv"
ARCHIVEV = Path.home() / "iPodSync" / "archivev"
 
TEMPV.mkdir(parents=True, exist_ok=True)
CHANGEDV.mkdir(parents=True, exist_ok=True)
ARCHIVEV.mkdir(parents=True, exist_ok=True)
 
print("=" * 40)
print("iPodSync Gen5")
print("=" * 40)
print()
 
urls = []
 
while True:
    url = input("YouTube URL: ").strip()
 
    if not url:
        print("URL cannot be empty.")
        continue
 
    urls.append(url)
 
    print()
    print(f"Added ({len(urls)})")
    print(url)
 
    answer = input("\nAdd another URL? (Y/N): ").strip().upper()
 
    if answer != "Y":
        break
 
print()
print("Download queue:")
print("-" * 40)
 
for i, url in enumerate(urls, start=1):
    print(f"{i}. {url}")
 
print("-" * 40)
print(f"Total URLs: {len(urls)}")
 
confirm = input("\nStart download? (Y/N): ").strip().upper()
 
if confirm != "Y":
    print("Cancelled.")
    raise SystemExit
 
print()
print("Downloading...")
print()
 
for url in urls:
    print(f"Downloading: {url}")
 
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
 
VALID_EXTENSIONS = [".webm", ".mkv", ".mp4", ".avi"]
 
stats_converted = 0
stats_skipped   = 0
stats_failed    = 0
 
for file in TEMPV.iterdir():
 
    if not file.is_file():
        continue
 
    if file.name.startswith("."):
        continue
 
    if file.suffix.lower() not in VALID_EXTENSIONS:
        continue
 
    output = CHANGEDV / f"{file.stem}_iPod.m4v"
 
    # 중복 변환 방지
    if output.exists():
        print(f"Skipped (already exists): {output.name}")
        stats_skipped += 1
        continue
 
    print()
    print("=" * 40)
    print(f"Converting: {file.name}")
    print("INPUT :", file)
    print("OUTPUT:", output)
    print("=" * 40)
 
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
        stats_converted += 1
 
        # archivev 자동 이동
        archive_dest = ARCHIVEV / file.name
        shutil.move(str(file), str(archive_dest))
        print(f"Archived: {file.name}")
 
    else:
        print(f"Failed: {file.name}")
        stats_failed += 1
 
print()
print("=" * 40)
print("All conversions completed.")
print("-" * 40)
print(f"Converted : {stats_converted}")
print(f"Skipped   : {stats_skipped}")
print(f"Failed    : {stats_failed}")
print("=" * 40)