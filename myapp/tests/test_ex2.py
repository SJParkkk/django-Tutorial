import pytest

@pytest.fixture
def yield_fixture():
    print('start Test Phrase')
    yield 6
    print('end Test Phrase')


def test_example(yield_fixture):
    print('run_test')
    assert yield_fixture == 6