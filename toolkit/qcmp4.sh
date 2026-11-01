#!/bin/bash
# usage: qcmp4.sh file.mp4 id  -> qc/<id>_mp4.png (2 fps samples cropped to safe area) + spec line
f=$1; id=$2
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate,pix_fmt -of compact=p=0 "$f" | tr '\n' ' '; echo
ffmpeg -v error -y -i "$f" -vf "fps=1,crop=1080:1240:0:220,scale=180:-1,tile=8x4:padding=3:color=0x777777" -frames:v 1 qc/${id}_mp4.png
