# 游游现在有a个'y', b个'o', c个'u',他想用这些字母拼成一个字符串。三个相邻的字母是"you"可以获得2分,两个相邻的字母是"00",可以获得1分。问最多可以获得多少分？
# 要求如下：输入描述
# 第一行一个整数q，代表询问次数。
# 接下来q行，每行三个正整数a,b,c，用空格隔开。
# 1<q≤10^5 1≤ a,b,c≤ 10^9
# 举例如下：
# 输入
# 3
# 1 1 1
# 2 3 2
# 1 5 2
# 输出
# 2 4 5解释：
# 第一次询问,可以拼出"you",获得2分。
# 第二次询问,可以拼出"oyouyou",获得4分。
# 第三次询问,可以拼出"uooooyou",获得5分。

def max_score(q, abc):
    results = []
    for i in range(q):
        a, b, c = abc[i]
        total = 0
        # 尽可能地构造"you"
        you = min(a, min(b, c))
        total += you * 2
        a -= you
        b -= you
        c -= you
        # 尽可能地构造"oo"
        oo = min(b // 2, a)
        total += oo
        b -= oo * 2
        results.append(total)
    return results


# q = 3
# abc_list = [[1, 1, 1], [2, 3, 2], [1, 5, 2]]
# print(max_score(q, abc_list))  # 输出：[2, 4, 5]
if __name__ == '__main__':
    q = int(input().strip())
    res = []
    abc = []
    for _ in range(q):
        a, b, c = map(int, input().strip().split())
        abc.append([a, b, c])

    res=max_score(q,abc)
    for score in res:
        print(score)

