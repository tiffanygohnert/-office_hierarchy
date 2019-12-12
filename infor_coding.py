import re

class pretty_print:
    tabs = 1

def print_hierarch(managers,employee_list,tab):
    """Prints out hierarchy of employees
        Params:
        managers (list): list of managers
        employee (list): list of employees
        tab (int): count of tabs

        Return: None


        """
    for x, i in enumerate(managers):
        print("\t"*tab.tabs +"{} \n".format(i) + "\t"*tab.tabs +"Employees of: {}".format(i,i))
        tab.tabs = tab.tabs + 1
        for a in employee_list[x]:
            if a in managers:
                print_hierarch(managers[x+1:],employee_list[x+1:],tab)
                managers.remove(a)
            else: print("\t"*tab.tabs +"{}".format(a))
    return

def get_hierarchy(hier_input):
    """Constructs manager and employee lists
    Params:
    hier_input (string): string of hierarchy

    Return: None


    """
    # Making an assumption that the input parameter is a string.
    if not isinstance(hier_input,str):
        raise ValueError(print("Input needs to be a string"))

    # Assume format stays the same for each hierarchy
    ceo = re.findall(".* \(\$\d+k salary\) is the CEO", hier_input)
    managers_report = re.findall("[A-Z][a-z][a-z]+ has \d+", hier_input)
    managers = re.findall("[A-Z][a-z]+",str(ceo)) + re.findall("[A-Z][a-z]+", str(managers_report))
    employee_list = re.findall("[A-Z][a-z]+\s{0,1}\(\$\d+k\)",hier_input)
    reports = re.findall("\d+ reports", hier_input)

    #Lets make everything pretty now
    get_salarys = re.findall("\d+", str(employee_list))
    employee_list = re.findall("[A-Z][a-z]+",str(employee_list))
    reports = re.findall("\d+", str(reports))

    #sanity check
    if len(reports) != len(managers):
        raise ValueError("Lists don't match we did something wrong!")

    # merge reports and employee_list
    employee_hierarchy_list = []
    for x in (reports):
        employee_hierarchy_list.append(employee_list[0:int(x)])
        del employee_list[0:int(x)]
    for x in employee_hierarchy_list:
        x.sort()

    # Final Output
    tab = pretty_print()
    print_hierarch(managers,employee_hierarchy_list,tab)

    #Print out total salary sum
    print("Total salary: ${},000".format(sum([int(i) for i in get_salarys])))
    return

if __name__ == '__main__':
    hierarchy = "Jeff ($100k salary) is the CEO of a startup. He has 2 reports, Dave ($85k) and Cory($65k). " \
                "Dave has 5 reports: Andy ($65k), Dan ($60k), Jason ($60k), Rick ($56k), and Suzanne ($61k)"
    get_hierarchy(hierarchy)

    # get_hierarchy(19)



# Background
# There are many problems in programming which involving collections of objects that are very similar but
# differ in their containing ability. A common case is that of an employee hierarchy. All people in a
# company are employees, yet some are managers and so, in a sense, contain collections of other
# employees.
# Problem Statement
# For the following office hierarchy, provide concrete implementations of Manager and Employee. Write
# a test program which does two things:
#  Print out an ASCII employee tree (any format you want).
#  Print out the total salary requirements for the entire company.
# Extra Credit: Sort employees alphabetically (hint: there is an easy way to do this)
#
# Mega Extra Credit: Build unit tests for the code
#
# Super-Mega Extra Credit: Create the hierarchy by reading in from a properties file or json/yaml file