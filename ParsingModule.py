# 파싱 모듈
import urllib.request
import json

KEY = "54f5080eba13432083e57d1ea07e26c0"
Type = "json"
pIndex = 1
pSize = 100

SCHOOL_INFORMATION_URL = "https://open.neis.go.kr/hub/schoolInfo?"

URL = SCHOOL_INFORMATION_URL + "Type=" + Type + "&" + "KEY=" + KEY + "&" + "pIndex=" + str(pIndex) + "&" + "pSize=" + str(pSize)
print(URL)
request = urllib.request.urlopen(URL)
response = request.readline()
responseJson = json.loads(response)
print(responseJson)