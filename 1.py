import random
import time
people = ['kingname', '王小一', '李小二', '张小三', '刘小四', '卢小五', '马小六', '周小七', '丁小八', '朱小九']
for i in range(1, 11):
    lucky_guy = random.choice(people)
    print(f'第{i}次抽奖，中奖用户：{lucky_guy}')
    time.sleep(1)