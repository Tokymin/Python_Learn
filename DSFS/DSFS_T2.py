# 已知n个箱子的长、宽和高。请设计算法,计算将箱子堆起来的最大高度（上面箱子的宽度和长度必须小于下面的箱子,且箱子不能旋转)。
#
# 输入描述
# 第一行一个整数n,表示箱子的数量。
# 接下来n行每行三个整数l_i,w_i,h_i表示箱子的长宽高，用空格分开。
# 1<n< 3000,
# 1 <l_i,w_i,h_i <3000
#
# 输出是一个整数，表示答案。
#
# 示例 1
# 输入
# 3
# 1 1 1
# 2 2 2
# 1 2 4
# 输出
# 4


def max_stack_height(boxes):
    # 不考虑不同方向
    extended_boxes = [(l, w, h) for l, w, h in boxes]
    # 根据宽度和长度降序排序箱子
    # 如果宽度相同，则按长度降序排序
    extended_boxes.sort(key=lambda x: (-x[1], -x[0]))

    n = len(extended_boxes)
    dp = [0] * n
    # 初始化，每个箱子单独使用时的高度
    for i in range(n):
        dp[i] = extended_boxes[i][2]

    for i in range(1, n):# 动态规划
        for j in range(i):
            # 如果箱子j可以放在箱子i上
            if extended_boxes[j][0] > extended_boxes[i][0] and extended_boxes[j][1] > extended_boxes[i][1]:
                dp[i] = max(dp[i], dp[j] + extended_boxes[i][2])
    # 最大高度
    return max(dp)

if __name__ == '__main__':
    q = int(input().strip())
    res = []
    boxes = []
    for _ in range(q):
        a, b, c = map(int, input().strip().split())
        boxes.append([a, b, c])

    max_height=max_stack_height(boxes)
    print(max_height)
