def splitAtNth(string, delimiter, n):
    result = string.split(delimiter, n)[n]
    print(string.split(delimiter, n))
    print(result)
    return string[:-len(result)-len(delimiter)]
