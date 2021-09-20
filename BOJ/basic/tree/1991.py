"""
- BOJ
- CDR
- 트리, 전위 중위 후위 순회 문제
"""
N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])     # left
        preorder(tree[root][1])     # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])      # left
        print(root, end='')
        inorder(tree[root][1])      # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])    # left
        postorder(tree[root][1])    # right
        print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
