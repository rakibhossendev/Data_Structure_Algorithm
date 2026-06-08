mkdir -p /home/claude/ds_guide && cat > /home/claude/ds_guide/generate.py << 'PYEOF'
#!/usr/bin/env python3
"""Generate Data Structures Complete Guide HTML"""

# ─────────────────────────────────────────────
# ALL PYTHON CODE EXAMPLES
# ─────────────────────────────────────────────

codes = {}

codes['stack_impl'] = '''
class Stack:
    def __init__(self):
        self.items = []   # empty list দিয়ে শুরু

    def push(self, item):
        """Stack এ element যোগ করো — O(1)"""
        self.items.append(item)

    def pop(self):
        """Top element বের করো — O(1)"""
        if not self.is_empty():
            return self.items.pop()
        return "Stack খালি!"

    def peek(self):
        """Top element দেখো, বের না করে — O(1)"""
        if not self.is_empty():
            return self.items[-1]
        return "Stack খালি!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack: [খালি]")
            return
        print("Stack (Top → Bottom):", self.items[::-1])


# ──── ব্যবহার ────
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()           # Stack (Top → Bottom): [30, 20, 10]
print(s.peek())       # 30
print(s.pop())        # 30
s.display()           # Stack (Top → Bottom): [20, 10]
print("Size:", s.size())    # Size: 2
print("Empty?", s.is_empty())  # Empty? False
'''

codes['stack_p1'] = '''
# Problem 1: Balanced Parentheses Checker
# Input: "((){}[])"  → True
# Input: "({[})"     → False

def is_balanced(expr):
    stack = []
    opening = "({["
    closing = ")}]"
    pair = {")": "(", "}": "{", "]": "["}

    for ch in expr:
        if ch in opening:
            stack.append(ch)          # opening → stack এ রাখো
        elif ch in closing:
            if not stack:             # stack খালি মানে unmatched closing
                return False
            if stack[-1] != pair[ch]: # মিলছে না
                return False
            stack.pop()               # matched pair বের করো

    return len(stack) == 0            # সব মিললে stack খালি


# Test
print(is_balanced("((){}[])"))   # True
print(is_balanced("({[})"))      # False
print(is_balanced("{[()]}"))     # True
print(is_balanced("((()"))       # False
print(is_balanced(""))           # True
'''

codes['stack_p2'] = '''
# Problem 2: Stack ব্যবহার করে String Reverse করো
# Input:  "Rakib"
# Output: "bikaR"

def reverse_string(s):
    stack = []

    # Step 1: প্রতিটি character push করো
    for ch in s:
        stack.append(ch)

    # Step 2: একে একে pop করে নতুন string বানাও
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# Test
print(reverse_string("Rakib"))       # bikaR
print(reverse_string("Python"))      # nohtyP
print(reverse_string("racecar"))     # racecar (palindrome!)
print(reverse_string("12345"))       # 54321
'''

# ─── QUEUE ───
codes['queue_impl'] = '''
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()   # deque ব্যবহার করি — দুদিক থেকে O(1) অ্যাক্সেস

    def enqueue(self, item):
        """Queue এর পেছনে element যোগ করো — O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Queue এর সামনে থেকে element বের করো — O(1)"""
        if not self.is_empty():
            return self.items.popleft()
        return "Queue খালি!"

    def front(self):
        """সামনের element দেখো — O(1)"""
        if not self.is_empty():
            return self.items[0]
        return "Queue খালি!"

    def rear(self):
        """পেছনের element দেখো — O(1)"""
        if not self.is_empty():
            return self.items[-1]
        return "Queue খালি!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue (Front → Rear):", list(self.items))


# ──── ব্যবহার ────
q = Queue()
q.enqueue("রাকিব")
q.enqueue("সাকিব")
q.enqueue("তামিম")
q.display()             # Queue (Front → Rear): ['রাকিব', 'সাকিব', 'তামিম']
print(q.front())        # রাকিব
print(q.dequeue())      # রাকিব
q.display()             # Queue (Front → Rear): ['সাকিব', 'তামিম']
print("Size:", q.size())  # Size: 2
'''

codes['queue_p1'] = '''
# Problem 1: ১ থেকে N পর্যন্ত Binary Numbers তৈরি করো
# Input: N = 5
# Output: ["1", "10", "11", "100", "101"]

from collections import deque

def generate_binary_numbers(n):
    result = []
    q = deque()
    q.append("1")   # "1" দিয়ে শুরু

    for _ in range(n):
        front = q.popleft()
        result.append(front)
        # বাঁয়ে 0 যোগ করলে → পরের even number
        q.append(front + "0")
        # বাঁয়ে 1 যোগ করলে → পরের odd number
        q.append(front + "1")

    return result


# Test
for i, b in enumerate(generate_binary_numbers(10), 1):
    print(f"{i} = {b}")
# 1=1, 2=10, 3=11, 4=100, 5=101, ...
'''

codes['queue_p2'] = '''
# Problem 2: ২টি Queue দিয়ে Stack তৈরি করো

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()   # main queue
        self.q2 = deque()   # helper queue

    def push(self, item):
        """O(n) — push করার সময় সব উল্টে দাও"""
        self.q2.append(item)
        # q1 এর সব element q2 তে নিয়ে যাও
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap করো
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """O(1) — সামনে থেকেই বের হয়"""
        if self.q1:
            return self.q1.popleft()
        return "Stack খালি!"

    def top(self):
        if self.q1:
            return self.q1[0]
        return "Stack খালি!"

    def is_empty(self):
        return len(self.q1) == 0


# Test
s = StackUsingQueue()
s.push(1); s.push(2); s.push(3)
print(s.top())   # 3 (LIFO order)
print(s.pop())   # 3
print(s.pop())   # 2
print(s.top())   # 1
'''

# ─── HEAP ───
codes['heap_impl'] = '''
import heapq

class MinHeap:
    """Python এর heapq module Min Heap implement করে"""
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Element insert করো — O(log n)"""
        heapq.heappush(self.heap, val)

    def extract_min(self):
        """সবচেয়ে ছোট element বের করো — O(log n)"""
        if self.heap:
            return heapq.heappop(self.heap)
        return "Heap খালি!"

    def get_min(self):
        """সবচেয়ে ছোট element দেখো — O(1)"""
        if self.heap:
            return self.heap[0]
        return "Heap খালি!"

    def size(self):
        return len(self.heap)

    def display(self):
        print("Heap:", self.heap)


class MaxHeap:
    """Max Heap: value কে negative করে store করো"""
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Negative করে push করলে max heap হয় — O(log n)"""
        heapq.heappush(self.heap, -val)

    def extract_max(self):
        """সবচেয়ে বড় element — O(log n)"""
        if self.heap:
            return -heapq.heappop(self.heap)
        return "Heap খালি!"

    def get_max(self):
        """সবচেয়ে বড় দেখো — O(1)"""
        if self.heap:
            return -self.heap[0]
        return "Heap খালি!"


# ──── ব্যবহার ────
print("── Min Heap ──")
mn = MinHeap()
for v in [5, 3, 8, 1, 9, 2]:
    mn.insert(v)
mn.display()              # Heap: [1, 3, 2, 5, 9, 8]
print(mn.extract_min())   # 1
print(mn.extract_min())   # 2

print("\\n── Max Heap ──")
mx = MaxHeap()
for v in [5, 3, 8, 1, 9, 2]:
    mx.insert(v)
print(mx.get_max())        # 9
print(mx.extract_max())    # 9
print(mx.extract_max())    # 8
'''

codes['heap_p1'] = '''
# Problem 1: Array থেকে K-টি সবচেয়ে বড় element খুঁজো
# Input: arr = [3, 2, 1, 5, 6, 4], k = 3
# Output: [6, 5, 4]

import heapq

def k_largest(arr, k):
    """
    পদ্ধতি: K size এর Min Heap রাখো।
    যদি heap full হয় এবং নতুন element বড় হয়
    তাহলে সবচেয়ে ছোটটা বের করে নতুনটা ঢোকাও।
    """
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)   # ছোটটা বাদ দাও

    # Heap এ এখন K-টি সবচেয়ে বড় আছে
    return sorted(min_heap, reverse=True)


# Test
arr = [3, 2, 1, 5, 6, 4]
print(k_largest(arr, 3))   # [6, 5, 4]
print(k_largest(arr, 2))   # [6, 5]

arr2 = [7, 10, 4, 3, 20, 15]
print(k_largest(arr2, 4))  # [20, 15, 10, 7]
'''

codes['heap_p2'] = '''
# Problem 2: K টি Sorted Array Merge করো
# Input: [[1,4,7], [2,5,8], [3,6,9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

import heapq

def merge_k_sorted(arrays):
    """
    প্রতিটি array এর প্রথম element heap এ রাখো।
    Heap থেকে সবচেয়ে ছোটটা বের করো,
    সেই array এর পরের element heap এ দাও।
    """
    result = []
    # heap এ: (value, array_index, element_index)
    min_heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][next_idx]
            heapq.heappush(min_heap, (next_val, arr_idx, next_idx))

    return result


# Test
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge_k_sorted(arrays))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

arrays2 = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
print(merge_k_sorted(arrays2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# ─── LINKED LIST ───
codes['ll_impl'] = '''
class Node:
    def __init__(self, data):
        self.data = data    # data store করে
        self.next = None    # পরের node এর pointer


class LinkedList:
    def __init__(self):
        self.head = None    # শুরু খালি

    def append(self, data):
        """শেষে node যোগ করো — O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:      # শেষ node খুঁজো
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """শুরুতে node যোগ করো — O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """নির্দিষ্ট data এর node মুছো — O(n)"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next   # bypass করো
                return
            current = current.next

    def search(self, data):
        """Data খুঁজো — O(n)"""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return f"পাওয়া গেছে, index: {index}"
            current = current.next
            index += 1
        return "পাওয়া যায়নি"

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements) + " → NULL")


# ──── ব্যবহার ────
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.display()          # 5 → 10 → 20 → 30 → NULL
print(ll.search(20))  # পাওয়া গেছে, index: 2
ll.delete(10)
ll.display()          # 5 → 20 → 30 → NULL
print("Length:", ll.length())  # Length: 3
'''

codes['ll_p1'] = '''
# Problem 1: Linked List Reverse করো
# Input:  1 → 2 → 3 → 4 → 5 → NULL
# Output: 5 → 4 → 3 → 2 → 1 → NULL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_ll(head):
    """
    ৩টি pointer ব্যবহার করো:
    prev, current, next_node
    প্রতিটি step এ arrow উল্টো করো।
    """
    prev = None
    current = head

    while current:
        next_node = current.next   # পরেরটা মনে রাখো
        current.next = prev        # arrow উল্টো করো
        prev = current             # prev এগাও
        current = next_node        # current এগাও

    return prev   # নতুন head


def build_ll(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head

def print_ll(head):
    els = []
    while head:
        els.append(str(head.data))
        head = head.next
    print(" → ".join(els) + " → NULL")


# Test
head = build_ll([1, 2, 3, 4, 5])
print("Original:", end=" ")
print_ll(head)
head = reverse_ll(head)
print("Reversed:", end=" ")
print_ll(head)   # 5 → 4 → 3 → 2 → 1 → NULL
'''

codes['ll_p2'] = '''
# Problem 2: Linked List এ Cycle আছে কিনা বের করো
# Floyd's Cycle Detection Algorithm (Tortoise & Hare)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    """
    ২টি pointer:
    - slow: প্রতি step এ ১ টা এগোয়
    - fast: প্রতি step এ ২ টা এগোয়
    যদি cycle থাকে, fast কখনো slow কে ধরে ফেলবে।
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # ১ step
        fast = fast.next.next   # ২ step

        if slow == fast:        # মিলে গেলে cycle আছে
            return True

    return False   # fast NULL পৌঁছে গেলে cycle নেই


# Test — cycle তৈরি করো
n1 = Node(1); n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5)
n1.next = n2; n2.next = n3; n3.next = n4
n4.next = n5

print(has_cycle(n1))   # False (no cycle)

n5.next = n3           # cycle: 5 → 3 (cycle তৈরি)
print(has_cycle(n1))   # True
'''

# ─── TREE ───
codes['tree_impl'] = '''
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Level-order (BFS) দিয়ে insert করো — Complete BT তৈরি হয়"""
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            queue.append(node.right)

    def inorder(self, node=None, first=True):
        """Left → Root → Right (Sorted order দেয় BST এর জন্য)"""
        if first:
            node = self.root
            print("Inorder: ", end="")
        if node:
            self.inorder(node.left, False)
            print(node.val, end=" ")
            self.inorder(node.right, False)
        if first:
            print()

    def preorder(self, node=None, first=True):
        """Root → Left → Right"""
        if first:
            node = self.root
            print("Preorder: ", end="")
        if node:
            print(node.val, end=" ")
            self.preorder(node.left, False)
            self.preorder(node.right, False)
        if first:
            print()

    def postorder(self, node=None, first=True):
        """Left → Right → Root"""
        if first:
            node = self.root
            print("Postorder: ", end="")
        if node:
            self.postorder(node.left, False)
            self.postorder(node.right, False)
            print(node.val, end=" ")
        if first:
            print()

    def height(self, node=None, first=True):
        """Tree এর height বের করো — O(n)"""
        if first:
            node = self.root
        if not node:
            return 0
        left_h = self.height(node.left, False)
        right_h = self.height(node.right, False)
        return 1 + max(left_h, right_h)

    def level_order(self):
        """BFS — Level by level print"""
        if not self.root:
            return
        queue = deque([self.root])
        level = 0
        while queue:
            level_size = len(queue)
            print(f"Level {level}:", end=" ")
            for _ in range(level_size):
                node = queue.popleft()
                print(node.val, end=" ")
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            print()
            level += 1


# ──── ব্যবহার ────
bt = BinaryTree()
for v in [1, 2, 3, 4, 5, 6, 7]:
    bt.insert(v)

#         1
#       /   \\
#      2     3
#    /  \\  /  \\
#   4    5 6    7

bt.inorder()       # Inorder:   4 2 5 1 6 3 7
bt.preorder()      # Preorder:  1 2 4 5 3 6 7
bt.postorder()     # Postorder: 4 5 2 6 7 3 1
bt.level_order()   # Level 0: 1, Level 1: 2 3, Level 2: 4 5 6 7
print("Height:", bt.height())   # Height: 3
'''

codes['tree_p1'] = '''
# Problem 1: Tree এর সব Node count করো
# Input Tree:     1
#               /   \\
#              2     3
#            /  \\
#           4    5
# Output: 5

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_nodes(root):
    """Recursive approach — O(n)"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaves(root):
    """Leaf nodes count করো (যার কোনো child নেই)"""
    if not root:
        return 0
    if not root.left and not root.right:
        return 1   # এটি leaf
    return count_leaves(root.left) + count_leaves(root.right)


# Tree তৈরি করো
root = TreeNode(1)
root.left = TreeNode(2);  root.right = TreeNode(3)
root.left.left = TreeNode(4); root.left.right = TreeNode(5)

print("Total Nodes:", count_nodes(root))   # 5
print("Leaf Nodes:", count_leaves(root))   # 3 (3, 4, 5)
'''

codes['tree_p2'] = '''
# Problem 2: Mirror Tree তৈরি করো (Tree Flip/Invert)
# Input:      1          Output:     1
#           /   \\                  /   \\
#          2     3                3     2
#        /  \\                        /  \\
#       4    5                       5    4

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror_tree(root):
    """প্রতিটি node এর left এবং right swap করো"""
    if not root:
        return None
    # Recursively mirror করো
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Test
root = TreeNode(1)
root.left = TreeNode(2);  root.right = TreeNode(3)
root.left.left = TreeNode(4); root.left.right = TreeNode(5)

print("Before mirror - Inorder: ", end="")
inorder(root)   # 4 2 5 1 3
print()

mirror_tree(root)
print("After mirror  - Inorder: ", end="")
inorder(root)   # 3 1 5 2 4
print()
'''

# ─── BST ───
codes['bst_impl'] = '''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree:
    - বাঁদিকের সব node < root
    - ডানদিকের সব node > root
    - Inorder traversal = Sorted order
    """
    def __init__(self):
        self.root = None

    def insert(self, val):
        """BST তে সঠিক জায়গায় insert করো — O(log n) avg"""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node   # duplicate ignore করি

    def search(self, val):
        """Value খুঁজো — O(log n) avg"""
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def delete(self, val):
        """Node মুছো — ৩ case আছে"""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Case 1: No child
            if not node.left and not node.right:
                return None
            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Case 3: Two children → inorder successor খুঁজো
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def inorder(self, node=None, first=True):
        """Sorted order এ print করো"""
        if first:
            node = self.root
            print("Sorted BST:", end=" ")
        if node:
            self.inorder(node.left, False)
            print(node.val, end=" ")
            self.inorder(node.right, False)
        if first:
            print()

    def min_val(self):
        node = self.root
        while node and node.left:
            node = node.left
        return node.val if node else None

    def max_val(self):
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else None


# ──── ব্যবহার ────
bst = BST()
for v in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(v)

#         5
#       /   \\
#      3     7
#    /  \\  /  \\
#   1    4 6    8

bst.inorder()                  # Sorted BST: 1 3 4 5 6 7 8
print(bst.search(4))           # True
print(bst.search(9))           # False
print("Min:", bst.min_val())   # Min: 1
print("Max:", bst.max_val())   # Max: 8
bst.delete(3)
bst.inorder()                  # Sorted BST: 1 4 5 6 7 8
'''

codes['bst_p1'] = '''
# Problem 1: BST এর K-তম সবচেয়ে ছোট element খুঁজো
# Input: BST = [5,3,7,1,4], k = 3
# Output: 4  (1,3,4,5,7 → 3rd smallest = 4)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kth_smallest(root, k):
    """
    Inorder traversal → sorted order।
    k-তম element মানে inorder এর k-তম।
    """
    count = [0]   # list হিসেবে নিলে nested function এ modify হয়
    result = [None]

    def inorder(node):
        if not node or result[0] is not None:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]


# BST তৈরি করো: 5,3,7,1,4
root = TreeNode(5)
root.left = TreeNode(3);    root.right = TreeNode(7)
root.left.left = TreeNode(1); root.left.right = TreeNode(4)

# Inorder: 1, 3, 4, 5, 7
print(f"1st smallest: {kth_smallest(root, 1)}")  # 1
print(f"2nd smallest: {kth_smallest(root, 2)}")  # 3
print(f"3rd smallest: {kth_smallest(root, 3)}")  # 4
print(f"5th smallest: {kth_smallest(root, 5)}")  # 7
'''

codes['bst_p2'] = '''
# Problem 2: BST তে দুটো Node এর Lowest Common Ancestor (LCA)
# Input: BST=[6,2,8,0,4,7,9], p=2, q=8 → LCA = 6
# Input: BST=[6,2,8,0,4,7,9], p=2, q=4 → LCA = 2

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca_bst(root, p, q):
    """
    BST property ব্যবহার করো:
    - p এবং q যদি root এর বাঁয়ে → বাঁয়ে যাও
    - p এবং q যদি root এর ডানে → ডানে যাও
    - একটা বাঁয়ে একটা ডানে → root-ই LCA
    """
    if not root:
        return None

    if p < root.val and q < root.val:
        return lca_bst(root.left, p, q)   # দুটোই বাঁয়ে
    if p > root.val and q > root.val:
        return lca_bst(root.right, p, q)  # দুটোই ডানে

    return root.val   # এখানেই split হচ্ছে → LCA


# BST তৈরি করো
root = TreeNode(6)
root.left = TreeNode(2);   root.right = TreeNode(8)
root.left.left = TreeNode(0); root.left.right = TreeNode(4)
root.right.left = TreeNode(7); root.right.right = TreeNode(9)

print(lca_bst(root, 2, 8))   # 6
print(lca_bst(root, 2, 4))   # 2
print(lca_bst(root, 7, 9))   # 8
print(lca_bst(root, 0, 9))   # 6
'''

# ─── SEARCHING ───
codes['search_impl'] = '''
# ════════════════════════════════════
# LINEAR SEARCH — O(n)
# ════════════════════════════════════
def linear_search(arr, target):
    """প্রতিটি element check করো — unsorted array তেও কাজ করে"""
    for i, val in enumerate(arr):
        if val == target:
            return i   # index return করো
    return -1   # পাওয়া গেলো না


# Test
arr = [64, 25, 12, 22, 11]
print("Linear Search:")
print(f"  22 খুঁজে পেলাম index: {linear_search(arr, 22)}")   # 3
print(f"  99 খুঁজে পেলাম index: {linear_search(arr, 99)}")   # -1


# ════════════════════════════════════
# BINARY SEARCH — O(log n)
# ════════════════════════════════════
def binary_search(arr, target):
    """
    SORTED array তে কাজ করে।
    প্রতিবার অর্ধেক বাদ দাও।
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # মাঝের index

        if arr[mid] == target:
            return mid            # পাওয়া গেছে!
        elif arr[mid] < target:
            low = mid + 1         # ডানদিকে খোঁজো
        else:
            high = mid - 1        # বাঁদিকে খোঁজো

    return -1   # পাওয়া যায়নি


# Test
sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\\nBinary Search (sorted array):")
print(f"  23 এর index: {binary_search(sorted_arr, 23)}")   # 5
print(f"  72 এর index: {binary_search(sorted_arr, 72)}")   # 8
print(f"  99 এর index: {binary_search(sorted_arr, 99)}")   # -1

# Recursive Binary Search
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

print(f"  Recursive — 56 এর index: {binary_search_recursive(sorted_arr, 56)}")  # 7
'''

codes['search_p1'] = '''
# Problem 1: Sorted Array তে First এবং Last Occurrence খুঁজো
# Input: arr = [1, 3, 5, 5, 5, 7, 9], target = 5
# Output: First = 2, Last = 4

def find_first(arr, target):
    """Binary Search: target পেলেও বাঁয়ে খুঁজতে থাকো"""
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid          # মনে রাখো
            high = mid - 1        # আরো বাঁয়ে খোঁজো
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def find_last(arr, target):
    """Binary Search: target পেলেও ডানে খুঁজতে থাকো"""
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid          # মনে রাখো
            low = mid + 1         # আরো ডানে খোঁজো
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0
    last = find_last(arr, target)
    return last - first + 1


# Test
arr = [1, 3, 5, 5, 5, 7, 9]
print(f"First 5: index {find_first(arr, 5)}")       # 2
print(f"Last  5: index {find_last(arr, 5)}")        # 4
print(f"Count of 5: {count_occurrences(arr, 5)}")   # 3
print(f"Count of 7: {count_occurrences(arr, 7)}")   # 1
print(f"Count of 4: {count_occurrences(arr, 4)}")   # 0
'''

codes['search_p2'] = '''
# Problem 2: Rotated Sorted Array তে Search করো
# Input: arr = [4,5,6,7,0,1,2], target = 0 → Output: 4
# Input: arr = [4,5,6,7,0,1,2], target = 3 → Output: -1

def search_rotated(arr, target):
    """
    যেকোনো অবস্থায় একটি অর্ধেক sorted থাকে।
    Sorted অর্ধে target আছে কিনা দেখো।
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # বাঁ অর্ধ sorted?
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1     # বাঁয়ে খোঁজো
            else:
                low = mid + 1      # ডানে খোঁজো
        # ডান অর্ধ sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1      # ডানে খোঁজো
            else:
                high = mid - 1     # বাঁয়ে খোঁজো

    return -1


# Test
arr = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(arr, 0))    # 4
print(search_rotated(arr, 6))    # 2
print(search_rotated(arr, 3))    # -1
print(search_rotated(arr, 4))    # 0 (first element)
'''

# ─── SORTING ───
codes['sort_impl'] = '''
import time

# ════════════════════════════════════
# 1. BUBBLE SORT — O(n²)
# ════════════════════════════════════
def bubble_sort(arr):
    """প্রতিবার বড় element কে বুদবুদের মতো ওপরে তোলো"""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # already sorted!
            break
    return arr


# ════════════════════════════════════
# 2. SELECTION SORT — O(n²)
# ════════════════════════════════════
def selection_sort(arr):
    """প্রতিবার সবচেয়ে ছোট element খুঁজে সামনে রাখো"""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ════════════════════════════════════
# 3. INSERTION SORT — O(n²)
# ════════════════════════════════════
def insertion_sort(arr):
    """তাস সাজানোর মতো — নতুন element সঠিক জায়গায় ঢোকাও"""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # একটা ডানে সরাও
            j -= 1
        arr[j + 1] = key
    return arr


# ════════════════════════════════════
# 4. MERGE SORT — O(n log n)
# ════════════════════════════════════
def merge_sort(arr):
    """Divide & Conquer: ভাগ করো, sort করো, merge করো"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ════════════════════════════════════
# 5. QUICK SORT — O(n log n) avg
# ════════════════════════════════════
def quick_sort(arr):
    """Pivot বেছে দুভাগ করো — in-place sort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ──── সব একসাথে Test ────
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:         ", arr)
print("Bubble Sort:      ", bubble_sort(arr))
print("Selection Sort:   ", selection_sort(arr))
print("Insertion Sort:   ", insertion_sort(arr))
print("Merge Sort:       ", merge_sort(arr))
print("Quick Sort:       ", quick_sort(arr))
'''

codes['sort_p1'] = '''
# Problem 1: Dutch National Flag — 0, 1, 2 Sort করো
# Input:  [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]
# Constraint: একবারেই করতে হবে — O(n), O(1) space

def dutch_flag(arr):
    """
    ৩টি pointer:
    - low:  0 এর জন্য
    - mid:  1 এর জন্য
    - high: 2 এর জন্য
    """
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1; mid += 1
        elif arr[mid] == 1:
            mid += 1          # 1 সঠিক জায়গায়
        else:                 # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1         # mid বাড়াই না! নতুন arr[mid] check দরকার

    return arr


# Test
print(dutch_flag([2, 0, 2, 1, 1, 0]))   # [0, 0, 1, 1, 2, 2]
print(dutch_flag([0, 1, 2, 0, 1, 2]))   # [0, 0, 1, 1, 2, 2]
print(dutch_flag([2, 2, 0, 0, 1, 1]))   # [0, 0, 1, 1, 2, 2]
print(dutch_flag([1, 0, 2]))            # [0, 1, 2]
'''

codes['sort_p2'] = '''
# Problem 2: Frequency অনুযায়ী Sort করো
# Input:  [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
# Output: [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]
# (বেশি আসা element আগে, same frequency হলে ছোট আগে)

from collections import Counter

def sort_by_frequency(arr):
    """
    Counter দিয়ে frequency গুনো,
    তারপর (-freq, value) দিয়ে sort করো।
    """
    freq = Counter(arr)
    # Key: frequency বেশি = আগে (-freq), same freq হলে ছোট আগে
    return sorted(arr, key=lambda x: (-freq[x], x))


# Test
arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
result = sort_by_frequency(arr)
print(result)  # [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]

arr2 = [4, 5, 6, 5, 4, 3]
print(sort_by_frequency(arr2))  # [4, 4, 5, 5, 3, 6]
'''

# ─── HASHING ───
codes['hash_impl'] = '''
# ════════════════════════════════════
# Python dict = Hash Map (Built-in)
# ════════════════════════════════════

# Basic Hash Map ব্যবহার
phone_book = {}

# Insert — O(1)
phone_book["রাকিব"] = "01712345678"
phone_book["সাকিব"] = "01898765432"
phone_book["তামিম"] = "01611223344"

# Search — O(1)
print(phone_book["রাকিব"])           # 01712345678
print("সাকিব" in phone_book)         # True
print(phone_book.get("নাইম", "নেই")) # নেই

# Delete — O(1)
del phone_book["তামিম"]
print(phone_book)


# ════════════════════════════════════
# Custom Hash Map (Chaining দিয়ে Collision handle)
# ════════════════════════════════════
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]   # প্রতিটি bucket একটি list

    def _hash(self, key):
        """Hash function: key → index"""
        return hash(key) % self.size

    def put(self, key, value):
        """Key-Value pair insert/update করো — O(1) avg"""
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # update
                return
        bucket.append((key, value))         # insert

    def get(self, key):
        """Key দিয়ে value খুঁজো — O(1) avg"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Key মুছো — O(1) avg"""
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  [{i}]: {bucket}")


# ──── ব্যবহার ────
hm = HashMap()
hm.put("name", "রাকিব")
hm.put("age", 22)
hm.put("city", "Jessore")
print("name:", hm.get("name"))   # রাকিব
print("age:", hm.get("age"))     # 22
hm.remove("city")
print("city:", hm.get("city"))   # None
hm.display()
'''

codes['hash_p1'] = '''
# Problem 1: Two Sum — দুটো number যোগ করলে target হয়?
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  (কারণ nums[0] + nums[1] = 2 + 7 = 9)

def two_sum(nums, target):
    """
    Hash Map দিয়ে O(n) এ solve করো।
    প্রতিটি number এর জন্য দেখো:
    complement = target - num আগে দেখা গেছে?
    """
    seen = {}   # {value: index}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]   # পাওয়া গেছে!
        seen[num] = i   # এখনো পাইনি, মনে রাখো

    return []   # কোনো pair নেই


# Test
print(two_sum([2, 7, 11, 15], 9))    # [0, 1]
print(two_sum([3, 2, 4], 6))         # [1, 2]
print(two_sum([3, 3], 6))            # [0, 1]
print(two_sum([1, 2, 3, 4, 5], 9))   # [3, 4]
print(two_sum([1, 2, 3], 10))        # []
'''

codes['hash_p2'] = '''
# Problem 2: Array তে Duplicate আছে কিনা বের করো
# সব duplicates এর list দাও

def has_duplicate(arr):
    """O(n) — Hash Set ব্যবহার করো"""
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

def find_all_duplicates(arr):
    """সব duplicate খুঁজে বের করো"""
    from collections import Counter
    freq = Counter(arr)
    return [num for num, count in freq.items() if count > 1]

def first_non_repeating(arr):
    """প্রথম non-repeating element খুঁজো"""
    from collections import Counter, OrderedDict
    # OrderedDict insertion order maintain করে
    freq = Counter(arr)
    for num in arr:
        if freq[num] == 1:
            return num
    return -1


# Test
arr = [1, 2, 3, 4, 2, 5, 6, 3, 7]
print(has_duplicate(arr))         # True
print(find_all_duplicates(arr))   # [2, 3]
print(first_non_repeating(arr))   # 1

arr2 = [1, 1, 2, 2, 3, 3]
print(first_non_repeating(arr2))  # -1 (সব duplicate)
'''

# ─── GRAPH ───
codes['graph_impl'] = '''
from collections import defaultdict, deque

class Graph:
    """Adjacency List দিয়ে Graph represent করো"""

    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        """Edge যোগ করো"""
        self.adj[u].append(v)
        if not self.directed:    # undirected হলে দুদিকেই
            self.adj[v].append(u)

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def display(self):
        print("Graph (Adjacency List):")
        for vertex in sorted(self.adj):
            neighbors = " → ".join(map(str, self.adj[vertex]))
            print(f"  {vertex}: [{neighbors}]")

    # ════════════════════════════════
    # BFS — Breadth First Search
    # Level by level explore করো
    # ════════════════════════════════
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # ════════════════════════════════
    # DFS — Depth First Search
    # যতদূর যাওয়া যায় যাও, তারপর ফিরে এসো
    # ════════════════════════════════
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]

        for neighbor in self.adj[start]:
            if neighbor not in visited:
                order.extend(self.dfs(neighbor, visited))

        return order

    def has_path(self, start, end):
        """BFS দিয়ে path আছে কিনা — O(V+E)"""
        visited = set([start])
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex == end:
                return True
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False


# ──── ব্যবহার ────
g = Graph()
edges = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7)]
for u, v in edges:
    g.add_edge(u, v)

g.display()
print("BFS from 1:", g.bfs(1))    # [1, 2, 3, 4, 5, 6, 7]
print("DFS from 1:", g.dfs(1))    # [1, 2, 4, 5, 3, 6, 7]
print("Path 1→7:", g.has_path(1, 7))  # True
print("Path 4→6:", g.has_path(4, 6))  # False (undirected, but 4 is isolated from 6)
'''

codes['graph_p1'] = '''
# Problem 1: BFS দিয়ে Shortest Path খুঁজো
# (Unweighted Graph এ)

from collections import deque, defaultdict

def shortest_path(graph, start, end):
    """
    BFS সবসময় shortest path দেয় unweighted graph এ।
    প্রতিটি node এর parent track করো, তারপর backtrack করো।
    """
    if start == end:
        return [start]

    visited = {start}
    queue = deque([[start]])   # path list নিয়ে চলো

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path           # পেয়ে গেলাম!
                visited.add(neighbor)
                queue.append(new_path)

    return []   # কোনো path নেই


# Graph তৈরি করো
graph = defaultdict(list)
edges = [("A","B"),("A","C"),("B","D"),("B","E"),
         ("C","F"),("E","F"),("D","G")]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Test
print(shortest_path(graph, "A", "G"))  # A → B → D → G
print(shortest_path(graph, "A", "F"))  # A → C → F
print(shortest_path(graph, "G", "F"))  # G → D → B → E → F (or shorter)
print(shortest_path(graph, "B", "C"))  # B → A → C
'''

codes['graph_p2'] = '''
# Problem 2: Undirected Graph এ Cycle আছে কিনা বের করো

from collections import defaultdict

def has_cycle(graph, num_vertices):
    """
    DFS দিয়ে cycle detect করো।
    যদি visited node কে আবার পাই (parent ছাড়া)
    তাহলে cycle আছে।
    """
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True   # cycle পাওয়া গেছে!
        return False

    # প্রতিটি component check করো (disconnected graph)
    for v in range(num_vertices):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False


# Test — Cycle আছে
g1 = defaultdict(list)
for u, v in [(0,1),(1,2),(2,3),(3,0)]:   # 0-1-2-3-0 cycle
    g1[u].append(v); g1[v].append(u)
print("Cycle আছে:", has_cycle(g1, 4))    # True

# Test — Cycle নেই (Tree)
g2 = defaultdict(list)
for u, v in [(0,1),(1,2),(2,3)]:         # simple path
    g2[u].append(v); g2[v].append(u)
print("Cycle আছে:", has_cycle(g2, 4))    # False
'''

# ─────────────────────────────────────────────
# HTML GENERATION
# ─────────────────────────────────────────────

def make_code_block(code_key, filename):
    code = codes[code_key].strip()
    # escape for HTML attribute (not needed since we use data- attr and JS)
    return f'''<div class="code-wrapper">
  <div class="code-label">📄 {filename}</div>
  <pre class="code-display language-python" data-code="{code_key}"></pre>
</div>'''

HTML = '''<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Data Structures — সম্পূর্ণ গাইড (Python)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&family=Hind+Siliguri:wght@300;400;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<style>
:root {
  --bg:        #060d1f;
  --bg2:       #080f24;
  --bg3:       #0c1530;
  --card:      #0a1428;
  --border:    #162540;
  --border2:   #1e3a5f;
  --cyan:      #00d4ff;
  --cyan2:     #00aacc;
  --orange:    #ff6b35;
  --green:     #00e676;
  --yellow:    #ffd740;
  --purple:    #b39ddb;
  --pink:      #f48fb1;
  --text:      #cce7ff;
  --text2:     #7ea8d0;
  --text3:     #3d6a90;
  --sidebar:   280px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{
  font-family:'Hind Siliguri',sans-serif;
  background:var(--bg);color:var(--text);
  display:flex;min-height:100vh;
  line-height:1.7;
}
/* ─── SIDEBAR ─── */
.sidebar{
  width:var(--sidebar);background:var(--bg2);
  border-right:1px solid var(--border);
  position:fixed;top:0;left:0;height:100vh;
  overflow-y:auto;z-index:100;
  display:flex;flex-direction:column;
}
.sb-logo{
  padding:22px 20px;border-bottom:1px solid var(--border);
  background:linear-gradient(135deg,#060d1f 0%,#0c1835 100%);
}
.sb-logo h1{
  font-family:'Syne',sans-serif;font-size:16px;
  color:var(--cyan);letter-spacing:2px;text-transform:uppercase;
}
.sb-logo p{font-size:11px;color:var(--text3);margin-top:4px;}
.sb-section{padding:8px 0;}
.sb-section-label{
  padding:10px 20px 6px;font-size:10px;
  color:var(--text3);letter-spacing:2px;text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;
}
.nav-item{
  display:flex;align-items:center;gap:10px;
  padding:10px 20px;cursor:pointer;transition:all .2s;
  border-left:3px solid transparent;text-decoration:none;
}
.nav-item:hover{background:rgba(0,212,255,.07);border-left-color:var(--cyan2);}
.nav-item.active{background:rgba(0,212,255,.12);border-left-color:var(--cyan);}
.nav-num{
  width:26px;height:26px;border-radius:6px;
  background:var(--bg3);border:1px solid var(--border);
  display:flex;align-items:center;justify-content:center;
  font-family:'JetBrains Mono',monospace;font-size:11px;
  color:var(--text3);flex-shrink:0;transition:.2s;
}
.nav-item.active .nav-num{color:var(--cyan);border-color:var(--cyan);}
.nav-text{font-size:13px;color:var(--text2);}
.nav-item.active .nav-text{color:var(--text);}
/* ─── MAIN ─── */
.main{
  margin-left:var(--sidebar);flex:1;
  padding:48px 52px;max-width:calc(100vw - var(--sidebar));
}
/* ─── CHAPTERS ─── */
.chapter{display:none;animation:fadeUp .35s ease;}
.chapter.active{display:block;}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.ch-badge{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(0,212,255,.08);border:1px solid rgba(0,212,255,.25);
  border-radius:20px;padding:5px 14px;
  font-size:11px;color:var(--cyan);
  font-family:'JetBrains Mono',monospace;letter-spacing:1px;
  margin-bottom:14px;
}
.ch-title{
  font-family:'Syne',sans-serif;font-size:44px;
  font-weight:800;color:#fff;margin-bottom:6px;
  letter-spacing:-1px;
}
.ch-sub{
  font-size:15px;color:var(--text2);margin-bottom:36px;
  padding-bottom:28px;border-bottom:1px solid var(--border);
}
/* ─── SECTIONS ─── */
.section{margin-bottom:44px;}
.sec-title{
  font-size:21px;font-weight:700;color:var(--cyan);
  margin-bottom:18px;display:flex;align-items:center;gap:10px;
}
.sec-title::before{
  content:'';display:block;width:4px;height:20px;
  background:var(--cyan);border-radius:2px;flex-shrink:0;
}
.card{
  background:var(--card);border:1px solid var(--border);
  border-radius:12px;padding:24px;margin-bottom:16px;
}
.card p{color:var(--text2);margin-bottom:10px;font-size:15px;}
.card p:last-child{margin-bottom:0;}
strong{color:var(--text);}
/* ─── VIZ BOX ─── */
.viz{
  background:#000c1a;border:1px solid var(--border);
  border-radius:8px;padding:18px 22px;
  font-family:'JetBrains Mono',monospace;font-size:13px;
  color:var(--green);overflow-x:auto;white-space:pre;
  line-height:1.7;margin-bottom:16px;
}
/* ─── CODE BLOCKS ─── */
.code-wrapper{margin-bottom:20px;}
.code-label{
  display:inline-block;background:var(--bg3);
  border:1px solid var(--border);border-bottom:none;
  border-radius:6px 6px 0 0;padding:5px 14px;
  font-size:11px;color:var(--text3);
  font-family:'JetBrains Mono',monospace;
}
.code-wrapper pre.code-display{
  border-radius:0 10px 10px 10px !important;
  margin:0 !important;font-size:13px !important;
  border:1px solid var(--border) !important;
}
/* ─── OPS GRID ─── */
.ops-grid{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));
  gap:12px;margin-bottom:20px;
}
.op-card{
  background:var(--bg3);border:1px solid var(--border);
  border-radius:10px;padding:16px;text-align:center;
}
.op-name{
  font-family:'JetBrains Mono',monospace;font-size:13px;
  color:var(--cyan);margin-bottom:6px;
}
.op-desc{font-size:12px;color:var(--text3);}
.op-c{
  font-family:'JetBrains Mono',monospace;font-size:11px;
  color:var(--green);margin-top:4px;font-weight:700;
}
.op-c.bad{color:var(--orange);}
.op-c.mid{color:var(--yellow);}
/* ─── COMPLEXITY TABLE ─── */
.cmp-table{width:100%;border-collapse:collapse;margin-bottom:20px;border-radius:10px;overflow:hidden;}
.cmp-table th{
  background:var(--bg3);padding:11px 16px;
  text-align:left;font-size:12px;color:var(--cyan);
  border-bottom:1px solid var(--border);letter-spacing:.5px;
}
.cmp-table td{
  padding:11px 16px;font-size:13px;color:var(--text2);
  border-bottom:1px solid var(--border);
}
.cmp-table tr:last-child td{border-bottom:none;}
.cmp-table tr:hover td{background:rgba(255,255,255,.02);}
.g{color:var(--green);font-family:monospace;font-weight:700;}
.y{color:var(--yellow);font-family:monospace;}
.r{color:var(--orange);font-family:monospace;}
/* ─── PROBLEM CARDS ─── */
.prob-card{
  background:var(--card);border:1px solid var(--border2);
  border-top:3px solid var(--orange);
  border-radius:12px;padding:24px;margin-bottom:18px;
}
.prob-tag{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,107,53,.12);color:var(--orange);
  padding:4px 12px;border-radius:20px;
  font-size:11px;font-weight:700;margin-bottom:12px;
  letter-spacing:.5px;
}
.prob-title{
  font-size:18px;font-weight:700;color:#fff;margin-bottom:10px;
}
.prob-desc{color:var(--text2);font-size:14px;margin-bottom:16px;line-height:1.7;}
.io-box{
  background:#000c1a;border:1px solid var(--border);
  border-radius:8px;padding:14px 18px;
  font-family:'JetBrains Mono',monospace;font-size:12px;
  color:var(--purple);margin-bottom:14px;line-height:1.8;
}
/* ─── TASKS ─── */
.tasks-card{
  background:var(--card);border:1px solid var(--border);
  border-top:3px solid var(--yellow);
  border-radius:12px;padding:24px;
}
.tasks-hdr{
  font-size:17px;font-weight:700;color:var(--yellow);
  margin-bottom:18px;display:flex;align-items:center;gap:8px;
}
.task-list{list-style:none;}
.task-item{
  display:flex;align-items:flex-start;gap:12px;
  padding:12px 0;border-bottom:1px solid var(--border);
  font-size:14px;color:var(--text2);
}
.task-item:last-child{border-bottom:none;padding-bottom:0;}
.task-n{
  min-width:28px;height:28px;
  background:rgba(255,215,64,.08);
  border:1px solid rgba(255,215,64,.3);
  border-radius:6px;display:flex;align-items:center;
  justify-content:center;font-size:12px;color:var(--yellow);
  font-family:'JetBrains Mono',monospace;font-weight:700;
}
.diff{
  font-size:11px;padding:2px 8px;border-radius:10px;
  font-weight:700;margin-left:auto;flex-shrink:0;
}
.easy{background:rgba(0,230,118,.1);color:var(--green);}
.med {background:rgba(255,215,64,.1);color:var(--yellow);}
.hard{background:rgba(255,107,53,.1);color:var(--orange);}
/* ─── DIVIDER ─── */
.divider{border:none;border-top:1px solid var(--border);margin:36px 0;}
/* ─── SCROLLBAR ─── */
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:var(--bg2);}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px;}
::-webkit-scrollbar-thumb:hover{background:var(--cyan);}
/* ─── RESPONSIVE ─── */
@media(max-width:900px){
  .sidebar{width:220px;--sidebar:220px;}
  .main{padding:28px 24px;}
  .ch-title{font-size:32px;}
}
</style>
</head>
<body>

<!-- ═══════════════ SIDEBAR ═══════════════ -->
<nav class="sidebar">
  <div class="sb-logo">
    <h1>⚡ DS Guide</h1>
    <p>Python দিয়ে Data Structures</p>
  </div>
  <div class="sb-section">
    <div class="sb-section-label">Chapters</div>
    <a class="nav-item active" onclick="showChapter(1)">
      <div class="nav-num">01</div><div class="nav-text">Stack</div>
    </a>
    <a class="nav-item" onclick="showChapter(2)">
      <div class="nav-num">02</div><div class="nav-text">Queue</div>
    </a>
    <a class="nav-item" onclick="showChapter(3)">
      <div class="nav-num">03</div><div class="nav-text">Heap</div>
    </a>
    <a class="nav-item" onclick="showChapter(4)">
      <div class="nav-num">04</div><div class="nav-text">Linked List</div>
    </a>
    <a class="nav-item" onclick="showChapter(5)">
      <div class="nav-num">05</div><div class="nav-text">Tree</div>
    </a>
    <a class="nav-item" onclick="showChapter(6)">
      <div class="nav-num">06</div><div class="nav-text">Binary Search Tree</div>
    </a>
    <a class="nav-item" onclick="showChapter(7)">
      <div class="nav-num">07</div><div class="nav-text">Searching</div>
    </a>
    <a class="nav-item" onclick="showChapter(8)">
      <div class="nav-num">08</div><div class="nav-text">Sorting</div>
    </a>
    <a class="nav-item" onclick="showChapter(9)">
      <div class="nav-num">09</div><div class="nav-text">Hashing</div>
    </a>
    <a class="nav-item" onclick="showChapter(10)">
      <div class="nav-num">10</div><div class="nav-text">Graph</div>
    </a>
  </div>
</nav>

<!-- ═══════════════ MAIN ═══════════════ -->
<main class="main">

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 1: STACK                  -->
<!-- ══════════════════════════════════ -->
<section class="chapter active" id="ch-1">
  <div class="ch-badge">Chapter 01</div>
  <h2 class="ch-title">Stack</h2>
  <p class="ch-sub">LIFO (Last In First Out) — শেষে যা ঢুকবে সে আগে বের হবে। থালা-বাসনের স্তূপের মতো।</p>

  <div class="section">
    <h3 class="sec-title">Stack কী?</h3>
    <div class="card">
      <p><strong>Stack</strong> হলো একটি Linear Data Structure যেখানে element insert এবং delete সবসময় একটি নির্দিষ্ট প্রান্ত থেকে হয় — যাকে বলা হয় <strong>Top</strong>।</p>
      <p>বাস্তব জীবনে উদাহরণ: থালা-বাসনের স্তূপ (নতুন থালা উপরে রাখা হয়, উপর থেকেই নেওয়া হয়), Browser এর Back button, Ctrl+Z (Undo)।</p>
      <p>Stack LIFO নীতি মেনে চলে: <strong>L</strong>ast <strong>I</strong>n <strong>F</strong>irst <strong>O</strong>ut।</p>
    </div>
    <div class="viz">  Stack visualization:

  push(10) → push(20) → push(30)

  ┌──────┐  ← TOP
  │  30  │  ← সবার শেষে ঢুকেছে
  ├──────┤
  │  20  │
  ├──────┤
  │  10  │  ← সবার আগে ঢুকেছে
  └──────┘

  pop() → 30 বের হবে (TOP থেকে)
  pop() → 20 বের হবে
  pop() → 10 বের হবে</div>
  </div>

  <div class="section">
    <h3 class="sec-title">কীভাবে কাজ করে?</h3>
    <div class="ops-grid">
      <div class="op-card"><div class="op-name">push(item)</div><div class="op-desc">Top এ element যোগ করো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">pop()</div><div class="op-desc">Top থেকে element বের করো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">peek()</div><div class="op-desc">Top element দেখো (না সরিয়ে)</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">is_empty()</div><div class="op-desc">Stack খালি কিনা</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">size()</div><div class="op-desc">কতটি element আছে</div><div class="op-c">O(1)</div></div>
    </div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 stack.py</div>
      <pre class="code-display language-python" data-code="stack_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>

    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">Balanced Parentheses Checker</div>
      <div class="prob-desc">একটি string এ ব্র্যাকেট balanced কিনা বের করো। Opening bracket stack এ রাখো, closing আসলে match করো।</div>
      <div class="io-box">Input:  "((){}[])"  →  Output: True
Input:  "({[})"    →  Output: False
Input:  "{[()]}"   →  Output: True</div>
      <div class="code-wrapper">
        <div class="code-label">📄 balanced_parens.py</div>
        <pre class="code-display language-python" data-code="stack_p1"></pre>
      </div>
    </div>

    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Stack দিয়ে String Reverse করো</div>
      <div class="prob-desc">Stack এর LIFO property ব্যবহার করে string reverse করো। প্রথমে সব push করো, তারপর pop করলেই reversed পাবে।</div>
      <div class="io-box">Input:  "Rakib"   →  Output: "bikaR"
Input:  "Python"  →  Output: "nohtyP"</div>
      <div class="code-wrapper">
        <div class="code-label">📄 reverse_string.py</div>
        <pre class="code-display language-python" data-code="stack_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks (৫টি সমস্যা সমাধান করো)</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Stack ব্যবহার করে Decimal সংখ্যাকে Binary তে convert করো। (যেমন: 10 → 1010)</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Next Greater Element: প্রতিটি element এর জন্য right দিকে তার চেয়ে বড় প্রথম element খুঁজো। Monotonic Stack ব্যবহার করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Infix Expression কে Postfix এ convert করো। (যেমন: A+B*C → ABC*+)</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Min Stack তৈরি করো যেখানে push(), pop(), top() এবং getMin() সব O(1) তে কাজ করবে।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Largest Rectangle in Histogram: N টি bar এর মধ্যে সবচেয়ে বড় rectangle এর area বের করো। Stack ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 2: QUEUE                  -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-2">
  <div class="ch-badge">Chapter 02</div>
  <h2 class="ch-title">Queue</h2>
  <p class="ch-sub">FIFO (First In First Out) — যে আগে ঢুকবে সে আগে বের হবে। টিকেট কাউন্টারের লাইনের মতো।</p>

  <div class="section">
    <h3 class="sec-title">Queue কী?</h3>
    <div class="card">
      <p><strong>Queue</strong> হলো একটি Linear Data Structure যেখানে element একদিক (Rear/পেছন) থেকে insert হয় এবং অন্যদিক (Front/সামনে) থেকে delete হয়।</p>
      <p>বাস্তব জীবনে উদাহরণ: ব্যাংকের সিরিয়াল লাইন, Printer queue, CPU scheduling, BFS algorithm।</p>
      <p>Queue FIFO নীতি মেনে চলে: <strong>F</strong>irst <strong>I</strong>n <strong>F</strong>irst <strong>O</strong>ut।</p>
    </div>
    <div class="viz">  Queue visualization:

  enqueue(A) → enqueue(B) → enqueue(C)

  FRONT                          REAR
    ↓                              ↓
  ┌──────┬──────┬──────┐
  │  A   │  B   │  C   │
  └──────┴──────┴──────┘
    ↑
  dequeue() → A বের হবে (FRONT থেকে)

  FRONT         REAR
    ↓              ↓
  ┌──────┬──────┐
  │  B   │  C   │
  └──────┴──────┘</div>
  </div>

  <div class="section">
    <h3 class="sec-title">কীভাবে কাজ করে?</h3>
    <div class="ops-grid">
      <div class="op-card"><div class="op-name">enqueue(item)</div><div class="op-desc">Rear এ element যোগ করো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">dequeue()</div><div class="op-desc">Front থেকে element বের করো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">front()</div><div class="op-desc">Front element দেখো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">rear()</div><div class="op-desc">Rear element দেখো</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">is_empty()</div><div class="op-desc">Queue খালি কিনা</div><div class="op-c">O(1)</div></div>
    </div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 queue.py</div>
      <pre class="code-display language-python" data-code="queue_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>

    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">১ থেকে N পর্যন্ত Binary Numbers Generate করো</div>
      <div class="prob-desc">Queue তে "1" দিয়ে শুরু করো। সামনেরটা বের করে "0" এবং "1" জুড়ে আবার দাও। এভাবে BFS pattern এ binary পাওয়া যায়।</div>
      <div class="io-box">Input:  N = 5
Output: ["1", "10", "11", "100", "101"]
        (1,   2,    3,    4,     5)</div>
      <div class="code-wrapper">
        <div class="code-label">📄 binary_numbers.py</div>
        <pre class="code-display language-python" data-code="queue_p1"></pre>
      </div>
    </div>

    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">দুটো Queue দিয়ে Stack তৈরি করো</div>
      <div class="prob-desc">Queue (FIFO) দিয়ে Stack (LIFO) এর behavior implement করো। Push করার সময় q1 এর সব element q2 তে নিয়ে যাও।</div>
      <div class="io-box">push(1), push(2), push(3)
top()  → 3  (Stack: LIFO)
pop()  → 3
pop()  → 2</div>
      <div class="code-wrapper">
        <div class="code-label">📄 stack_using_queue.py</div>
        <pre class="code-display language-python" data-code="queue_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Circular Queue implement করো — fixed size এর array ব্যবহার করে। enqueue, dequeue সব O(1) হতে হবে।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Queue দিয়ে Tree এর Level Order Traversal করো। প্রতিটি level আলাদা list এ রাখো।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Sliding Window Maximum: N size এর array এবং K size এর window। প্রতিটি window এর max বের করো। Deque ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Queue তে সংখ্যা reverse করো। অর্থাৎ Queue এর element গুলোর order উল্টো করো। (শুধু Stack বা Queue use করতে পারবে।)</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Priority Queue implement করো — যে element এর priority বেশি সে আগে বের হবে। heapq ব্যবহার করো।</div><span class="diff med">Medium</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 3: HEAP                   -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-3">
  <div class="ch-badge">Chapter 03</div>
  <h2 class="ch-title">Heap</h2>
  <p class="ch-sub">Complete Binary Tree যেখানে parent সবসময় child থেকে ছোট (Min Heap) বা বড় (Max Heap)।</p>

  <div class="section">
    <h3 class="sec-title">Heap কী?</h3>
    <div class="card">
      <p><strong>Heap</strong> হলো একটি Complete Binary Tree যা heap property মেনে চলে।</p>
      <p><strong>Min Heap:</strong> প্রতিটি parent node তার children থেকে ছোট বা সমান। Root সবচেয়ে ছোট।</p>
      <p><strong>Max Heap:</strong> প্রতিটি parent node তার children থেকে বড় বা সমান। Root সবচেয়ে বড়।</p>
      <p>ব্যবহার: Priority Queue, Heap Sort, Dijkstra's Algorithm, K largest/smallest elements।</p>
    </div>
    <div class="viz">  Min Heap:                    Max Heap:
         1                              9
       /   \\                          /   \\
      3     2                         7     8
    /  \\  /  \\                      /  \\  /  \\
   5    4 8    6                    4    6 2    1

  Array: [1, 3, 2, 5, 4, 8, 6]    Array: [9, 7, 8, 4, 6, 2, 1]
  Index:  0  1  2  3  4  5  6

  Parent of index i → (i-1) // 2
  Left child of i  → 2*i + 1
  Right child of i → 2*i + 2</div>
  </div>

  <div class="section">
    <h3 class="sec-title">কীভাবে কাজ করে?</h3>
    <div class="ops-grid">
      <div class="op-card"><div class="op-name">insert(val)</div><div class="op-desc">Heap এ element যোগ করো</div><div class="op-c">O(log n)</div></div>
      <div class="op-card"><div class="op-name">extract_min()</div><div class="op-desc">সবচেয়ে ছোট বের করো</div><div class="op-c">O(log n)</div></div>
      <div class="op-card"><div class="op-name">get_min()</div><div class="op-desc">Root দেখো (ছোট)</div><div class="op-c">O(1)</div></div>
      <div class="op-card"><div class="op-name">heapify(arr)</div><div class="op-desc">Array কে heap বানাও</div><div class="op-c">O(n)</div></div>
      <div class="op-card"><div class="op-name">size()</div><div class="op-desc">Element সংখ্যা</div><div class="op-c">O(1)</div></div>
    </div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 heap.py</div>
      <pre class="code-display language-python" data-code="heap_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">K-টি সবচেয়ে বড় Element খুঁজো</div>
      <div class="prob-desc">K size এর Min Heap রাখো। যখন heap full, ছোটটা বের করো। শেষে heap এই K-টি সবচেয়ে বড় element থাকবে।</div>
      <div class="io-box">Input: arr=[3,2,1,5,6,4], k=3
Output: [6, 5, 4]</div>
      <div class="code-wrapper">
        <div class="code-label">📄 k_largest.py</div>
        <pre class="code-display language-python" data-code="heap_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">K টি Sorted Array Merge করো</div>
      <div class="prob-desc">প্রতিটি array এর smallest element heap এ রাখো। Extract করো এবং সেই array এর next element দাও।</div>
      <div class="io-box">Input: [[1,4,7], [2,5,8], [3,6,9]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]</div>
      <div class="code-wrapper">
        <div class="code-label">📄 merge_k_sorted.py</div>
        <pre class="code-display language-python" data-code="heap_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Heap Sort implement করো। Array কে Max Heap বানাও, তারপর sort করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Running Median: প্রতিবার নতুন number আসলে এখন পর্যন্ত সব number এর median বের করো। Max Heap + Min Heap ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Task Scheduler: CPU tasks schedule করো যেন সবচেয়ে বেশি remaining task সবার আগে execute হয়।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>K-th Largest Element in a Stream: Stream থেকে data আসছে। প্রতিটি insert এ K-th largest দাও।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Minimum Cost to Connect Ropes: N টি rope আছে। প্রতিবার দুটো connect করলে cost = তাদের length এর sum। সবচেয়ে কম cost এ সব connect করো।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 4: LINKED LIST            -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-4">
  <div class="ch-badge">Chapter 04</div>
  <h2 class="ch-title">Linked List</h2>
  <p class="ch-sub">Node এর chain — প্রতিটি Node এ data এবং পরের node এর address থাকে। Dynamic size।</p>

  <div class="section">
    <h3 class="sec-title">Linked List কী?</h3>
    <div class="card">
      <p><strong>Linked List</strong> হলো এমন একটি Data Structure যেখানে elements (nodes) একে অপরের সাথে pointer দিয়ে সংযুক্ত থাকে।</p>
      <p>Array এর মতো contiguous memory লাগে না। প্রতিটি <strong>Node</strong> এ থাকে: (১) Data এবং (২) Next node এর pointer।</p>
      <p>ধরন: Singly Linked List, Doubly Linked List, Circular Linked List।</p>
    </div>
    <div class="viz">  Singly Linked List:

  head
   ↓
  ┌────┬──┐    ┌────┬──┐    ┌────┬──┐    ┌────┬────┐
  │ 10 │ •──→ │ 20 │ •──→ │ 30 │ •──→ │ 40 │NULL│
  └────┴──┘    └────┴──┘    └────┴──┘    └────┴────┘
   Node 1       Node 2       Node 3       Node 4

  Array vs Linked List:
  ┌─────────────┬─────────────────┬──────────────────┐
  │ Operation   │ Array           │ Linked List      │
  ├─────────────┼─────────────────┼──────────────────┤
  │ Access      │ O(1) ✓          │ O(n)             │
  │ Insert Head │ O(n)            │ O(1) ✓           │
  │ Insert Tail │ O(1)            │ O(n)             │
  │ Delete      │ O(n)            │ O(n)             │
  │ Memory      │ Fixed (static)  │ Dynamic ✓        │
  └─────────────┴─────────────────┴──────────────────┘</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 linked_list.py</div>
      <pre class="code-display language-python" data-code="ll_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">Linked List Reverse করো</div>
      <div class="prob-desc">তিনটি pointer (prev, current, next) ব্যবহার করে প্রতিটি arrow উল্টো করো। O(n) time, O(1) space।</div>
      <div class="io-box">Input:  1 → 2 → 3 → 4 → 5 → NULL
Output: 5 → 4 → 3 → 2 → 1 → NULL</div>
      <div class="code-wrapper">
        <div class="code-label">📄 reverse_ll.py</div>
        <pre class="code-display language-python" data-code="ll_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Cycle Detection — Floyd's Algorithm</div>
      <div class="prob-desc">Slow pointer ১ step, fast pointer ২ step এগোয়। Cycle থাকলে তারা একসময় meet করবেই। O(n) time, O(1) space।</div>
      <div class="io-box">1 → 2 → 3 → 4 → 5 → 3 (cycle)  →  True
1 → 2 → 3 → 4 → 5 → NULL        →  False</div>
      <div class="code-wrapper">
        <div class="code-label">📄 cycle_detection.py</div>
        <pre class="code-display language-python" data-code="ll_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Linked List এর মাঝের element খুঁজো। Two pointer (slow/fast) ব্যবহার করো। O(n) time, O(1) space।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Sorted Linked List merge করো। দুটো sorted linked list কে একটি sorted linked list এ merge করো।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Doubly Linked List implement করো — প্রতিটি node এ prev এবং next pointer থাকবে।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Linked List এ Palindrome কিনা check করো। List কে reverse করে compare করো। O(n) time।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>দুটো Linked List এর Intersection Point খুঁজো। যেখানে দুটো list একই node share করে।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 5: TREE                   -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-5">
  <div class="ch-badge">Chapter 05</div>
  <h2 class="ch-title">Tree</h2>
  <p class="ch-sub">Hierarchical Data Structure — Root থেকে শুরু হয়ে Branch ও Leaf পর্যন্ত যায়। File system, DOM tree এর মতো।</p>

  <div class="section">
    <h3 class="sec-title">Tree কী?</h3>
    <div class="card">
      <p><strong>Tree</strong> হলো একটি Hierarchical (স্তরক্রমিক) Non-linear Data Structure। এতে এক বা একাধিক Node থাকে যারা parent-child সম্পর্কে সংযুক্ত।</p>
      <p>গুরুত্বপূর্ণ Terms: <strong>Root</strong> (শীর্ষ node), <strong>Parent</strong> (উপরের node), <strong>Child</strong> (নিচের node), <strong>Leaf</strong> (কোনো child নেই), <strong>Height</strong> (root থেকে leaf পর্যন্ত দূরত্ব)।</p>
      <p>ব্যবহার: File system, HTML DOM, Database indexing, Expression trees।</p>
    </div>
    <div class="viz">  Binary Tree (প্রতিটি node এ সর্বোচ্চ ২টি child):

              1          ← Root (Level 0)
            /   \\
           2     3       ← Level 1
         /  \\  /  \\
        4    5 6    7    ← Level 2 (Leaf nodes)

  Traversal Orders:
  ┌─────────────┬────────────────────────┬────────────────┐
  │ Traversal   │ Order                  │ Result         │
  ├─────────────┼────────────────────────┼────────────────┤
  │ Inorder     │ Left → Root → Right    │ 4 2 5 1 6 3 7  │
  │ Preorder    │ Root → Left → Right    │ 1 2 4 5 3 6 7  │
  │ Postorder   │ Left → Right → Root    │ 4 5 2 6 7 3 1  │
  │ Level Order │ Level by Level (BFS)   │ 1 2 3 4 5 6 7  │
  └─────────────┴────────────────────────┴────────────────┘</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 binary_tree.py</div>
      <pre class="code-display language-python" data-code="tree_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">Tree এর Node Count করো</div>
      <div class="prob-desc">Recursively প্রতিটি node count করো: total = 1 + count(left) + count(right)। Leaf node count আলাদাভাবে।</div>
      <div class="io-box">Tree: 1→(2,3)→(4,5)  (5 nodes, 3 leaves)
Total Nodes: 5,  Leaf Nodes: 3</div>
      <div class="code-wrapper">
        <div class="code-label">📄 count_nodes.py</div>
        <pre class="code-display language-python" data-code="tree_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Mirror Tree (Tree Invert)</div>
      <div class="prob-desc">প্রতিটি node এর left এবং right child swap করো। Recursively পুরো tree mirror হয়ে যাবে।</div>
      <div class="io-box">Original:  4 2 5 1 3  (inorder)
Mirrored:  3 1 5 2 4  (inorder)</div>
      <div class="code-wrapper">
        <div class="code-label">📄 mirror_tree.py</div>
        <pre class="code-display language-python" data-code="tree_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Tree এর Height (Depth) বের করো। height = 1 + max(height(left), height(right))।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>দুটো Binary Tree identical কিনা check করো। Structure এবং values দুটোই same হতে হবে।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Tree এর সব Leaf Node এর sum বের করো। Recursion ব্যবহার করো।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Root থেকে Leaf পর্যন্ত সব Paths print করো। DFS ব্যবহার করে path track করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Diameter of Binary Tree: সবচেয়ে লম্বা path বের করো (যেকোনো দুটো node এর মধ্যে)।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 6: BST                    -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-6">
  <div class="ch-badge">Chapter 06</div>
  <h2 class="ch-title">Binary Search Tree</h2>
  <p class="ch-sub">BST — বাঁয়ে ছোট, ডানে বড়। Inorder traversal সবসময় sorted order দেয়। O(log n) search।</p>

  <div class="section">
    <h3 class="sec-title">BST কী?</h3>
    <div class="card">
      <p><strong>Binary Search Tree (BST)</strong> হলো একটি Binary Tree যেখানে প্রতিটি node এর জন্য:</p>
      <p>✦ বাঁ subtree এর সব values &lt; node.value</p>
      <p>✦ ডান subtree এর সব values &gt; node.value</p>
      <p>এই property এর কারণে Searching, Insertion, Deletion সব O(log n) তে করা যায় (balanced হলে)।</p>
    </div>
    <div class="viz">  BST তৈরি: insert(5,3,7,1,4,6,8)

          5
        /   \\
       3     7        Inorder: 1,3,4,5,6,7,8 ← Sorted!
     /  \\  /  \\
    1    4 6    8

  Search 4:  5→3→4  ✓ (৩ comparisons)
  Search 9:  5→7→8→NULL ✗

  BST vs Sorted Array:
  ┌──────────────┬──────────┬──────────────┐
  │ Operation    │ BST      │ Sorted Array │
  ├──────────────┼──────────┼──────────────┤
  │ Search       │ O(log n) │ O(log n)     │
  │ Insert       │ O(log n) │ O(n)         │
  │ Delete       │ O(log n) │ O(n)         │
  │ Min/Max      │ O(log n) │ O(1)         │
  └──────────────┴──────────┴──────────────┘</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 bst.py</div>
      <pre class="code-display language-python" data-code="bst_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">K-তম সবচেয়ে ছোট Element</div>
      <div class="prob-desc">BST এর Inorder traversal sorted order দেয়। K-তম inorder element = K-th smallest। Counter track করো।</div>
      <div class="io-box">BST: [5,3,7,1,4]  →  Inorder: 1,3,4,5,7
kth_smallest(k=3)  →  4</div>
      <div class="code-wrapper">
        <div class="code-label">📄 kth_smallest.py</div>
        <pre class="code-display language-python" data-code="bst_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Lowest Common Ancestor (LCA)</div>
      <div class="prob-desc">BST property ব্যবহার করো: দুটো value যেখানে split হয়, সেটাই LCA। O(log n) সময়।</div>
      <div class="io-box">BST: [6,2,8,0,4,7,9]
LCA(2, 8) = 6
LCA(2, 4) = 2</div>
      <div class="code-wrapper">
        <div class="code-label">📄 lca_bst.py</div>
        <pre class="code-display language-python" data-code="bst_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>BST Valid কিনা check করো। প্রতিটি node BST property মানছে কিনা verify করো (range check করো)।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Sorted Array থেকে Balanced BST তৈরি করো। Middle element কে root করো (recursively)।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">3</div><div>BST কে Sorted Doubly Linked List এ convert করো। Inorder traversal ব্যবহার করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>BST তে দুটো Swapped Node খুঁজো এবং fix করো (Morris Traversal বা Inorder)।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">5</div><div>BST Iterator implement করো — next() এবং hasNext() method দিয়ে sorted order এ iterate করো।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 7: SEARCHING              -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-7">
  <div class="ch-badge">Chapter 07</div>
  <h2 class="ch-title">Searching</h2>
  <p class="ch-sub">Linear Search O(n) বনাম Binary Search O(log n) — কোনটা কখন ব্যবহার করবে এবং কীভাবে কাজ করে।</p>

  <div class="section">
    <h3 class="sec-title">Searching কী?</h3>
    <div class="card">
      <p><strong>Searching</strong> হলো একটি collection থেকে নির্দিষ্ট element খুঁজে বের করার প্রক্রিয়া।</p>
      <p><strong>Linear Search:</strong> শুরু থেকে শেষ পর্যন্ত প্রতিটি element check করো। Unsorted data তেও কাজ করে।</p>
      <p><strong>Binary Search:</strong> Sorted array তে মাঝ থেকে শুরু করো, প্রতিবার অর্ধেক বাদ দাও। অনেক দ্রুত।</p>
    </div>
    <div class="viz">  Linear Search (arr=[5,2,8,1,9], target=8):
  5 → 2 → 8 ✓  (3 comparisons)

  Binary Search (arr=[1,2,5,8,9], target=8):
  Step 1: mid=5, 8>5  → right half
  Step 2: mid=8 ✓      (2 comparisons!)

  Comparison:
  ┌────────────────┬──────────┬──────────────┐
  │ Algorithm      │ Time     │ Requires     │
  ├────────────────┼──────────┼──────────────┤
  │ Linear Search  │ O(n)     │ Nothing      │
  │ Binary Search  │ O(log n) │ Sorted Array │
  └────────────────┴──────────┴──────────────┘

  Binary Search — 1 million elements:
  Linear: 1,000,000 comparisons
  Binary: log₂(1,000,000) ≈ 20 comparisons ⚡</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 searching.py</div>
      <pre class="code-display language-python" data-code="search_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">First এবং Last Occurrence খুঁজো</div>
      <div class="prob-desc">Sorted array তে একটি element কতবার আছে এবং কোথায় শুরু/শেষ হয় খুঁজো। Binary Search modify করো।</div>
      <div class="io-box">arr=[1,3,5,5,5,7,9], target=5
First: index 2,  Last: index 4,  Count: 3</div>
      <div class="code-wrapper">
        <div class="code-label">📄 first_last.py</div>
        <pre class="code-display language-python" data-code="search_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Rotated Sorted Array তে Search</div>
      <div class="prob-desc">Sorted array যদি rotate হয়ে যায়, তবুও Binary Search এ কাজ করে। একটি half সবসময় sorted — সেটা দিয়ে সিদ্ধান্ত নাও।</div>
      <div class="io-box">arr=[4,5,6,7,0,1,2], target=0  →  index 4
arr=[4,5,6,7,0,1,2], target=3  →  -1</div>
      <div class="code-wrapper">
        <div class="code-label">📄 search_rotated.py</div>
        <pre class="code-display language-python" data-code="search_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Square Root বের করো (integer part)। Binary Search ব্যবহার করো। যেমন: sqrt(10) = 3।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Book Allocation Problem: N টি book এবং M জন student। সর্বোচ্চ pages minimize করো। Binary Search on Answer।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Peak Element খুঁজো: arr[i] > arr[i-1] এবং arr[i] > arr[i+1] এমন যেকোনো একটি index দাও। O(log n)।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>2D Matrix তে Binary Search করো। Matrix sorted (প্রতিটি row এবং column sorted)।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Minimum in Rotated Sorted Array: Rotation এর pivot খুঁজো। O(log n) সময়ে।</div><span class="diff med">Medium</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 8: SORTING                -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-8">
  <div class="ch-badge">Chapter 08</div>
  <h2 class="ch-title">Sorting</h2>
  <p class="ch-sub">Bubble, Selection, Insertion, Merge, Quick Sort — সব algorithm, সব complexity, এক জায়গায়।</p>

  <div class="section">
    <h3 class="sec-title">Sorting কী?</h3>
    <div class="card">
      <p><strong>Sorting</strong> হলো একটি collection কে নির্দিষ্ট order এ (ascending বা descending) সাজানোর প্রক্রিয়া।</p>
      <p>Sorting algorithms এর দুটো বড় category: <strong>Comparison-based</strong> (Bubble, Merge, Quick) এবং <strong>Non-comparison-based</strong> (Counting, Radix)।</p>
    </div>
    <table class="cmp-table">
      <tr><th>Algorithm</th><th>Best Case</th><th>Average Case</th><th>Worst Case</th><th>Space</th><th>Stable</th></tr>
      <tr><td>Bubble Sort</td><td class="g">O(n)</td><td class="r">O(n²)</td><td class="r">O(n²)</td><td class="g">O(1)</td><td>হ্যাঁ</td></tr>
      <tr><td>Selection Sort</td><td class="r">O(n²)</td><td class="r">O(n²)</td><td class="r">O(n²)</td><td class="g">O(1)</td><td>না</td></tr>
      <tr><td>Insertion Sort</td><td class="g">O(n)</td><td class="r">O(n²)</td><td class="r">O(n²)</td><td class="g">O(1)</td><td>হ্যাঁ</td></tr>
      <tr><td>Merge Sort</td><td class="y">O(n log n)</td><td class="y">O(n log n)</td><td class="y">O(n log n)</td><td class="r">O(n)</td><td>হ্যাঁ</td></tr>
      <tr><td>Quick Sort</td><td class="y">O(n log n)</td><td class="y">O(n log n)</td><td class="r">O(n²)</td><td class="g">O(log n)</td><td>না</td></tr>
    </table>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python (সব algorithm)</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 sorting.py</div>
      <pre class="code-display language-python" data-code="sort_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">Dutch National Flag — 0, 1, 2 Sort</div>
      <div class="prob-desc">0, 1, 2 আছে এমন array কে one-pass এ sort করো। ৩টি pointer — low, mid, high। O(n) time, O(1) space।</div>
      <div class="io-box">Input:  [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]</div>
      <div class="code-wrapper">
        <div class="code-label">📄 dutch_flag.py</div>
        <pre class="code-display language-python" data-code="sort_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Frequency অনুযায়ী Sort করো</div>
      <div class="prob-desc">Counter দিয়ে frequency গণো, তারপর (-freq, value) key দিয়ে sort করো। বেশি আসা আগে, same হলে ছোট আগে।</div>
      <div class="io-box">Input:  [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
Output: [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]</div>
      <div class="code-wrapper">
        <div class="code-label">📄 freq_sort.py</div>
        <pre class="code-display language-python" data-code="sort_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Counting Sort implement করো। Non-negative integers এর জন্য O(n+k) sort।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Merge Sort দিয়ে Inversion Count করো। Array তে কতটি pairs (i,j) আছে যেখানে i&lt;j কিন্তু arr[i]&gt;arr[j]।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Strings Sort করো length অনুযায়ী। Same length হলে alphabetically sort করো।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Meeting Rooms: N টি meeting আছে [start, end] interval দেওয়া। সব meeting করতে ন্যূনতম কতটা room লাগবে?</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>QuickSelect: Array তে K-th smallest element O(n) average time এ খুঁজো। Quicksort partition ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 9: HASHING                -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-9">
  <div class="ch-badge">Chapter 09</div>
  <h2 class="ch-title">Hashing</h2>
  <p class="ch-sub">Hash Map এবং Hash Set — O(1) average time এ insert, search, delete। সবচেয়ে versatile data structure।</p>

  <div class="section">
    <h3 class="sec-title">Hashing কী?</h3>
    <div class="card">
      <p><strong>Hashing</strong> হলো একটি technique যেখানে key কে একটি hash function দিয়ে array এর index এ map করা হয়।</p>
      <p><strong>Hash Function:</strong> key → index। যেমন: hash("name") % 10 = 4</p>
      <p><strong>Collision:</strong> যখন দুটো ভিন্ন key একই index এ map হয়। Handle করার উপায়: Chaining (linked list) বা Open Addressing।</p>
      <p>Python এ dict এবং set হলো built-in Hash Map এবং Hash Set।</p>
    </div>
    <div class="viz">  Hash Map (size=5):

  hash(key) = sum(ord(ch)) % 5

  put("age", 22):  hash("age") = (97+103+101)%5 = 1
  put("name", X):  hash("name")= (110+97+109+101)%5 = 2

  Index  Bucket
  ┌───┬──────────────────────┐
  │ 0 │ []                   │
  │ 1 │ [("age", 22)]        │
  │ 2 │ [("name", "Rakib")]  │  ← Chaining
  │ 3 │ []                   │
  │ 4 │ []                   │
  └───┴──────────────────────┘

  Python dict → average O(1) for all operations
  Worst case O(n) when too many collisions</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 hashing.py</div>
      <pre class="code-display language-python" data-code="hash_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">Two Sum</div>
      <div class="prob-desc">Array তে এমন দুটো number খুঁজো যাদের যোগফল target। Hash Map এ complement (target-num) খুঁজলে O(n) তেই হয়।</div>
      <div class="io-box">nums=[2,7,11,15], target=9  →  [0,1]  (2+7=9)
nums=[3,2,4],   target=6  →  [1,2]  (2+4=6)</div>
      <div class="code-wrapper">
        <div class="code-label">📄 two_sum.py</div>
        <pre class="code-display language-python" data-code="hash_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Duplicate খুঁজো</div>
      <div class="prob-desc">Hash Set বা Counter দিয়ে frequency track করো। যার count > 1, সে duplicate। First non-repeating ও বের করো।</div>
      <div class="io-box">arr=[1,2,3,4,2,5,6,3,7]
Duplicates: [2, 3]
First non-repeating: 1</div>
      <div class="code-wrapper">
        <div class="code-label">📄 find_duplicate.py</div>
        <pre class="code-display language-python" data-code="hash_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Anagram Check: দুটো string anagram কিনা বলো। Counter বা sorted string compare করো।</div><span class="diff easy">Easy</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Group Anagrams: একটি list এর সব anagram গুলো একসাথে group করো। Sorted string কে key হিসেবে ব্যবহার করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Longest Consecutive Sequence: Array তে সবচেয়ে লম্বা consecutive numbers এর sequence এর length বের করো। O(n)।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Subarray with Zero Sum: Array তে এমন subarray আছে কিনা যার sum = 0। Prefix sum + Hash Map।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>LRU Cache implement করো — Least Recently Used। OrderedDict বা Doubly Linked List + Hash Map ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════ -->
<!-- CHAPTER 10: GRAPH                 -->
<!-- ══════════════════════════════════ -->
<section class="chapter" id="ch-10">
  <div class="ch-badge">Chapter 10</div>
  <h2 class="ch-title">Graph</h2>
  <p class="ch-sub">Vertices এবং Edges এর সমষ্টি। BFS, DFS, Shortest Path — সব problem এর ভিত্তি।</p>

  <div class="section">
    <h3 class="sec-title">Graph কী?</h3>
    <div class="card">
      <p><strong>Graph</strong> হলো G = (V, E) যেখানে V = Vertices (শীর্ষ বিন্দু) এবং E = Edges (সংযোগ)।</p>
      <p><strong>Undirected Graph:</strong> Edge দুদিকেই যায়। যেমন: Facebook friends।</p>
      <p><strong>Directed Graph (Digraph):</strong> Edge একদিকেই যায়। যেমন: Twitter follow।</p>
      <p><strong>Weighted Graph:</strong> প্রতিটি edge এর weight/cost আছে। যেমন: Google Maps road distances।</p>
    </div>
    <div class="viz">  Undirected Graph:          Adjacency List:
                                   1: [2, 3]
      1 ──── 2                     2: [1, 4, 5]
      |    / |                     3: [1, 6, 7]
      |   /  |                     4: [2]
      3 ──── 5                     5: [2, 3]
      |                            6: [3]
      6                            7: [3]

  BFS from 1: [1, 2, 3, 4, 5, 6, 7]  (level by level)
  DFS from 1: [1, 2, 4, 5, 3, 6, 7]  (deep first)

  Graph Representations:
  ┌────────────────┬──────────────┬──────────────┐
  │ Representation │ Space        │ Add Edge     │
  ├────────────────┼──────────────┼──────────────┤
  │ Adj. Matrix    │ O(V²)        │ O(1)         │
  │ Adj. List      │ O(V+E)       │ O(1)         │
  └────────────────┴──────────────┴──────────────┘</div>
  </div>

  <div class="section">
    <h3 class="sec-title">Implementation — Python (BFS + DFS)</h3>
    <div class="code-wrapper">
      <div class="code-label">📄 graph.py</div>
      <pre class="code-display language-python" data-code="graph_impl"></pre>
    </div>
  </div>

  <hr class="divider">

  <div class="section">
    <h3 class="sec-title">✅ Solved Problems</h3>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 1</div>
      <div class="prob-title">BFS দিয়ে Shortest Path</div>
      <div class="prob-desc">Unweighted graph এ BFS সবসময় shortest path দেয়। পুরো path list track করো, target পেলেই return করো।</div>
      <div class="io-box">A–B–C–D–E–F–G network:
shortest_path(A, G) = A → B → D → G
shortest_path(A, F) = A → C → F</div>
      <div class="code-wrapper">
        <div class="code-label">📄 shortest_path.py</div>
        <pre class="code-display language-python" data-code="graph_p1"></pre>
      </div>
    </div>
    <div class="prob-card">
      <div class="prob-tag">⚡ SOLVED PROBLEM 2</div>
      <div class="prob-title">Undirected Graph এ Cycle Detection</div>
      <div class="prob-desc">DFS করার সময় যদি visited node পাই এবং সে current এর parent না হয়, তাহলে cycle আছে।</div>
      <div class="io-box">0–1–2–3–0 (cycle) → True
0–1–2–3   (path)  → False</div>
      <div class="code-wrapper">
        <div class="code-label">📄 cycle_detection.py</div>
        <pre class="code-display language-python" data-code="graph_p2"></pre>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="tasks-card">
      <div class="tasks-hdr">🎯 Practice Tasks</div>
      <ul class="task-list">
        <li class="task-item"><div class="task-n">1</div><div>Number of Islands: 2D grid এ '1' (land) এবং '0' (water) আছে। কতটি island আছে গণো। BFS/DFS ব্যবহার করো।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">2</div><div>Topological Sort: Directed Acyclic Graph (DAG) এর সব vertex কে এমন order এ সাজাও যেন u→v edge এ u, v এর আগে আসে।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">3</div><div>Dijkstra's Algorithm implement করো — Weighted Graph এ single source shortest path। heapq ব্যবহার করো।</div><span class="diff hard">Hard</span></li>
        <li class="task-item"><div class="task-n">4</div><div>Bipartite Graph Check: Graph কে দুটো group এ ভাগ করা যায় কিনা যেখানে একই group এর মধ্যে কোনো edge নেই।</div><span class="diff med">Medium</span></li>
        <li class="task-item"><div class="task-n">5</div><div>Word Ladder: শুধু একটি letter বদলে একটি word থেকে আরেকটিতে যাও। সর্বোচ্চ কম step এ target word এ পৌঁছাও। BFS।</div><span class="diff hard">Hard</span></li>
      </ul>
    </div>
  </div>
</section>

</main>

<!-- ═══════════════════════════════════════ -->
<!-- ALL PYTHON CODE STORED IN JS           -->
<!-- ═══════════════════════════════════════ -->
<script>
const CODE = ''' + '{' + '''
};
</script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>

<script>
// ─── Navigation ───
function showChapter(n) {
  document.querySelectorAll('.chapter').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
  document.getElementById('ch-' + n).classList.add('active');
  document.querySelectorAll('.nav-item')[n - 1].classList.add('active');
  window.scrollTo(0, 0);
}

// ─── Inject code into pre blocks ───
document.querySelectorAll('.code-display[data-code]').forEach(pre => {
  const key = pre.getAttribute('data-code');
  const code = pre.getAttribute('data-code');
  pre.innerHTML = '<code class="language-python"></code>';
  pre.querySelector('code').textContent = (CODE[key] || '# Code not found').trim();
});
Prism.highlightAll();
</script>
</body>
</html>'''

# Now insert all code into the JS CODE object
import json

# Build the JS code object string
js_parts = []
for key, val in codes.items():
    # The code is stored as JS string — escape backticks and backslashes
    escaped = val.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js_parts.append(f'  {json.dumps(key)}: `{escaped}`')

js_object = 'const CODE = {\n' + ',\n'.join(js_parts) + '\n};'

# Replace placeholder
HTML = HTML.replace('const CODE = ' + '{' + '\n};', js_object)

# Write to file
output_path = '/mnt/user-data/outputs/ds_complete_guide.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"Generated: {output_path}")
print(f"File size: {len(HTML):,} bytes ({len(HTML)//1024} KB)")
print(f"Chapters: 10 (Stack, Queue, Heap, LL, Tree, BST, Searching, Sorting, Hashing, Graph)")
print(f"Code blocks: {len(codes)}")
PYEOF
echo "Script created successfully"
Output

Command argument is 118_880 bytes, exceeding the 100_000-byte per-argument limit. For large content, pipe via stdin or use a file-write API instead of embedding the content inline in the command. Argument preview: 'mkdir -p /home/claude/ds_guide && cat > /home/claude/ds_guide/generate.py << \'PYEOF\'\n#!/usr/bin/env python3\n"""Generate Data Structures Complete Guide HTML"""\n\n# ──────────────────────────────────────'
Done

You are out of free messages until 8:50 PM
Get more




