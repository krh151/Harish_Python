"""
Pytest is a Python testing framework used to write and execute test cases
efficiently with simple syntax, powerful assertions, fixtures, and reporting features.”

def add(a, b):
    return a - b

def test_add():
    assert add(2, 3) == -1

1.if the file names like test_*.py, *_test.py pytest will automatically identifies those are test files
and pytest methods like def test_method():...method name starts with test_

2.Assertions - Assertions validate expected vs actual result.

def test_fail():
    assert 2 + 2 == 5

def test_pass():
    assert 2 + 2 == 4

3.Fixtures - Reusable setup and cleanup method used before/after test execution.

import pytest

@pytest.fixture
def setup():
    print("Open Browser")
    yield #Here pytest pauses the fixture and gives control to testcase
    print("Close Browser")

def test_google(setup):
    print("Test Executed")

def test_edge(setup):
    print("Test Executed with edge")

# yield is used to perform setup before test execution and
# cleanup after test execution within the same fixture.

4.contest.py - conftest.py is a special file in Pytest used to store:
common fixtures
hooks
reusable setup code
So multiple test files can use the same code.

5.What is Parameterization?
Running same test multiple times with different data.

import pytest
@pytest.mark.parametrize("a,b,result",[
    (2,3,5),
    (5,5,10),
    (10,1,11)
])
def test_add(a,b,result):
    assert a+b==result

6.What are markers in pytest?
Markers are labels used to categorize and selectively run test cases
Markers are tags used to group and control pytest test execution.


import pytest
@pytest.mark.smoke
def test_login_s():
    print("running smoke tests")

@pytest.mark.smoke
@pytest.mark.regression
def test_login_r():
    print("running Regression tests")

7.skip - Do NOT run this test....Pytest completely ignores that test case.
import pytest
@pytest.mark.skip(reason="Feature not developed")
def test_payment():
    print("Payment Test")

xfail - when We EXPECT the test would fail...test STILL runs
but failure is treated as expected

import pytest
@pytest.mark.xfail
def test_bug():
    assert 1 == 2

8.Run specific method in the file - pytest test_pytest.py::test_login_s

9. -v - Show detailed test execution output.
-s - it will show the printing statements defined in the tests
-k - Run tests matching specific name pattern.

10. Fixture Scope - “How many times a fixture should execute.”
Scope	           Meaning
function	Runs before every test function
class	    Runs once per class
module	    Runs once per file
session	    Runs once for entire pytest execution

import pytest

@pytest.fixture(scope="function")
def setup():
    print("Browser Opened")

def test_login(setup):
    print("Login Test")

def test_logout(setup):
    print("Logout Test")

---------------------------------------------------------------------

import pytest

@pytest.fixture(scope="class")
def setup():
    print("Browser Opened")

class TestDemo:

    def test_one(self, setup):
        print("Test One")

    def test_two(self, setup):
        print("Test Two")

===========================================================================

import pytest
@pytest.fixture(scope="module")
def setup():
    print("Database Connected")

def test_login(setup):
    print("Login Test")

def test_logout(setup):
    print("Logout Test")

=========================================================================

@pytest.fixture(scope="session")
def setup():
    print("Starting Test Environment")

Even if:
100 files
1000 tests

=============================================================================
11. Autouse fixture - Autouse fixture automatically executes for tests
without explicitly mentioning fixture name in test methods.

import pytest

@pytest.fixture(autouse=True)
def setup():
    print("Opening Browser")

def test_login():
    print("Login Test")

def test_logout():
    print("Logout Test")

12.How Pytest helps Selenium framework?
Used for:
test execution
assertions
fixtures
reporting
parallel execution

13. What is pytest.ini? -Configuration file used to customize pytest behavior
pytest.ini is a configuration file in Pytest used to store:

pytest settings
marker registrations
default options
test execution configuration

Where should pytest.ini be placed - In project root directory.

[pytest]
addopts = -v -s

markers =
    smoke: smoke test cases
    regression: regression test cases
    sanity: sanity tests

testpaths = tests

14.How to run tests in parallel? - with pytest-xdist plugin.
Parallel execution means running multiple pytest tests simultaneously using pytest-xdist plugin.

15.Hooks - Hooks are special pytest functions that
execute automatically at different stages of test execution.

Customize pytest behavior during test execution.

Commonly Used Hooks
Hook	Purpose
pytest_sessionstart	Runs before test session starts
pytest_sessionfinish	Runs after all tests complete
pytest_runtest_setup	Before every test
pytest_runtest_teardown	After every test
pytest_collection_modifyitems	Modify collected tests

Where are hooks usually implemented? - conftest.py

15. Request Fixture - The request fixture in Pytest is a built-in fixture used to:
get information about the currently executing test or fixture.

request helps access test details dynamically during execution.
request is automatically injected by pytest, You don't create it manually.

What Can We Access Using request?
Property	            Purpose
request.node.name	Current test name
request.module	    Current module/file
request.cls	        Current class
request.config	    Pytest config
request.param	    Parameterized values

import pytest

@pytest.fixture
def setup(request):

    print("Running:", request.node.name)

def test_login(setup):
    print("Login Test")

def test_logout(setup):
    print("Logout Test")

************************************************************************

import pytest

@pytest.fixture
def setup(request):

    marker = request.node.get_closest_marker("smoke")

    if marker:
        print("Smoke Test Found")


@pytest.mark.smoke
def test_login(setup):
    pass



===================================================================================
"""

import pytest
@pytest.mark.smoke
def test_login_s():
    print("running smoke tests")

@pytest.mark.smoke
@pytest.mark.regression
def test_login_r():
    print("running Regression tests")


@pytest.mark.skip(reason="Feature not developed")
def test_payment():
    print("Payment Test")


@pytest.mark.xfail
def test_bug():
    print("Testing Xfail")
    assert 1 == 2
