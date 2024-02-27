# 1、找磨损度最高和最低的硬盘存储阵列上使用的一批固态硬盘,根据硬盘磨损值给定一个数组endurances,数组中每个元素表示单块硬盘的麻损度(0到10000之间)。磨损度越大,表示此盘需要更换的概率越高。需要找出磨损度最高三块盘下标和磨损度最低的三块盘下标。
# 输入一组硬盘磨损度的数组。说明：(1) 数组endurances中无重复值(2) 数组的长度范围：[6,200]（2）数组的下标从0开始。
# 输出第一行:磨损度最高三块盘下标,按下标升序展示第二行:麻损度最低的三块盘下标,按下标升序展示
# 样例1
# 复制
# 输入：1 50 40 68 72 86 35 14 87 99 63 75
# 输出：5 8 9
# 0 6 7
# 解释：
# 输入：1 50 40 68 72 86 35 14 87 99 63 75：表示一组硬盘磨损度的数组，其中的每个数值表示每个硬盘对应的磨损度。输出：5 8 9:表示磨损度最高三块盘的下标
# 0 6 7：表示磨损度最低的三块盘的下标
def find_disk_of_high_and_low(endurances):
    indexed_endurances = list(enumerate(endurances))
    indexed_endurances.sort(key=lambda x: x[1])
    lowest_three = [x[0] for x in indexed_endurances[:3]]
    highest_three = [x[0] for x in indexed_endurances[-3:]]
    lowest_three.sort()
    highest_three.sort()
    return highest_three, lowest_three


if __name__ == '__main__':
    endurances = list(map(int, input("").split()))
    highest_indices, lowest_indices = find_disk_of_high_and_low(endurances)
    print(" ".join(map(str, highest_indices)))
    print(" ".join(map(str, lowest_indices)))
