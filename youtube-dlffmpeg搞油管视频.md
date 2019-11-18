## youtube-dl/ffmpeg下油管视频

### 安装youtube-dl

pip install youtube-dl

安装后检查安装情况输入youtube-dl

看到：

Usage: youtube-dl [OPTIONS] URL [URL...]

youtube-dl: error: You must provide at least one URL.
Type youtube-dl --help to see a list of all options.

说明成功

### 安装ffmpeg

 https://ffmpeg.zeranoe.com/builds/win64/static/ 选择一个版本（我安装了ffmpeg-4.2.1-win64-static

 环境变量>系统变量>Path加上解压后的bin文件夹地址 

新打开cmd检查：ffmpeg -version

看到：

ffmpeg version 4.2.1 Copyright (c) 2000-2019 the FFmpeg developers
built with gcc 9.1.1 (GCC) 20190807

说明成功

### youtube-dl下载视频

#### 查看视频格式列表

代理调为全局：

```
youtube-dl -F [url]
```

代理模式PAC：都加上--proxy 127.0.0.1:1080

```
youtube-dl -F [url] --proxy 127.0.0.1:1080
```

 最左边一列就是编号对应着不同的格式.
由于YouTube的1080p及以上的分辨率都是音视频分离的,所以我们需要分别下载视频和音频,可以使用137+140这样的组合. 

```
youtube-dl -f [format code] [url]
```

youtube-dl -f 137+140  https://www.youtube.com/watch?v=L02Q6KexMtM --proxy 127.0.0.1:1080



 

参考

- https://www.jianshu.com/p/6bae57859325 

- https://github.com/ytdl-org/youtube-dl/blob/master/README.md