def reverse_sentence(sentence):
    """
    将句子中的单词顺序反转。
    
    Args:
        sentence (str): 包含多个单词的字符串，单词间可能有多个空格
        
    Returns:
        str: 单词顺序反转后的字符串，单词间只用单个空格分隔
        
    示例:
        >>> reverse_sentence("world hello")
        'hello world'
        >>> reverse_sentence("npm  install   apt    sudo")
        'sudo apt install npm'
    """
    # 处理空输入的边界情况
    if not sentence:
        return ""
    
    # 将句子分割成单词列表（自动处理多个空格）
    words = sentence.split()
    
    # 反转单词列表
    reversed_words = words[::-1]
    
    # 用单个空格连接反转后的单词
    return " ".join(reversed_words)
