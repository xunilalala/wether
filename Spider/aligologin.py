from aligo import Aligo
import time
if __name__ == '__main__':
    # 详情请查看源码中的文档字符串
    ali = Aligo(email=('3120294679@qq.com', 'GITHUB'))
    user = ali.get_user()
    print(user.user_id, user.user_name, user.nick_name)
time.sleep(30)
