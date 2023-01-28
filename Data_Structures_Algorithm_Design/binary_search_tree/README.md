# Binary search tree

# Problem Statement 

In a company named “ABC”, the employees are identified by their employee ID and name. The 
employee details are stored in a binary search tree data structure format. The employee details 
contain Employee name, employee ID and designation. The details are inserted into the binary search
tree data type based on the employee ID (employee ID is an integer data type). The employee Id is 
assigned based on the joining date of the employee. For example, the employee who joined latest will 
have the highest employee ID. 

# The following operations are expected to perform

1. Employee name and their details are stored in a file “abc_emp_data.txt”. Program should 
read the data from the file and create a BST with each node having the following details 
<employee ID> <employee name> <Designation>
2. Search for the employee with their employee ID. 
3. List the Id’s of all the employees for a given input name. 
4. For an inputted employee designation, list all the employee with the name and ID based on the 
joining date.

# Requirement:

1. Implement the above problem statement using Python 3.7.
2. Create a BST data structure for storing employee details. The details should be read from a 
file “abc_emp_data.txt”. The program should create BST with a single node containing 
details such as <employee ID> <employee name> and < Designation>. Each employee details 
are in single line where the details are separated by “,”. In the output file “output.txt”, 
enter the total number of employee records that are created. 
3. Search and list all the details of employees from the prompt file. The file “prompts.txt”
contain the list of abc’s employees IDs with a tag “Search ID:”. The program should be written 
to search the BST for each employee ID from the same file and the corresponding details 
should be written into the file “output.txt”. If an employee ID is not present in the BST, 
the program should write “not found” in the file.
4. Search for all employees for a given input name. The name to be searched will be provided 
with a tag “Search Name:” in the file “prompts.txt” and Id no’s of the employees 
matching with the given name should be output to the file “output.txt”
5. List the employee name and ID as per the seniority for a prompted designation. Seniority is 
calculated based on the employee id. The employee with the lower employee id is more senior 
than the one with a higher employee id. The designation to be searched will be provided with 
a tag “Search Designation:” in the file “prompts.txt” The result including the employee 
name and employee id should be written to a file called “output.txt”
6. Perform an analysis for the features above and give the running time in terms of input size: n.

# Sample input files

Details of the employee should be provided using a comma separated list. One employee’s details 
will be present per line. 

# Sample abc_emp_data.txt
  
  Rajesh Sharma, 1004, CEO
  
  Jordan Leon, 1012, Project Manager
  
  Mark Antony, 1006, CTO
  
  Divya Rajesh, 1013, software Engg
  
  Anvar Mohamed, 1017, Project Manager
  
  Rajesh Nair, 1103, Software Engg
  
  Najeem Ali, 1105, PRO
  
  Sony Rajesh, 1015, Project Manager
  
  Arun Kumar, 1009, Trainee

# Sample prompts.txt

  Search ID: 1004
  
  Search ID: 1005
  
  Search ID: 1006
  
  Search ID: 1009
  
  Search ID: 1105
  
  Search Name: Rajesh
  
  Search Designation: Project Manager

# Sample output and output files

  Below is the sample output after executing 

# Sample output.txt

9 Binary Tree Created with the employee details (from file abc_emp_data.txt”)

  ------------- Search by ID ---------------
  
  1004 Rajesh Sharma
  
  1005 not found
  
  1006 Mark Antony
  
  1009 Arun Kumar
  
  1105 Najeem Ali
  
  --------------------------------------------

  ------------- Search by Name: Rajesh -----------
  
  Rajesh Sharma
  
  Divya Rajesh
  
  Sony Rajesh
  
  Rajesh Nair
  
  -----------------------------------------------

  -----------List Employees by Designation: Project Manager -------------
  
  Jordan Leon, 1012
  
  Sony Rajesh, 1015
  
  Anvar Mohamed, 1017
  
  ------------------------------------------------------------------------
