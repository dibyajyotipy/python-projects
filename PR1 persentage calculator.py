def persent(markobt,totmark,c=100):
    sum = (markobt/totmark)*c
    return sum

    
markobt = int(input("Enter your obtain mark: "))
totmark = int(input("Enter total mark: "))


result = persent(markobt,totmark)
print(result,"%")