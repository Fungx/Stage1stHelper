import requests
import logging
import re

logger = logging.getLogger(__name__)


class Member:
    def __init__(self, username, password):
        self.is_login = False
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self, on_success, on_failure):
        data = self.session.post(
            "https://bbs.saraba1st.com/2b/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1",
            data={"username": self.username, "password": self.password},
        ).text
        if "https://bbs.saraba1st.com/2b/./" in data:
            logger.info(self.username + ": 登陆成功")
            self.session.headers.update(
                {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "referer": "https://bbs.saraba1st.com/2b/forum-75-1.html",
                }
            )
            self.is_login = True
            on_success()
        else:
            logger.warning(data)
            on_failure()

    # 发请求保持在线
    def action(self):
        if not self.is_login:
            return
        # 获取用户id
        userid = re.findall('.*(?=%7C)', self.session.cookies.get('B7Y9_2132_lastcheckfeed'))[0]
        # 构造主页url
        home_url = "https://bbs.saraba1st.com/2b/home.php?mod=space&uid={}&do=profile&from=space".format(userid)
        data = self.session.get(home_url).text
        # 访问成功
        if "个人资料" in data:
            score = re.findall("(?<=积分</em>)[0-9]*", data)[0]
            online_time = re.findall("[1-9]* 小时", data)[0]
            logger.info("{}: 刷新 积分: {} 在线时间: {}".format(self.username, score, online_time))
