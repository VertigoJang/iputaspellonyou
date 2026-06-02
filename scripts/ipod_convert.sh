#!/bin/bash

SOURCE="$HOME/iPodSync/tempv"
DEST="$HOME/iPodSync/changedv"

mkdir -p "$DEST"

for FILE in "$SOURCE"/*.webm "$SOURCE"/*.mkv "$SOURCE"/*.mp4 "$SOURCE"/*.avi
do
    [ -f "$FILE" ] || continue

    BASENAME=$(basename "$FILE")
    NAME="${BASENAME%.*}"

    echo "Converting: $BASENAME"

    ffmpeg -y \
        -i "$FILE" \
        -vf "scale=320:240:force_original_aspect_ratio=decrease,pad=320:240:(ow-iw)/2:(oh-ih)/2" \
        -c:v libx264 \
        -profile:v baseline \
        -level 3.0 \
        -pix_fmt yuv420p \
        -r 30 \
        -b:v 700k \
        -c:a aac \
        -b:a 128k \
        -ar 44100 \
        -movflags +faststart \
        "$DEST/${NAME}_iPod.m4v"

    echo "Done: $BASENAME"
done

echo "All conversions completed."
