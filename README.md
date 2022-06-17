# video-upscaling (WIP)

1. Use FFMPEG to pad height (original height X 3);
```
ffmpeg -i 1280x720.mp4 -vf "pad=1280:720*3:0:0:black" -preset slower -crf 18 2160x720_pad.mp4 
``` 
2. Upscale using Topaz Video Enhance unregistered version (take upscaled desired width as a target);
3. Use FFMPEG to crop height to final desired resolution;
4. Use cracked version of Davinci resolve to increase frame hate to 60fps;
5. Use FFMPEG to put back sound track;
