def pytest_sessionstart(session):
    print("Starting Test Execution")
def pytest_sessionfinish(session, exitstatus):
    print("Execution Completed")
def pytest_runtest_setup(item):
    print("Before Test")
def pytest_runtest_teardown(item):
    print("After Test")
def test_login():
    print("Executing Login Test")