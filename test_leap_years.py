from main import leap_years


def test_lp_div_by_four_thousands():
    assert leap_years(2000) == True

def test_lp_div_by_one_thousand():
    assert leap_years(1700) == False

def test_lp_div_by_four():
    assert leap_years(2008) == True

def test_lp_not_div_by_four():
    assert leap_years(2017) == False