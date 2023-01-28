"""
A binary search tree can have atmost 2 children
Left Child must always be smaller than parent node
Right Child must always be greater than parent node
Left & Subtree must also be a binary search tree
                        Average  Worst
Space time complexity - O(n)    O(n)
Access time -           O(logn) O(n)
Search time -           O(logn) O(n)
Insertion time -        O(logn) O(n)
Deletion time -         O(logn) O(n)

"""
#--------------------------------------------------------------------------
#  Import Statements
#--------------------------------------------------------------------------
import sys, re, os

# Checking Python Version befor running the scirpt
if sys.version_info[0] < 3:
    # Exit for Python 2
    print ("The script is written in Python 3.7 and cannot be \
        executed in a python 2 version")
    sys.exit()
elif sys.version_info[0] == 3 & sys.version_info[1] > 7:
    print ("The script is written in Python 3.7 and executing this \
        in a version greater than 3.7 might not work as expected. \
        So giving you a prior headsup****")
else:
    pass

# changing the directory to the location where this script is present
# expecting abc_emp_data.txt and prompts.txt to be available in this location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#--------------------------------------------------------------------------
#  Global Constants
#--------------------------------------------------------------------------
HIPHENS = 80
SUBID = "Search by ID"
SUBNAME = "Search by Name: "
SUBDESG = "List Employees by Designation: "


#--------------------------------------------------------------------------
#  Node Class
#--------------------------------------------------------------------------
class EmpNode:
    def __init__(self,empID=None, empName=None, empDesg=None):
        """
        Init method to create a node for BST
        :param empID: int
        :param empName: string
        :param empDesg: string
        """
        self.value=empID
        self.empName = empName
        self.empDesg = empDesg
        self.left_child = None
        self.right_child = None


#--------------------------------------------------------------------------
#  BST Class
#--------------------------------------------------------------------------
class binary_search_tree:
    def __init__(self):
        """
        Init method to create initialize BST
        """
        self.root=None # root node of BST

    def insert(self,empID, empName, empDesg):
        """
        Recursive Method to insert a new node into BST
        :param empID:
        :param empName:
        :param empDesg:
        :return:
        """
        if self.root==None:
            self.root=EmpNode(empID,empName,empDesg)
        else:
            self._insert(empID,empName,empDesg,self.root)

    def _insert(self,value,empName,empDesg,cur_node):
        # Class Private method
        if value < cur_node.value:
            # Handling Left Childs
            if cur_node.left_child==None:
                cur_node.left_child=EmpNode(value,empName,empDesg)
            else:
                self._insert(value,empName,empDesg,cur_node.left_child)
        elif value > cur_node.value:
            # Handling Right childs
            if cur_node.right_child==None:
                cur_node.right_child=EmpNode(value,empName,empDesg)
            else:
                self._insert(value,empName,empDesg,cur_node.right_child)
        else:
            print (f"Value already in tree! No duplicates allowed {value}")

    def count_nodes(self):
        """
        Recursive Method to print BST in Inorder fashion
        :return:
        """
        if self.root!=None:
            num_nodes = self._count_nodes(self.root)
            return num_nodes
        else:
            return 0

    def _count_nodes(self,cur_node):
        # Class private method
        if cur_node!=None:
            # In order traversal Left, Parent, Right
            # Advantage: reads data in a sorted order fashion
            return 1 + self._count_nodes(cur_node.left_child) + self._count_nodes(cur_node.right_child)
        else:
            return 0

    def findbyID(self,value):
        """
        Recursive method to find a node based on the input value (empID).
        :param value:
        :return: matched Node value (empID)
        """
        if self.root!=None:
            return self._findbyID(value,self.root)
        else:
            return None

    def _findbyID(self,value,cur_node):
        """
        # Class private method
        Asymptotic Analysis:
            * The average find operation would be halved for each recursive call under a balance BST, leading
              to theta(log(n)) where n is the number of nodes
            * The worst case find oepration would be to look at every node in each layer typically for an unbalanced BST
              leanding to theta(n)
        """
        if value==cur_node.value:
            return cur_node.empName
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._findbyID(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._findbyID(value,cur_node.right_child)

    def findbyName(self, empName):
        """
        Recursive method to search for name in BST and return matched empIDs
        :param empName:
        :return:
        """
        if self.root!=None:
            matchedIDs = []
            self._findbyName(self.root, empName, matchedIDs)
            return matchedIDs
        else:
            return []

    def _findbyName(self,cur_node, empName, matchedIDs):
        # Class private method
        if cur_node!=None:
            self._findbyName(cur_node.left_child, empName, matchedIDs)
            # In order traversal for Sorted Order
            # Case insensitive search
            if cur_node.empName.lower().find(empName.lower()) != -1:
                # The code returns True if there is a partial match in the Name
                # for instance "urya" in "Surya", "Raj" in "Rajesh"
                matchedIDs.append([cur_node.empName, cur_node.value])
            self._findbyName(cur_node.right_child, empName, matchedIDs)

    def findbyDesignation(self, empDesg):
        """
        Recursive Method to search for all nodes matching an Designation and returns
        sorted order (empId)
        :param empDesg:
        :return:
        """
        if self.root!=None:
            matchedEntity = []
            self._findbyDesignation(self.root, empDesg, matchedEntity)
            return matchedEntity
        else:
            return []

    def _findbyDesignation(self,cur_node, empDesg, matchedEntity):
        # Class private method
        if cur_node!=None:
            self._findbyDesignation(cur_node.left_child, empDesg, matchedEntity)
            # In order traversal for Sorted Order
            # exact case insensitive search for designation
            if (cur_node.empDesg.lower() == empDesg.lower()):
                # The code returns True if there is a partial match in the Designation
                # for instance "product" in "Product Manager"
                _ = [cur_node.empName, cur_node.value]
                matchedEntity.append(_)
            self._findbyDesignation(cur_node.right_child, empDesg, matchedEntity)

#--------------------------------------------------------------------------
#  Prompt Methods
#--------------------------------------------------------------------------

def idSearch(searchList, searchTree, destinationFile):
    """
    Method that searches tree based on ID value and writes the result to output file
    """
    if searchList:
        destinationFile.write("-" * ( (HIPHENS - len(SUBID))//2 ) + f"{SUBID}" + "-" * ( (HIPHENS - len(SUBID))//2 ) + "\n")
        for eachId in searchList:
            searchResult = searchTree.findbyID(int(eachId))
            searchResult = searchResult if searchResult is not None else "not found"
            destinationFile.write(f"{eachId} {searchResult}\n")
        # End of search
        destinationFile.write("-"*80 + "\n")


def name_or_desgSearch(searchList, searchMethod, destinationFile, seperator):
    """
    Method that searches tree based on Name/Designation value and writes the result to output file
    """
    if searchList:
        for eachItem in searchList:
            destinationFile.write( "-" * ( (HIPHENS - len(seperator) - len(eachItem))//2 ) + f"{seperator}{eachItem}" + \
                "-" *( (HIPHENS - len(seperator) - len(eachItem))//2 ) + "\n"  )
            searchResult = searchMethod(eachItem)
            if searchResult:
                for eachId in searchResult:
                    destinationFile.write(f"{eachId[0]} {eachId[1]}\n")
            else:
                destinationFile.write(f"No {eachItem} found in BST\n")
        # End of search
        destinationFile.write("-"*80 + "\n")


#--------------------------------------------------------------------------
#  __main__
#--------------------------------------------------------------------------
if __name__ == '__main__':
    # Instantiating a BST
    tree = binary_search_tree()
    
    #--------------------------------------------------------------------------
    #  Parsing the Input and creating the BST
    #--------------------------------------------------------------------------

    # Parsing input file and creating the tree
    with open("abc_emp_data.txt", "r") as f:
        data = f.readlines()
        for eachline in data:
            try:
                # Expected Input pattern: Name, ID, Designation
                # if ',' in eachline:
                if eachline.count(",") >= 2: 
                    # comma based seperated split
                    empName, empID, empDesg, *_ = eachline.split(',')
                    # if more than 3 items are present, appending last items to designation
                    empDesg = empDesg + " " + " ".join(_)
                elif eachline.count(";") >= 2 :
                    # semi colon based seperated split
                    empName, empID, empDesg, *_ = eachline.split(';')
                    # if more than 3 items are present, appending last items to designation
                    empDesg = empDesg + " " + " ".join(_)
                elif eachline.count(":") >= 2:
                    # semi colon based seperated split
                    empName, empID, empDesg, *_ = eachline.split(':')
                    # if more than 3 items are present, appending last items to designation
                    empDesg = empDesg + " " + " ".join(_)
                else:
                    print ("Unknown parameter used for splitting <empName><empID><empDesg>, expecting comma seperation")
                    sys.exit()
            except Exception as e:
                print(f"Exception: {e}")
            try:
                tree.insert(int(empID.strip()), empName.strip(), empDesg.strip())
            except ValueError as e:
                print(f"Exception: {e}")
            except Exception as e:
                print(f"Exception: {e}")
    

    # Storage for keeping track of various operations that are to be 
    # written to the final output.txt file
    findByID = []
    findByName = []
    findbyDesignation = []

    #--------------------------------------------------------------------------
    #  Parsing the Prompt
    #--------------------------------------------------------------------------

    with open("prompts.txt", "r") as f:
        data = f.readlines()
        for index, eachline in enumerate(data):
            #****************************
            #***** Search ID: ***********
            #****************************
            # Case and Syntax insensitive search mechanism
            if all([ term.lower() in eachline.lower() for term in ["Search", "ID", ":"]]):
                m = re.search(r"Search\s*ID\s*:\s*[\"\']?(\d+)[\"\']?", eachline, re.IGNORECASE)
                if m:
                    # rstript is used to remove any trailing "\n" characters
                    # removing any unwanted quotes
                    searchWord = re.sub(r"[\"\']", "", m.group(1).rstrip())
                    findByID.append(searchWord)
                else:
                    print (f"No ID found to search in Line no {index+1}: \"{eachline.rstrip()}\"")
            #****************************
            #***** Search Name: *********
            #****************************
            # Case and Syntax insensitive search mechanism
            elif all([ term.lower() in eachline.lower() for term in ["Search", "Name", ":"]]):
                # Expecting that Employee Name may contain any of the following characters
                #  Alphabets A-Z, a-z
                #  A space
                #  An underscore
                #  Numbers 0-9
                #  A hiphen
                #  A dot
                #  A quote              
                m = re.search(r"Search\s*Name\s*:\s*([A-Za-z\s_0-9-\.\'\"]+)", eachline, re.IGNORECASE)
                if m:
                    # removing any unwanted quotes
                    searchWord = re.sub(r"[\"\']", "", m.group(1).rstrip())
                    if searchWord != "":
                        findByName.append(searchWord)
                    else:
                        print(f"No Name found in Line no {index+1}: \"{eachline.rstrip()}\"")
                else:
                    print (f"No Name found to search in Line no {index+1}: \"{eachline.rstrip()}\"")
            #****************************
            #***** Search Designation: **
            #****************************
            # Case and Syntax insensitive search mechanism
            elif all([ term.lower() in eachline.lower() for term in ["Search", "Designation", ":"]]):
                # Expecting that Designation may contain any of the following characters
                #  Alphabets A-Z, a-z
                #  A space
                #  An underscore
                #  Numbers 0-9
                #  A hiphen
                #  A dot
                #  A quote
                m = re.search(r"Search\s*Designation\s*:\s*([A-Za-z\s_0-9-\.\'\"]+)", eachline,re.IGNORECASE)
                if m:
                    # removing any unwanted quotes
                    searchWord = re.sub(r"[\"\']", "", m.group(1).rstrip())
                    if searchWord != "":
                        findbyDesignation.append(searchWord)
                    else:
                        print(f"No Designation found in Line no {index+1}: \"{eachline.rstrip()}\"")
                else:
                    print(f"No Designation found in Line no {index+1}: \"{eachline.rstrip()}\"")
            else:
                # ignoring rest
                pass


    with open("output.txt", "w") as outfile:
        # writing the number of node entries made to the tree
        outfile.write(str(tree.count_nodes())+ ", Binary Tree Created with the employee details \
            (from file abc_emp_data.txt)" +"\n")
        # Call prompt methods to find and write the output
        idSearch(findByID, tree, outfile)
        name_or_desgSearch(findByName, tree.findbyName, outfile, SUBNAME)
        name_or_desgSearch(findbyDesignation, tree.findbyDesignation, outfile, SUBDESG)

            
#--------------------------------------------------------------------------
#  END OF SCRIPT
#--------------------------------------------------------------------------
