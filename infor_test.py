from infor_coding import get_hierarchy

# content of test_sample.py
def test_basic():
    hierarchy = "Jeff ($100k salary) is the CEO of a startup. He has 2 reports, Dave ($85k) and Cory($65k). " \
                "Dave has 5 reports: Andy ($65k), Dan ($60k), Jason ($60k), Rick ($56k), and Suzanne ($61k)"
    get_hierarchy(hierarchy)

def test_basic2():
    hierarchy = "Jeff ($100k salary) is the CEO of a startup. He has 2 reports, Dave ($85k) and Cory($65k). " \
                "Dave has 5 reports: Andy ($65k), Dan ($60k), Jason ($60k), Rick ($56k), and Suzanne ($61k)" \
                "June has 10 reports: Bob ($65k), Sally ($60k), Jake ($60k), Rob ($56k), and Sue ($61k)"
    get_hierarchy(hierarchy)

def test_basic_number_fail():
    hierarchy = 344
    try:    get_hierarchy(hierarchy)
    except Exception: ("failed as expected")