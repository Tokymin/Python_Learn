# http网关在一个系统中起看非常关键的作用。网关经常需要根据某些请求URL来定义一些处理规则，当请求进来时需要根据请求URL匹配到对应的规则。定义规则时，URL的匹配方式可以是完整匹配或前缓匹配;当同一请求与多个规则相匹配时，取匹配长度最长的那一条规则。
#
# 输入：匹配规则列表及待匹配的请求URL列表，格式定义：第一行表示待匹配的规则个数，取值范围：0<m<100000。后续的行紧跟着定义的规则，格式为：匹配方式+空格+URL，匹配方式取值约束：prefix前缀匹配、exact精确匹配后续的行表示待匹配的URL，URL个数y取值范围：O<y<3000。每个规则中待匹配的URL段(将URL按/分隔后的字符串称为URL段)个数n取值范围: 0<n<50,每个URL段字符串长度范围: 0<x<50
#
# 输出：每一行表示每个待匹配的URL匹配上的规则信息列表,若无规则匹配，则返回(null)

def match_rules(rules, urls):
    # 创建字典存储规则
    rule_dict = {}
    for rule in rules:
        match_type, url = rule.split()
        rule_dict[url] = match_type
    # 对规则按长度降序排序
    sorted_rules = sorted(rule_dict.items(), key=lambda x: len(x[0]), reverse=True)
    result = []
    for url in urls:
        # 初始化匹配规则为null
        match_rule = '(null)'
        for rule, match_type in sorted_rules:
            # 如果规则匹配
            if (match_type == 'prefix' and url.startswith(rule)) or (match_type == 'exact' and url == rule):
                match_rule = rule
                break
        result.append(match_rule)
    return result


if __name__ == '__main__':
    length = input()
    scores = []
    for i in range(int(length)):
        tmp = list(map(int, input().strip().split()))
        scores.append(int(tmp[1]))
    # pairs = find_pairs(scores, int(length))

    match_rules()
    for i in range(len(pairs)):
        print(f'{pairs[i][0]} {pairs[i][1]}')

