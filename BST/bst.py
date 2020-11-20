class BinarySearchTree:

   # Initialization
   def __init__(self):
      self._size = 0
      self._root = None

   class _Node:
      def __init__(self,key,value):
         self.left = None
         self.right = None
         self.key = key
         self.value = value

   # (a) Calculate size of BST (no. of nodes)
   def size(self):
      return self._size

   # (b) Adding a node to BST
   def add(self, key, value):
      self._size += 1
      node = self._Node(key,value) # Node instance
      if self._root is None:
         self._root = node
      else:
         root = self._root
         while(root is not None):
            if(key< root.key):
               if(root.left is None):
                  root.left = node
                  break
               else:
                  root = root.left
            else:
               if(root.right is None):
                  root.right = node
                  break
               else:
                  root = root.right

   # (c) Searching for a requested key
   def search(self, key):
      root = self._root
      if(root is None):
         print ("The Tree is empty!")
         return None
      else:
         while (root is not None):
            if (key == root.key):
               return root.value
            if(key < root.key):
               root = root.left

            else:
               root = root.right
      return False

   # (d) Find the smallest key
   def smallest(self):
      root = self._root
      if(root is None):
         print ("The tree is empty")
         return None
      else:
         while (root.left is not None):
            root = root.left
      return (root.key,root.value)

   # (e) Find the largest key
   def largest(self):
      root = self._root
      if(root is None):
         print ("The tree is empty")
         return None
      else:
         while (root.right is not None):
            root = root.right
      return (root.key,root.value)

   # (f) Remove a key from the BST
   def remove(self, key):
      previous = self._root
      root = self._root
      if(root is None):
         print ("The tree is empty")
         return None
      while root is not None:
         if root.key == key:
            self._size -= 1
            if root.left is None and root.right is None: # Implies Leaf Node
               print("Leaf Node")
               print(previous.key)
               if key < previous.key:
                  previous.left = None
                  root = None
               else:
                  previous.right = None
                  root = None
            else:
               if root.right is None: #Only has One Child
                  print("One Child")
                  if key < previous.key: #Left Child
                     previous.left = root.left
                     root = None
                  else: #Right Child
                     previous.right = root.left
                     root = None
               else: #Both Child is Present
                  print("Both Child")
                  temp = root.right
                  temp_prev = root
                  while temp.left is not None: #Find Inorder Successor
                     temp_prev = temp
                     temp = temp.left
                  root.key = temp.key
                  root.value = temp.value

                  if(temp.key < temp_prev.key):
                     temp_prev.left = None
                  else:
                     temp_prev.right = None
            return ("Node Removed from Tree")   
         elif key < root.key:
            previous = root
            root = root.left
         elif key > root.key:
            previous = root
            root = root.right
      return False

   # (g) Inorder Traversal
   def inorder_walk(self):
      list=[]
      if (self._root==None):
         print ("EMPTY TREE")
         return None
      else:
         self._inorder_traversal(self._root,list)
      return list

   def _inorder_traversal(self,root,list):
      if root is not None:
         self._inorder_traversal(root.left,list)
         list.append(root.key)
         self._inorder_traversal(root.right,list)
      return list

   # (h) Postorder Traversal
   def postorder_walk(self):
      list=[]
      if (self._root==None):
         print ("EMPTY TREE")
         return None
      else:
         self._postorder_traversal(self._root,list)
      return list

   def _postorder_traversal(self,root,list):
      if root is not None:
         self._postorder_traversal(root.left,list)
         self._postorder_traversal(root.right,list)
         list.append(root.key)
      return list

   # (i) Preorder Traversal
   def preorder_walk(self):
      list=[]
      if (self._root==None):
         print ("EMPTY TREE")
         return None
      else:
         self._preorder_traversal(self._root,list)
      return list

   def _preorder_traversal(self,root,list):
      if root is not None:
         list.append(root.key)
         self._preorder_traversal(root.left,list)
         self._preorder_traversal(root.right,list)
      return list