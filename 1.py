class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return float('-inf')
    
    current = root
    while current.right is not None:
        current = current.right
    
    return current.value

# Приклад використання
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.right = TreeNode(30)

print(find_max_value(root))  # Виведе 30
