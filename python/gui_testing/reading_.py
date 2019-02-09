



while True:
    f = open("./te.txt", 'r')
    lines = f.readlines()
    try:
        print(lines[-1])
    except:
        pass

    f.close()