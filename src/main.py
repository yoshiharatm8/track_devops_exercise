def add(a, b, c=0):
    # 型チェック（int/floatのみ許可）
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return -1

    # 境界値チェック（0 <= x <= 10）
    if not (0 <= a <= 10) or not (0 <= b <= 10) or not (0 <= c <= 10):
        return -2

    return a + b + c
