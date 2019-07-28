

def getType(age):
    if age < 18:
        return '未成年人'
    elif 60 > age > 18:
        return '成年人'
    else:
        return '老年人'


print(getType(20))


if __name__ == '__main__':
    print(getType(20))
    print(getType(70))
