# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=dict(), code=''):
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code + '0')
    get_code(head.right, codes, code + '1')
    return codes


def get_tree(temp):
    count_str = Counter(temp)
    if len(count_str) <= 1:
        node = Node(None)
        if len(count_str) == 1:
            node.left = Node(count_str[0])
            node.right = None
        count_str = {node: 1}
    print(count_str)
    print(count_str.most_common())
    while len(count_str) != 1:
        node = Node(None)
        spam = count_str.most_common()[:-3:-1]
        print(spam)
        node.left = spam[0][0]
        node.right = spam[1][0]
        del count_str[spam[0][0]]
        del count_str[spam[1][0]]
        count_str+={node: spam[0][1] + spam[1][1]}
        print(count_str,node.value)
    #count_str.most_common()[0][0].value = ''
    print(count_str.elements())
    #print(count_str[0][0].)
    return Node(count_str)

#dist=get_code(get_tree("beep boop huoo"))
get_tree("beep boop huoo")
#print(dist)