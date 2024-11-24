def diamond(size):
    final=1
    for i in range(size):
        rows=(i*2)-1
        total=(rows*2)+2
        final=final+total
    return ("Amount: " +str(final))
user=int(input("size: "))
print(diamond(user))