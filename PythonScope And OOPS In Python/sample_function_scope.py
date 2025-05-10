
# Here the test value after execute value will be default.
# Because inside function values are local. So they are "local scope".
def check_scope() :
    def do_local() :
        test = "local test" # This test value only can access inside this function only. Because it is local.
    # Here we use a keyword. So the value of test will be changed to given value of test inside do_non_local function.
    def do_non_local() :
        nonlocal test # Because of using "nonlocal" keyword test value will be non local_test.
        test = "non local test"
    # If we want to get the "test" value of "global test". It can access outside of the main function. After using global keyword
    def do_global() :
        global test # If we use "global" keyword we can only access the value of test only outside of the main function.
        test = "global test"

    test = "default" # "nonlocal" will take this test. So here the value will change to "non local_test".
                     # Because we give the test value "non local_test" inside "do_global" function.
    do_local()
    # Here mentioned test value can only access if the test value execute inside that "do_local" function itself.
    # Otherwise it does take the value of test "default" value.
    print("test value after do local: " + test)
    do_non_local()
    # Here mentioned "test" value is actually the "default" value.
    # Because we use a keyword (nonlocal) inside the do_non_local function.
    # So the value "default" will change to "non local_test" value.
    print("test value after do non local: " + test)
    do_global()
    # Here mentioned test value will actually taking the value of just above test value.
    # Which is non local_test.
    # If we want to access the global test value.
    # We should take the value of global test outside of the main function.
    # Because it can take only global value.
    print("test value after do global: " + test)


check_scope()
print("test value after main: " + test) # "global" take this test value.
