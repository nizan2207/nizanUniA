import copy
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return '[' + str(self.value) + ']'


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key) + ": " + str(self.val)

    def is_leaf(self):
        return (self.left == None) and (self.right == None)

    def find_successor(self):
        if self.right is None:
            return None
        tmp = self.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp


class Binary_search_tree():
    def __init__(self):
        self.root = None

    def search(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def find_parent(self, key):
        parent = self.root
        children = self.root

        if self.root.key == key:
            return None, self.root

        while children.key != key:
            parent = children
            if parent.key > key:
                if parent.left is not None:
                    children = parent.left
                else:
                    return
            elif parent.key < key:
                if parent.right is not None:
                    children = parent.right
                else:
                    return
            else:
                break
        return parent, children

    def delete(self, key):
        if not self.search(key):
            return
        parent, children = self.find_parent(key)
        if children.is_leaf():  # basic case
            if parent is not None:
                if children.key > parent.key:
                    parent.right = None
                else:
                    parent.left = None

            else:
                self.root = None

        elif children.left is None:  # has one children - right
            if parent is not None:
                if children.key > parent.key:
                    parent.right = children.right
                else:
                    parent.left = children.right
            else:
                self.root = children.right

        elif children.right is None:  # has one children - left
            if parent is not None:
                if children.key < parent.key:
                    parent.left = children.left
                else:
                    parent.right = children.left
            else:
                self.root = children.left

        else:  # complicate case - 2 children
            successor = children.find_successor()
            successor_parent, successor = self.find_parent(successor.key)
            if successor.right is not None:
                if successor_parent.key != key:  # successor_parent shouldn't be deleted
                    successor_parent.left = successor.right
                else:
                    if children.key > parent.key:
                        parent.right = children.right
                    else:
                        parent.left = children.right
            else:  # successor is leaf
                if successor_parent.key > successor.key:
                    successor_parent.left = None
                else:
                    successor_parent.right = None
                children.key = successor.key
                children.val = successor.val

    def inorder(self):
        ''' return inorder traversal of values as str, uses recursion '''

        def inorder_rec(curr_node, res):
            if curr_node != None:
                inorder_rec(curr_node.left, res)
                res.append((curr_node.key, curr_node.val))
                inorder_rec(curr_node.right, res)
            return res

        if self.root == None:  # empty tree
            return []
        else:
            return inorder_rec(self.root, [])

    def __repr__(self):
        # no need to understand the implementation of this one
        out = ""
        # need printree.py file or make sure to run it in the NB
        for row in printree(self.root):
            out = out + row + "\n"
        return out

def printree(t, bykey=True):
    """Print a textual representation of t
        bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)

def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))

def conc(left, root, right):
    """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result

def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1

def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Subject:
    def __init__(self, name, grade, points):
        self.name = name
        self.grade = float(grade)
        self.points = float(points)

    def __repr__(self):
        return "" + self.name + ", " + str(self.grade) + "[" + str(self.points) + "]"


class Student:
    def __init__(self, name, student_id):
        self.name = str(name)
        self.student_id = int(student_id)
        self.head = None
        self.points = 0.0

    def Add(self, val, temp):
        if temp is None:
            return False
        if temp.value.name == val.name:
            if temp.value.grade < 56.0 and val.grade >= 56.0:
                self.points += val.points
            if temp.value.grade >= 56.0 and val.grade < 56.0:
                self.points-= temp.value.points
            temp.value = val
            return True
        return self.Add(val, temp.next)
    """
    def add_subjects(self, lst):
        if self.head is None:
            self.head = Node(lst[0])
            if lst[0].grade >= 56:
                self.points += lst[0].points
            lst.remove(lst[0])
        list_of_indexes = []
        for i in range(len(lst)):
            if self.Add(lst[i], self.head):
                list_of_indexes.append(i)
        for i in list_of_indexes:
            lst.remove(lst[i])
        if len(lst) == 0:
            return
        else:
            temp = self.head
            if self.head.next is None:
                self.head.next = Node(lst[0])
                if lst[0].grade >= 56:
                    self.points += lst[0].points
                lst.remove(lst[0])
            while self.head.next is not None:
                self.head = self.head.next
            for i in range(len(lst)):
                if lst[i].grade >= 56:
                    self.points += lst[i].points
                self.head.next = Node(lst[i])
                self.head = self.head.next
            self.head = temp
    """
    def add_subjects(self, lst):
        if self.head is None:
            self.head = Node(lst[len(lst)-1])
            if lst[len(lst)-1].grade >= 56.0:
                self.points += lst[len(lst)-1].points
            lst.remove(lst[len(lst)-1])
        list_of_indexes = []
        for i in range(len(lst)):
            if self.Add(lst[i], self.head):
                list_of_indexes.append(i)
        for i in reversed(list_of_indexes):
            lst.remove(lst[i])
        if len(lst) == 0:
            return
        else:
            temp = self.head
            if self.head.next is None:
                self.head.next = Node(lst[len(lst)-1])
                if lst[len(lst)-1].grade >= 56.0:
                    self.points += lst[len(lst)-1].points
                lst.remove(lst[len(lst)-1])
            while self.head.next is not None:
                self.head = self.head.next
            for i in range(len(lst)-1,-1,-1):
                if lst[i].grade >= 56.0:
                    self.points += lst[i].points
                self.head.next = Node(lst[i])
                self.head = self.head.next
            self.head = temp

    def get_average(self):
        top, bottum = 0.0, 0.0
        tem = self.head
        if self.head is None:
            return 0.0
        else:
            while tem is not None:
                top += (tem.value.grade * tem.value.points)
                bottum += tem.value.points
                tem = tem.next
        return top / bottum

    def _eq_(self, other):
        return self.get_average() == other.get_average()

    def _ne_(self, other):
        return not self._eq_(other)

    def _ge_(self, other):
        return self.get_average() >= other.get_average()

    def _le_(self, other):
        return self.get_average() <= other.get_average()

    def _gt_(self, other):
        return self.get_average() > other.get_average()

    def _lt_(self, other):
        return self.get_average() < other.get_average()

    def is_warning(self):
        if self.head is None: return False
        c = 0.0
        ll = self.head
        while ll is not None:
            if ll.value.grade < 56.0: c += 1.0
            ll = ll.next
        return c >= 2.0 or self.get_average() <= 65.0

    def largest(self):
        if self.head is not None:
            l = self.head.value
            while self.head is not None:
                self.head = self.head.next
                if self.head.value.grade > l.grade:
                    l = self.head.value
            return l.grade
        else:
            return 0.0

    def __repr__(self):
        s = ""
        if self.head is not None:
            temp = self.head
            while temp is not None:
                s += temp.value.name + "(" + str(temp.value.points) + ")" + "-" + str(temp.value.grade) + ", "
                temp = temp.next
            s = s.rstrip(", ")
        grade = "no subjects yet" if self.head is None else s
        return "Student " + self.name + "[" + str(self.student_id) + "], " + "avg:" + str(
            self.get_average()) + ", points:" + str(self.points) + ", grades:" + grade + "."


class ForeignStudent(Student):
    def __init__(self, name, student_id):
        Student.__init__(self,name,student_id)

    def get_highest_grade(self):
        temp = self.head
        high = -1
        while temp is not None:
            if temp.value.grade > high:
                high = temp.value.grade
            temp = temp.next
        return high

    def get_average(self):
        if self.head is None:
            return  0.0
        return ((float(float(self.get_highest_grade()) + float(Student.get_average(self))))/2.0)
    
    def __repr__(self):
        s = ""
        if self.head is not None:
            temp = self.head
            while temp is not None:
                s += temp.value.name + "(" + str(temp.value.points) + ")" + "-" + str(temp.value.grade) + ", "
                temp = temp.next
            s = s.rstrip(", ")
        grade = "no subjects yet" if self.head is None else s
        return "ForeignStudent " + self.name + "[" + str(self.student_id) + "], " + "avg:" + str(
            self.get_average()) + ", points:" + str(self.points) + ", grades:" + grade + "."

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def front(self):
        if self.isEmpty():
            return None
        return self.items[self.__len__()-1]

    def rear(self):
        if self.isEmpty():
            return None
        return self.items[0]


    def __len__(self):
        return len(self.items)

    def __repr__(self):
        s = ""
        for i in range(self.__len__()):
            if i < self.__len__()-1:
                s += (str(self.items[i])) + "\n"
            if i == self.__len__()-1:
                s += (str(self.items[i]))
        return  s

class Department:
    def __init__(self, name):
        self.name = name
        self.students_BST = Binary_search_tree()
        self.id2nodes = {}

    def printInorder(self,root, s):

        if root:
            # First recur on left child
            self.printInorder(root.left,s)

            # then print the data of node
            s += str(root.val) + "\n"

            # now recur on right child
            self.printInorder(root.right,s)
        return s


    def __repr__(self):
        s = ""
        s+= "Department: " + self.name + "\n"
        #s+= self.printInorder(self.students_BST,s)
        temp = self.students_BST.inorder()
        for i in range(len(temp)):
            s+= str(temp[i])[1:len(str(temp[i]))-2] + "\n"
        return s

    def insert(self, student):
        if student.student_id in self.id2nodes:
            return
        self.students_BST.insert(student.get_average(),student)
        self.id2nodes[student.student_id] = copy.copy(self.students_BST.search(student.get_average()))

    def delete_student_by_id(self, student_id):
        if student_id in self.id2nodes:
            self.students_BST.delete(self.id2nodes[student_id].val.get_average())
            del self.id2nodes[student_id]
        else:
            return

    def add_subject_by_student_id(self,student_id,subjcet):
        if student_id not in self.id2nodes:
            return
        else:
            student = self.id2nodes[student_id]
            self.delete_student_by_id(student_id)
            lst =[]
            lst.append(subjcet)
            student.val.add_subjects(lst)
            self.insert(student.val)

    def warnings(self):
        q = Queue()
        for i in self.id2nodes.keys():
            temp = self.id2nodes[i].val.head
            count = 0
            while temp is not None:
                if temp.value.grade < 56:
                    count+=1
                temp = temp.next
            #if self.id2nodes[i].val.get_average() != 0.0:
            if self.id2nodes[i].val.is_warning():
                #if self.id2nodes[i].val.get_average() <=65 or count>=2:
                q.enqueue(self.id2nodes[i].val)
        return q




"""
uriel = Student('Uriel', 654321)
#print(uriel)
uriel.add_subjects([Subject('Alegbra', 93, 4.5), Subject("Python", 95, 4), Subject("sql", 45, 2)])
ariel = ForeignStudent('Uriel', 123456)
dor = ForeignStudent('dor', 132456)
#print(uriel)
ariel.add_subjects([Subject('Alegbra', 93, 4.5), Subject("Python", 95, 4), Subject("sql", 45, 2)])
dor.add_subjects([Subject('Alegbra', 50, 4.5), Subject("Python", 60, 4), Subject("sql", 70, 2)])

print(uriel)
uriel.add_subjects([Subject("sql", 56, 2)])
print(uriel)
uriel.add_subjects([Subject("sql", 30, 2.5)])
print(uriel)
print(uriel.is_warning())
"""
#"""
"""
q = Queue()
print(len(q))
print(q.isEmpty())
print(q.rear())
print(q.front())
q.enqueue(3)
q.enqueue(4)
q.enqueue(5.5)
print("start")
print(q)
print("end")
print(len(q))
print(q.isEmpty())
print(q.rear())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
"""
"""
hapytana = Department("Hapytana")
hapytana.insert(uriel)
hapytana.insert(ariel)
hapytana.insert(dor)
print(hapytana)
print(hapytana.students_BST)
hapytana.delete_student_by_id(123456)
print(hapytana.students_BST)
print(hapytana)
#hapytana.add_subject_by_student_id(132456,Subject("snooker",100,5))
print(hapytana)
print(hapytana.warnings())
#"""
#"""
print(Subject('Algebra',93,4.5))
uriel=Student('Uriel',654321)
print(uriel)
print(str(uriel)=="Student Uriel[654321], avg:0.0, points:0.0, grades:no subjects yet.")
uriel.add_subjects([Subject('Algebra',93,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
print(uriel)
uriel.add_subjects([Subject('Algebra',93,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
print(uriel)
print(str(uriel)=="Student Uriel[654321], avg:84.61904761904762, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
uriel.add_subjects([Subject('SQL',56,2)])
print(uriel)
print(str(uriel)=="Student Uriel[654321], avg:86.71428571428571, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
uriel.add_subjects([Subject('SQL',30,2.5)])
print(uriel)
print(str(uriel)=="Student Uriel[654321], avg:79.4090909090909, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
print(uriel.is_warning(),"=?False")
ariel=ForeignStudent('Ariel',132456)
print(ariel)
print(str(ariel)=="ForeignStudent Ariel[132456], avg:0.0, points:0.0, grades:no subjects yet.")
ariel.add_subjects([Subject('Algebra',93,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
print(ariel)
print(str(ariel)=="ForeignStudent Ariel[132456], avg:89.80952380952381, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
ariel.add_subjects([Subject('SQL',56,2)])
print(ariel)
print(str(ariel)=="ForeignStudent Ariel[132456], avg:90.85714285714286, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
ariel.add_subjects([Subject('SQL',30,2.5)])
print(ariel)
print(str(ariel)=="ForeignStudent Ariel[132456], avg:87.20454545454545, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
print(uriel.is_warning(),"=?False")
#print("operator check:")
#print(ariel > uriel,"=?True")
#print(ariel >= uriel,"=?True")
#print(ariel < uriel,"=?False")
#print(ariel > uriel,"=?True")
#print(ariel == uriel,"=?False")
#print(ariel != uriel,"=?True")
#print("-----Queue-----")
#q=Queue()
#print(len(q),"=?0")
#print(q.is_empty(),"=?True")
#print(q.rear(),"=?None")
#print(q.front(),"=?None")
#q.enqueue(3)
#q.enqueue(4)
#q.enqueue(5.5)
#print("print of Queue")
#print(q)
#print("end of print of Queue (make sure there is no space between the last number and this line)")
#print(len(q),"=?3")
#print(q.is_empty(),"=?False")
#print(q.rear(),"=?5.5")
#print(q.front(),"=?3")
#print(q.dequeue(),"=?3")
#print(q.dequeue(),"=?4")
#print(q.dequeue(),"=?5.5")
#print(q.dequeue(),"=?None")
#print(q)
#print("make sure there is a space above this line (cause the queue is empty so it prints an empty string)")
#print("----department------")
hapaytana=Department('Hapaytana')
hapaytana.insert(uriel)
hapaytana.insert(ariel)
print(hapaytana)
print(uriel)
print(ariel)
print(hapaytana.students_BST)
hapaytana.delete_student_by_id(132456)
print(hapaytana.students_BST)
hapaytana.delete_student_by_id(654321)
print(hapaytana.students_BST)
uriel=Student('Uriel',654321)
uriel.add_subjects([Subject('Algebra',93,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
ariel=ForeignStudent('Ariel',132456)
ariel.add_subjects([Subject('Algebra',20,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
assaf=ForeignStudent('Assaf',1212)
assaf.add_subjects([Subject('Algebra',20,4.5),Subject('Python',30,4),Subject('SQL',45,2)])
shay=Student('Shay',909)
shay.add_subjects([Subject('Algebra',10,4.5),Subject('Python',20,4),Subject('SQL',20,2)])
hapaytana.insert(uriel)
hapaytana.insert(ariel)
hapaytana.insert(assaf)
hapaytana.insert(shay)
print(hapaytana.students_BST)
print(hapaytana.id2nodes)
print(hapaytana.warnings())
hapaytana.add_subject_by_student_id(909,Subject("shit",30.0,1.0))
print(shay)
#"""
'''
hapaytana=Department('Hapaytana')
uriel=Student('Uriel',654321)
uriel.add_subjects([Subject('Algebra',60.0,4.5),Subject('Python',70,4),Subject('SQL',80,2.0)])
ariel=ForeignStudent('Ariel',132456)
ariel.add_subjects([Subject('Algebra',50.0,4.5),Subject('Python',60,4),Subject('SQL',70,2.0)])
assaf=ForeignStudent('Assaf',1212)
assaf.add_subjects([Subject('Algebra',20,4.5),Subject('Python',30,4),Subject('SQL',45,2)])
shay=Student('Shay',909)
shay.add_subjects([Subject('Algebra',10,4.5),Subject('Python',20,4),Subject('SQL',20,2)])
hapaytana.insert(uriel)
hapaytana.insert(ariel)
hapaytana.insert(assaf)
hapaytana.insert(shay)
hapaytana.add_subject_by_student_id(132456, Subject('Snooker', 50, 0.5))
hapaytana.add_subject_by_student_id(132456, Subject('Snooker', 50, 0.5))
hapaytana.add_subject_by_student_id(132456, Subject('Snooker', 100, 5.0))
print(uriel)
print(hapaytana.students_BST)
#'''
