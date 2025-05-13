import pytest
@pytest.mark.smoke
def test_sample_one():
    print("hai")

def test_sample_two():
    print("Hello")

@pytest.mark.smoke
def test_sample_three():
    print("Welcome")

@pytest.mark.skip(reason="This is always disabled")
def test_sample1():
    a = 10 
    b = 5
    assert a < b

@pytest.mark.smoke
def test_sample2():
    a = 5
    b = 10
    assert a < b

def test_simple_assertion():
    print("2")
    assert 1+1==2

@pytest.mark.smoke
@pytest.mark.regression
def test_comparision_assertion():
    print("1")
    x = 4
    y = 4
    assert x==y

@pytest.mark.xfail(reason="this is unfinished")
def test_Sample_fail():
    a=10
    b=10
    assert a!=b

@pytest.mark.xfail(reason="This sometimes get pass and fail")
def test_pass():
    a="arun"
    b="arun"
    assert a.__eq__(b)

@pytest.mark.parametrize("input_tests,expected",[(1,3),(3,5),(5,7)])
def test_add(input_tests,expected):
    assert input_tests + 2 == expected