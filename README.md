# video-upscaling (WIP)

1. Use FFMPEG to pad height (original height X 3);

    ```
    ffmpeg -i 1280x720.mp4 -vf "pad=1280:720*3:0:0:black" -preset slower -crf 18 2160x720_pad.mp4 
    ``` 
    
2. Upscale it using Topaz Video Enhance unregistered version (fill parameters with upscaled desired width as a target, then let Topaz calculate how much percent must be applied);
3. Use FFMPEG to crop height to final desired resolution;

    ```
    ffmpeg -i 1920x3240_topaz.mp4 -vf "crop=1920:1080:0:0" -preset slower -crf 18 1920x1080_croped.mp4
    ```
    
4. Use cracked version of Davinci resolve to increase frame hate to 60fps;
5. Use FFMPEG to put back sound track;

    ```
    ffmpeg -i video.mp4  -i audio.mp4  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
    ```
  
 
# temp
  
- https://www.roelpeters.be/python-run-shell-commands-with-the-subprocess-package/
- https://superuser.com/questions/841235/how-do-i-use-ffmpeg-to-get-the-video-resolution
- https://stackoverflow.com/questions/37088517/remove-sequentially-duplicate-frames-when-using-ffmpeg
- https://avpres.net/FFmpeg/4-3_16-9
- https://avpres.net/FFmpeg/

```
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name,profile,level,bit_rate,r_frame_rate  -of json file.mp4
```

```
ffprobe -v error -show_streams -select_streams v:0 -of json file.mp4
```

Encode with handware asceleration:
```
ffmpeg -hide_banner -i video.mp4 -vcodec h264_nvenc -r 30 -preset p6 -profile baseline -level 40 -cq 23 output.mp4
```
