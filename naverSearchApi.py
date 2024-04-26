from urllib.request import *
from urllib.parse import quote
import json
import datetime

class NaverApi:  # 바로 함수로 불러올 것이기 때문에 초기화자 필요없음
    def getRequestUrlCode(self, url):  # 매개변수 url 삽입
        requestUrl = Request(url)

        client_id = "O_igCnhFYt7TFIXPCFJn"
        client_secret = "m7xL385EiZ"

        requestUrl.add_header("X-Naver-Client-Id",client_id)
        requestUrl.add_header("X-Naver-Client-Secret",client_secret)

        naverResult = urlopen(requestUrl)  # 네이버에서 요청에 의한 결과(응답)를 반환

        if naverResult.getcode()  == 200:  # 응답결과가 정상
            print(f"네이버 api 요청 정상 진행 : {datetime.datetime.now()}")
            return naverResult.read().decode('utf-8')
            # 응답결과가 정상이면 네이버에서 받은 결과를 utf-8로 인코딩해서 반환
        else:
            print(f"네이버 api 요청 정상 진행 : {datetime.datetime.now()}")
            return None
            # 응답결과가 에러이면 아무것도 반환하지 않음

    def getNaverSearch(self, node, keyword, start, display):
        baseUrl = "https://openapi.naver.com/v1/search/"  # 네이버 api 기본 url
        node = f"{node}.json"
        params = f"?query={quote(keyword)}&start={start}&display={display}"

        url = baseUrl+node+params

        result = self.getRequestUrlCode(url)

        if result != None:  # 네이버에서 결과가 정상적으로 도착
            return json.loads(result)  # json 형태로 변환해서 반환
        else:
            print("네이버 응답 실패! 에러발생!")
            return None




