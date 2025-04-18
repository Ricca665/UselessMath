import UselessMath
import sys

def test():
    if UselessMath.Add(2, 2) != 4:
        sys.exit(1)
    else:
        print("Add function test passed!")

test()