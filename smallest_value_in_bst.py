class Tree:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def get_tree(arr):
  if len(arr) is None:
    return None

  if len(arr) == 1:
    return Tree(arr[0])

  mid = int(len(arr)/2)
  
  root = Tree(arr[mid])
  root.left = get_tree(arr[:mid])
  print (arr[:mid], arr[mid], arr[mid+1:])
  if len(arr) == 2:
    return root
  root.right = get_tree(arr[mid+1:])

  return root

def inorder(tree, k):
  while tree.left:
      tree = tree.left
  return (tree.val)

sorted_array = [5,6,7,12,23,31,44,56,65,99, 100]
print(inorder(get_tree(sorted_array), 3))
