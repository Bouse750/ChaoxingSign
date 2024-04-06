import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            "Referer": "https://passport2.chaoxing.com",
                "Origin": "https://passport2.chaoxing.com",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                        "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": "Windows",
                                "Sec-Fetch-Dest": "empty",
                                    "Sec-Fetch-Mode": "cors",
                                        "Sec-Fetch-Site": "same-origin"
                                        
}

url = "https://passport2-static.chaoxing.com/js/common/crypto-js.min.js"

r = requests.get(url,headers=headers)
with open("crypto.js","w") as f:
    f.write(r.text)