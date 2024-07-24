class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_values(root):
    if root is None:
        return 0
    return root.value + sum_of_values(root.left) + sum_of_values(root.right)

# Приклад використання
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.right.right = TreeNode(30)

print(sum_of_values(root))  # Виведе 67
