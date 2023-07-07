"""
Lambdas allow us to start talking to python about functions not previously defined in our code and still get output.

"""

demolist = [1, 2, 4, 5]
demolist = list(map(lambda x : x * 2, demolist))
print(demolist)
