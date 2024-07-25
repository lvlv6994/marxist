import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, help='转换文件')
args = parser.parse_args()

with open(f'{args.file}','r') as file:
    content = file.read()

# 要发送POST请求的URL
url = 'https://luvvoice.xyz/text_to_speech'

# 表单数据
form_data = {
    'text': f'{content}',
    'language_code': 'zh-CN-YunyangNeural',
}

# 请求头
headers = {
    'Origin':'https://luvvoice.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':"macOS",
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'cross-site',
    'Sec-Gpc':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}


# 发送POST请求
response = requests.post(url, data=form_data,headers=headers)

# 检查响应状态码
if response.status_code == 200:
    print(response.json()['result_audio_url'])
else:
    print(f'Failed to submit form. Status code: {response.status_code} \n{response.text}')




