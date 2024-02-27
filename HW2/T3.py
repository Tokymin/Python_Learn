# 有一道动态规划的题目，平面灯阵中寻找最大正方形边界
# 现在有一个二维数组来模拟一个平面灯阵，平面灯阵中每个位置灯处于点亮或熄灭，分别对应数组每个元素取值只能为1或0，现在需要找一个正方形边界，其每条边上的灯都是点亮(对应数组中元素的值为1)的，且该正方形面积最大。
#
# 第一行为灯阵的高度(二维数组的行数)第二行为灯阵的宽度(二维数组的列数)
# 紧接着为模拟平台灯阵的二维数组
# arr1<arr.length<=200
# 1<arr[o]length<=200
# 样例输入：
# 4
# 5
# 1 0 0 0 1
# 1 1 1 1 1
# 1 0 1 1 0
# 1 1 1 1 1
#
#
# 3
# 3
# 1 0 0
# 0 1 0
# 0 0 1
#
# 输出是返回满足条件的面积最大正方形边界信息。返回信息[r,c,w],其中,c分别代表方阵右下角的行号和列号，w代表正方形的宽度。如果存在多个满足条件的正方形，则返回r最小的，若r相同，返回c最小的正方形。

# include <iostream>
# include <vector>
# include <algorithm>

# using namespace std;
#
# vector < int > largest1BorderedSquare(vector < vector < int >> & grid)
# {
#     int
# m = grid.size(), n = grid[0].size();
# vector < vector < int >> rs(m, vector < int > (n + 1)), cs(n, vector < int > (m + 1));
# for (int i = 0; i < m; ++i)
# for (int j = 0; j < n; ++j) {
#     rs[i][j + 1] = rs[i][j] + grid[i][j]; // 每行的前缀和
# cs[j][i + 1] = cs[j][i] + grid[i][j]; // 每列的前缀和
# }
# for (int d = min(m, n); d; --d) // 从大到小枚举正方形边长 d
# for (int i = 0; i <= m - d; ++i)
# for (int j = 0; j <= n - d; ++j) // 枚举正方形左上角坐标 (i, j)
# if (rs[i][j + d] - rs[i][j] == d & & // 上边
# cs[j][i + d] - cs[j][i] == d & & // 左边
# rs[i + d - 1][j + d] - rs[i + d - 1][j] == d & & // 下边
# cs[j + d - 1][i + d] - cs[j + d - 1][i] == d) // 右边
# return {i + d - 1, j + d - 1, d};
# return {};
# }
#
# int
# main()
# {
# int
# height, width;
# cin >> height >> width;
#
# // 输入模拟平台灯阵的二维数组
# vector < vector < int >> matrix(height, vector < int > (width));
# for (int i = 0; i < height; ++i) {
# for (int j = 0; j < width; ++j) {
# cin >> matrix[i][j];
# }
# }
#
# // 调用函数，获取最大正方形的边界信息
# vector < int > result = largest1BorderedSquare(matrix);
#
# // 输出最大正方形的边界信息
# cout << "[";
# for (int i = 0;i < result.size() - 1; i++) {
# cout << result[i] << ", ";
# }
# cout << result[result.size() - 1] << "]";
#
# // cout << largest1BorderedSquare(matrix);
#
# return 0;
# }
