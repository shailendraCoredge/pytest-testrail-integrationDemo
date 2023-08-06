import pytest


@pytest.mark.testrail(19889)
def test_pass_func():
    pass

@pytest.mark.testrail(20933)
def test_fail_func():
    assert 3==5

