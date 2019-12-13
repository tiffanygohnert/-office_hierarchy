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
            #if the employee is also a manager
            if a in managers:
                print_hierarch(managers[x+1:],employee_list[x+1:],tab)
            else: print("\t"*tab.tabs +"{}".format(a))
        managers.remove(i)

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
    ceo = re.findall(r".* \(\$\d+k salary\) is the CEO", hier_input)
    managers_report = re.findall(r"[A-Z][a-z][a-z]+ has \d+", hier_input)
    managers = re.findall(r"[A-Z][a-z]+",str(ceo)) + re.findall("[A-Z][a-z]+", str(managers_report))
    employee_list = re.findall(r"[A-Z][a-z]+\s{0,1}\(\$\d+k\)",hier_input)
    reports = re.findall(r"\d+ reports", hier_input)

    #Lets make everything pretty now
    get_salarys = re.findall(r"\d+", str(employee_list))
    employee_list = re.findall(r"[A-Z][a-z]+",str(employee_list))
    reports = re.findall(r"\d+", str(reports))

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
    pass
