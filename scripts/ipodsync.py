#!/usr/bin/env python3

# ============================================
# iPodSync
# Version : v0.3
# Codename: Menu System
# ============================================

import subprocess
import shutil
from pathlib import Path

VERSION  = "v0.3"
CODENAME = "Menu System"

TEMPV    = Path.home() / "iPodSync" / "tempv"
CHANGEDV = Path.home() / "iPodSync" / "changedv"
ARCHIVEV = Path.home() / "iPodSync" / "archivev"

TEMPV.mkdir(parents=True, exist_ok=True)
CHANGEDV.mkdir(parents=True, exist_ok=True)
ARCHIVEV.mkdir(parents=True, exist_ok=True)

VALID_EXTENSIONS = [".webm", ".mkv", ".mp4", ".avi"]


def download_videos(urls):
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


def convert_videos():
    print()
    print("Converting...")
    print()

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


def collect_urls():
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

    return urls


def show_queue_and_confirm(urls):
    print()
    print("Download queue:")
    print("-" * 40)

    for i, url in enumerate(urls, start=1):
        print(f"{i}. {url}")

    print("-" * 40)
    print(f"Total URLs: {len(urls)}")

    confirm = input("\nStart download? (Y/N): ").strip().upper()
    return confirm == "Y"


def menu_download_video():
    urls = collect_urls()

    if not show_queue_and_confirm(urls):
        print("Cancelled.")
        return

    download_videos(urls)
    convert_videos()


def menu_download_playlist():
    print()
    print("Playlist download is not implemented yet. (Coming in v0.5)")


def menu_convert_existing():
    print()
    print("Re-scanning tempv for unconverted files...")
    convert_videos()


def menu_settings():
    print()
    print("Settings menu is not implemented yet. (Coming in v0.4)")


def show_menu():
    print()
    print("=" * 40)
    print(f"iPodSync {VERSION} ({CODENAME})")
    print("=" * 40)
    print("1. Download Video")
    print("2. Download Playlist")
    print("3. Convert Existing Files")
    print("4. Settings")
    print("5. Exit")
    print("-" * 40)


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            menu_download_video()
        elif choice == "2":
            menu_download_playlist()
        elif choice == "3":
            menu_convert_existing()
        elif choice == "4":
            menu_settings()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
