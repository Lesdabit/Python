import urllib.request as req
url="https://www.ptt.cc/bbs/movie/M.1663930997.A.BF4.html"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)