class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return ('Node(' + repr(self.val) + ', '
                        + repr(self.left) + ', '
                        + repr(self.right) + ')')

    def __eq__(self, other):
        if isinstance(other, Node):
            return ( self.val == other.val and
                     self.left == other.left and
                     self.right == other.right )
        return False

serialize = repr
deserialize = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)) == node
