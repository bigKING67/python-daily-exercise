def get_words(paragraph):
    """
    返回段落中出现频率最高的前三个单词
    
    Args:
        paragraph (str): 输入的段落文本
        
    Returns:
        list: 包含前三个最频繁单词的列表，按频率降序排列，小写
    """
    if not paragraph:
        return []
    
    # 预处理：转小写并清楚标点符号
    text = paragraph.lower()
    for punt in ',.!':
        text = text.replace(punt, ' ')

    # 分割并过滤有效的单词
    words = [word for word in text.split() if word ]

    # 统计词频：单词及出现次数
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # 按频率排序并取前3个，items（）返回了可迭代对象，构成是元组。是为了拿到键值对，字典迭代只有键
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # 提取单词并限制数量，元组解包
    return [word for word, count in sorted_words[:3]]