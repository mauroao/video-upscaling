# video-upscaling (WIP)

1. Use FFMPEG to pad height (original height X 3);
```
ffmpeg -i 1280x720.mp4 -vf "pad=1280:720*3:0:0:black" -preset slower -crf 18 2160x720_pad.mp4 
``` 
2. Upscale using Topaz Video Enhance unregistered version (take upscaled desired width as a target);
3. Use FFMPEG to crop height to final desired resolution;
```
ffmpeg -i 1920x3240_topaz.mp4 -vf "crop=1920:1080:0:0" -preset slower -crf 18 1920x1080_croped.mp4
```
4. Use cracked version of Davinci resolve to increase frame hate to 60fps;
5. Use FFMPEG to put back sound track;
```
ffmpeg -i video.mp4  -i audio.mp4  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```
