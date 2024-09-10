def funcion1(var1):
    var1 = var1 + [1]
    print(var1)
    return var1

if __name__ == '__main__':
    var1 = [1]
    print(var1)
    var1 = funcion1(var1)
    print(var1)
