import json
import logging
import time
import os
from member import Member

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

config = json.load(open('./config.json', 'r', encoding='utf-8'))
refresh_time = config['refresh_time']
member_list = []
# 保存登录成功的对象
for i in config['members']:
    member = Member(i['username'], i['password'])
    member.login(on_success=lambda: member_list.append(member),
                 on_failure=lambda: logger.warning(i['username'] + ' 登录失败'))
# 没有登录成功的账号
if not member_list:
    logger.error('没有登录成功的账号，即将退出')
    os.system('pause')
    exit(1)

while True:
    for i in member_list:
        i.action()
    time.sleep(refresh_time)
