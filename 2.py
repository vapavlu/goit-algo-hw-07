class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def find_min_value(root):
    if root is None:
        return float('inf')
    
    current = root
    while current.left is not None:
        current = current.left
    
    return current.value

# Приклад використання
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)

print(find_min_value(root))  # Виведе 2

