# Stage1st巨魔助手

**自动登录账号挂权限，方便 ~~爱讨论、钓鱼、巨魔~~**



## 使用方法
1. 修改config.json中的配置，refresh_time为每次刷新的时间间隔，测试过300s不会被离线。members中可以填入多个账号，可以按需要添加。
```json
{
    "refresh_time": 1800,
    "members": [
        {
            "username":"你的用户名",
            "password":"你的密码"
        },
        {
            "username":"你的用户名2",
            "password":"你的密码2"
        }
    ]
}
```
2. 执行start.py。
```shell
python start.py
```
