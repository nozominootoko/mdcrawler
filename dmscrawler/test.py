import requests as req
from hyper.contrib import HTTP20Adapter
import time

co = {
    "Cookie": "_uuid=8B7669FA-FD4E-288D-55F1-57EB7C18555F18668infoc; buvid3=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; sid=8zdnly24; DedeUserID=624599; DedeUserID__ckMd5=faff4574ebdbeb78; SESSDATA=b5c4702c,1638704641,fd08e*61; bili_jct=c899e96872187e52f49fcaddf70329bb; CURRENT_FNVAL=80; rpdid=|(umYJmYl|YY0J'uYkJulJlRu; LIVE_BUVID=AUTO5316233083004769; bp_article_offset_624599=535838663859619721; blackside_state=0; bp_t_offset_624599=538253839929827747; CURRENT_QUALITY=116; fingerprint3=019befb9b51d63bea1bc36f915c903b6; fingerprint=869c0ba19aa51e9c14def39d36d7a654; fingerprint_s=abe727279fc5f450f250eed65f1b7fc0; buvid_fp=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; buvid_fp_plain=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; _dfcaptcha=267878eed36e2b05f6295a899fb394e3; bsource=search_baidu; bp_video_offset_624599=545533865337094231; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1625668853,1625855902,1625855960; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1625855960; PVID=24"
}
headers = {
    ':authority': 'api.live.bilibili.com',
    ':method': 'POST',
    ':path': '/msg/send',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuhKB9xaucmJ72Cni',
    'cookie': "_uuid=8B7669FA-FD4E-288D-55F1-57EB7C18555F18668infoc; buvid3=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; sid=8zdnly24; DedeUserID=624599; DedeUserID__ckMd5=faff4574ebdbeb78; SESSDATA=b5c4702c,1638704641,fd08e*61; bili_jct=c899e96872187e52f49fcaddf70329bb; CURRENT_FNVAL=80; rpdid=|(umYJmYl|YY0J'uYkJulJlRu; LIVE_BUVID=AUTO5316233083004769; bp_article_offset_624599=535838663859619721; blackside_state=0; bp_t_offset_624599=538253839929827747; CURRENT_QUALITY=116; fingerprint3=019befb9b51d63bea1bc36f915c903b6; fingerprint=869c0ba19aa51e9c14def39d36d7a654; fingerprint_s=abe727279fc5f450f250eed65f1b7fc0; buvid_fp=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; buvid_fp_plain=C2B98BBA-8FE3-4BCE-85D3-A436F64E955834784infoc; _dfcaptcha=267878eed36e2b05f6295a899fb394e3; bsource=search_baidu; bp_video_offset_624599=545533865337094231; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1625668853,1625855902,1625855960; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1625857982; PVID=29",
    'dnt': '1',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'URL':'https://api.live.bilibili.com/msg/send',
    'Server':'ks-tj-cu-w-06',
    'Date':'2021/07/10 03:57:02'
}
data = {
    'bubble': '0',
    'msg': 'feichangkeai',
    'color': '5566168',
    'mode': '1',
    'fontsize': '25',
    'roomid': '23126288',
    'csrf': 'c899e96872187e52f49fcaddf70329bb',
    'csrf_token': 'c899e96872187e52f49fcaddf70329bb'
}
ndata="color=16777215&fontsize=25&mode=1&msg=信息&roomid=22398978&bubble=0&csrf_token=c899e96872187e52f49fcaddf70329bb&csrf=c899e96872187e52f49fcaddf70329bb"
url = "https://api.live.bilibili.com/msg/send"

ses = req.session()
ses.mount(url, HTTP20Adapter())
time = time.time()
t = int(time)
data['rnd'] = str(t)
req = ses.post(url, data=data,headers=headers)
print(data)
print(req.text)
print("over")
