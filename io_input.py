def reverse(text):
    # 切片功能 seq[a:b]从a开始到位置b结束进行切片，第三个参数为步长

    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text:")
if is_palindrome(something):
    print("aaaa")
else:
    print("bbb")


# with语句
