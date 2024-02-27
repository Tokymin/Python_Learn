# 公司组织了一次考试，现在考试结果出来了，想看一下有没人存在作弊行为，但是员工太多了，需要先对员工进行一次过滤，再进一步确定是否存在作弊行为。过滤的规则为：找到分差最小的员工ID对(p1.p2)列表，要求p1<p2员工个数取值范围：0<n<100000员工ID为整数，取值范围：0<=n<=100000考试成绩为整数，取值范围：0<=score<=300
#
# 输入员工的ID及考试分数
# 5
# 1 90
# 2 91
# 3 95
# 4 96
# 5 100
#
# 5
# 1 90
# 2 91
# 3 92
# 4 85
# 5 86
#
# 7
# 1 90
# 2 91
# 3 92
# 4 85
# 5 86
# 6 90
# 7 90
# 输出分差最小的员工ID对(p1,p2)列表，要求p1<p2。
#
# 每一行代表一个集合,每个集合内的员工ID按顺序排列,多行结果也以员工对中p1值大小升序排列（如果p1相同则p2升序）。

from itertools import combinations


def find_min_diff_pairs(scores):
    # 检查员工的数量是否在给定的范围内
    if not (0 < len(scores) < 100000):
        return "Error"
    # 将员工ID和成绩存入哈希表
    score_dict = {i + 1: scores[i] for i in range(len(scores))}
    # 检查员工ID和考试成绩是否在给定的范围内
    for id, score in score_dict.items():
        if not (0 <= id <= 100000) or not (0 <= score <= 300):
            return "Error."
    # 对成绩进行排序
    sorted_scores = sorted(score_dict.items(), key=lambda x: x[1])
    min_diff = float('inf')
    # 找出分差最小的员工ID对
    # 构建差分数组
    # 构建二维数组，每一行都是一组成绩相同的员工
    pairs = []
    same_score_groups = []
    same_score_group = [sorted_scores[0]]

    for i in range(1, len(sorted_scores)):
        if sorted_scores[i][1] == sorted_scores[i - 1][1]:
            same_score_group.append(sorted_scores[i])
        else:
            same_score_groups.append(same_score_group)
            same_score_group = [sorted_scores[i]]
    if same_score_group:
        same_score_groups.append(same_score_group)

        # 对于每一组成绩相同的员工，生成所有可能的员工ID对
    for same_score_group in same_score_groups:
        for pair in combinations([id for id, score in same_score_group], 2):
            pairs.append(pair)

    if len(pairs) == 0:  # 说明不存在重复的
        for i in range(1, len(sorted_scores)):
            diff = sorted_scores[i][1] - sorted_scores[i - 1][1]
            if diff < min_diff:
                min_diff = diff
                pairs = [(sorted_scores[i - 1][0], sorted_scores[i][0])]
            elif diff == min_diff:
                pairs.append((sorted_scores[i - 1][0], sorted_scores[i][0]))

    # 确保p1 < p2
    pairs = [(p1, p2) if p1 < p2 else (p2, p1) for p1, p2 in pairs]
    # 对结果进行排序
    pairs.sort()
    return pairs


if __name__ == '__main__':
    length = input()
    lis = []
    scores = []
    for i in range(int(length)):
        tmp = list(map(int, input().strip().split()))
        scores.append(int(tmp[1]))
        lis.append(tmp)
    pairs = find_min_diff_pairs(scores)
    for i in range(len(pairs)):
        print(f'{pairs[i][0]} {pairs[i][1]}')
