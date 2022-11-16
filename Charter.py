def modify(tests):
    for test in tests:
        repeat = test["maxRepeat"]
        string = test["myString"]
        newS = string[0]
        currIndex = 1
        for i in range(1, len(string)):
            if string[i] == string[i-1]: 
                if currIndex < repeat:
                    currIndex += 1
                    newS += string[i]
                else:
                    pass
            else:
                currIndex = 1
                newS += string[i]
        test["myResult"] = newS
            
tests = [
    { "name": "Test 1", "myString": "xxxy", "maxRepeat": 2, "testCompleted": False, "myResult": ""},
    { "name": "Test 2", "myString": "xxyy", "maxRepeat": 1, "testCompleted": False, "myResult": "" },
    { "name": "Test 3", "myString": "xxxxyyyyxx", "maxRepeat": 1, "testCompleted": False, "myResult": "" },
    { "name": "Test 4", "myString": "aaaabbbbccccdddd", "maxRepeat": 1, "testCompleted": False, "myResult": ""},
    { "name": "Test 5", "myString": "aaaabbbbccccdddd", "maxRepeat": 2, "testCompleted": False, "myResult": "" },
    { "name": "Test 6", "myString": "aaaabbbbccccdddd", "maxRepeat": 3, "testCompleted": False, "myResult": "" },
]

modify(tests)
print(tests)