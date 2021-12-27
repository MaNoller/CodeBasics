#Class from Exercise:
class TreeNode:
    def __init__(self, name, position):
        self.name = name
        self.position=position
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,extend):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if extend=='name':
            fix=self.name
        elif extend=='designation':
            fix=self.position
        else:
            fix=self.name +' ('+ self.position + ')'
        print(prefix + fix)
        if self.children:
            for child in self.children:
                child.print_tree(extend)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode('Nilupul', 'CEO')

    chimnay = TreeNode('Chimnay', 'CTO')
    root.add_child(chimnay)
    vishwa=TreeNode('Vishwa', 'Infrastructure Head')
    chimnay.add_child(vishwa)
    vishwa.add_child(TreeNode('Dhaval','Cloud Manager'))
    vishwa.add_child(TreeNode('Abhijit','App Manager'))
    chimnay.add_child(TreeNode('Aamir','Application Head'))
    gels=TreeNode('Gels','HR Head')
    root.add_child(gels)
    gels.add_child(TreeNode('Peter','Recruitment Manager'))
    gels.add_child(TreeNode('Waqas','Policy Manager'))



    '''
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
'''
    root.print_tree('both')
    root.print_tree('designation')
    root.print_tree('name')
'''

Given is the management hierarchy of a company.
Extent tree class built in our main tutorial so that it takes name
 and designation in data part of TreeNode class. Now extend print_tree function
  such that it can print either name tree, designation tree or name and designation tree.
   As shown below,..
   

Here is how your main function should will look like,
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
'''


if __name__ == '__main__':
    build_product_tree()