def f(word):
    if not word:
        return ""
    result = []
    for i in range(len(word)):
        part = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        result.append(part)

    return "-".join(result)
    
if __name__ == "__main__":
    print(f("water"))
    print(f("a"))
    print(f(""))