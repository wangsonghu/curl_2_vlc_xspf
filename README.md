## 构建镜像

```
docker build -t harbor.hosts.songhu.wang:8443/apps/python:alpine3.6_curl_list_xspf_v2023-08-20 .
```
## url转vlc播放列表

```
docker run -it --rm --name curl_list_xspf --add-host web-server.hosts.songhu.wang:192.168.199.253 -v `pwd`:/out -w /work harbor.hosts.songhu.wang:8443/apps/python:alpine3.6_curl_list_xspf_v2023-08-20 <URL>
```

## 使用打开xspf
