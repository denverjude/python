def counter(message):
    count = {}
    message = message.replace(".", " .")
    message = message.replace(",", " ,")
    for i in message.split():
        count.setdefault(i, 0)
        count[i]+=1
    return count
