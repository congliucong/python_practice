def reverse(text):
    # ��Ƭ���� seq[a:b]��a��ʼ��λ��b����������Ƭ������������Ϊ����

    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text:")
if is_palindrome(something):
    print("aaaa")
else:
    print("bbb")


# with���
