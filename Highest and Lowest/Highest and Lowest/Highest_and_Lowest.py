import nose.tools as Test

def high_and_low(numbers):
    int_numbers=[int(s) for s in numbers.split()]
  
    results=[]
    for fn in (max, min):
        results.append(str(fn(int_numbers)))

    return ' '.join(results)

Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
