#定义二叉树中的节点
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

#定义二叉树类
class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

#先序遍历
def preOrder(retList,node):
    if node != None:
        #访问根节点
        retList.append(node)
        #遍历左子树
        preOrder(retList, node.left)
        #遍历右子树
        preOrder(retList, node.right)
    return retList

#中序遍历
def inOrder(retList,node):
    if node != None:
        #遍历左子树
        inOrder(retList, node.left)
        #访问根节点
        retList.append(node)
        #遍历右子树
        inOrder(retList, node.right)
    return retList

#后序遍历
def postOrder(retList,node):
    if node != None:
        #遍历左子树
        postOrder(retList, node.left)
        #遍历右子树
        postOrder(retList, node.right)
        #访问根节点
        retList.append(node)
    return retList


if __name__ == '__main__':
    #二叉树演示
    print('--------begin---------')
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9,left=TreeNode(6,left=TreeNode(3),right=TreeNode(8)),right=TreeNode(10))
    rootNode.right = TreeNode(17,left=TreeNode(12),right=TreeNode(19))
    bTree = BinaryTree(rootNode)
    ret = preOrder([], bTree.root)
    for i in ret:
        print(i.val, end=' ')
    print('---------inorder-------')
    ret = inOrder([],bTree.root)
    for i in ret:
        print(i.val, end=' ')
    print('----------postOrder--------')
    ret = postOrder([],bTree.root)
    for i in ret:
        print(i.val, end=' ')

