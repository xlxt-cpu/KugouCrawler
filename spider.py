import requests
import json

# 请求参数
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "Cookie": "kg_mid=1c18fc49a0caa122f500ac7505e22a41; kg_dfid=2C7ga71m8rBa1YB0el1siK8Q; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e",
}
proxies = {"http": None, "https": None}

# 获取歌曲hash值
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1698031619200&mid=1c18fc49a0caa122f500ac7505e22a41&uuid=1c18fc49a0caa122f500ac7505e22a41&dfid=2C7ga71m8rBa1YB0el1siK8Q&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=d0bebdeaf9424273bb017f30e0826ec4'
list_resp = requests.get(list_url, headers=headers, proxies=proxies)
song_list = json.loads(list_resp.text[12:-2])['data']['lists']
for i, s in enumerate(song_list):
    print(f"{i + 1}-----{s.get('SongName')}----{s.get('EMixSongID')}")

num = input('请输入要下载第几首音乐:')


#  保存数据
def download(name, m_url):
    m_resp = requests.get(m_url, headers=headers, proxies=proxies)
    with open(f'{name}.mp3', "wb") as f:
        f.write(m_resp.content)
    print(f"下载成功---{name}.mp3")


# 请求音乐信息的url
info_url = f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={song_list[int(num) - 1].get('EMixSongID')}"
info_resp = requests.get(info_url, headers=headers, proxies=proxies)
"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id=n0800ae"
audio_name = info_resp.json()['data']['audio_name']
m_url = info_resp.json()['data']['play_url']
download(audio_name, m_url)
