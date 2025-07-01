def fence(func):
    def wrapper():
        print("+" * 10)
        func()
        print("+" * 10)

    return wrapper

@fence
def log():
    print("decorated")

log()
