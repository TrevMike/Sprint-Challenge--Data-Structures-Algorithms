class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# there are two directions left and right i will use this to 
# go both ways. 

#  def make_incrementor(n):
#      return lambda x: x + n
#      f = make_incrementor(42)
#      f(0)
#      f(1)

# so the method has to solve it like solving a maze has to go
# to different directions and not go there again intill the 
# the whole thing is solved. 

# https://en.wikipedia.org/wiki/Depth-first_search
# https://medium.com/@bethqiang/abstract-data-types-data-structures-440ef051dbdc

# BinarySearchTree.prototype.depthFirstForEach = function(iterator, order) {
#   if (order === 'pre-order') {
#     iterator(this.value); <-- need this.
#   }
#   if (this.left) {
#     this.left.depthFirstForEach(iterator, order); <-- need this
#   }
#   if (!order || order === 'in-order') {
#     iterator(this.value);
#   }
#   if (this.right) {
#     this.right.depthFirstForEach(iterator, order); <--- need this.
#   }
#   if (order === 'post-order') {
#     iterator(this.value);
#   }
# };

  def depth_first_for_each(self, cb):
    # pass
    cb(self.value)

    if self.left:
      self.left.depth_first_for_each(cb)
    
    if self.right:
      self.right.depth_first_for_each(cb)


    
  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
