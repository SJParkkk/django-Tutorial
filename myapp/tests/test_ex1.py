import pytest

# function  Run once per tests
# class     Run once per class of tests
# module    Run Once per module
# session   Run Once Per session



@pytest.fixture(scope="module")
def fixture_1():
    print('run-fixture-1')
    return 1


def test_example(fixture_1):
    print('run_example_1')
    num = fixture_1
    assert 1 == num

def test_example2(fixture_1):
    print('run_example_2')
    num = fixture_1
    assert 1 == num
