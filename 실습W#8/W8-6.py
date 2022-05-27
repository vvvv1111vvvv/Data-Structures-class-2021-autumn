'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.04

1. 목적: 트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 8.6 :  이진트리의 좌우를 대칭시키는 연산을 구현하라
3. 방법 : 8.3절의 함수와 테스트 코드를 사용한다..

알고리즘
#1. TreeNode()클라스의 data를 링크를 통해 연결한다.
#2. reverse()메소드를 호출하여 root를 입력
    #2-1  root가 없으면 None을 반환
    #2-2. 좌우 링크를 교환
    #2-3. 자식 노드에 대해 재귀함수 호출
    #2-3. root를 반환
#3. printTree()메소드를 호출하여 root를 입력
    #3-1. 루트를 출력
    #3-2. 왼쪽 자식이 존재하면 재귀함수 호출
    #3-3. 오른쪽 자식이 존재하면 재귀함수 호출


'''

class TreeNode:                 #이진트리를 위한 노드클래스
    def __init__(self, data):  #생성자
        self.data = data                    #노드의 데이타
        self.left = None                    #왼쪽 자식을 위한 링크
        self.right = None                   # 오른쪽 자식을 위한 링크
def reverse(root):

    if root is None:            #root가 없으면
        return None             # None을 반환

    root.left, root.right = root.right, root.left   #좌우 링크를 교환

    reverse(root.left)          #자식 노드에 대해 재귀함수 호출
    reverse(root.right)

    return root
def printTree(root):            #전위순회 VLR
    print(root.data)             #루트를 출력
    if root.left:               #왼쪽 자식이 존재하면
        printTree(root.left)    #재귀함수 호출
    if root.right:              #오른쪽 자식이 존재하면
        printTree(root.right)   #재귀함수 호출
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('E')
root.left.left = TreeNode('C')
root.left.right = TreeNode('D')
root.right.right = TreeNode('F')
reverse(root)
printTree(root)