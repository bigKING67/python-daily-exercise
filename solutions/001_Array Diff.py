def array_diff(arr1, arr2):
    """
    返回两个数组中只出现在其中一个数组中的元素，按字母顺序排序
    
    Args:
        arr1: 第一个字符串数组
        arr2: 第二个字符串数组
    
    Returns:
        包含只在一个数组中出现的元素的新数组（按字母顺序排序）
    """
    set1 = set(arr1)
    set2 = set(arr2)
    
    # 计算对称差集：(set1 - set2) ∪ (set2 - set1)
    symmetric_diff = (set1 - set2) | (set2 - set1)
    
    # 转换为列表并按字母顺序排序
    return sorted(list(symmetric_diff))
