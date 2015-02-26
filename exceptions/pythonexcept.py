class MyError(IndexError):
    def __init__(self, value):
        self.value = value

def oops():
    #raise IndexError('index exception')
    raise MyError("Self defined exception")

try:
    oops()
except MyError as e:
    print("Index error raised in except clause\n" + e.value)
