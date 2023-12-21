inputStr = "Nishara"
n = len(inputStr)
result = ''

for i in range(n-1, -1, -1):
    result = result + inputStr[i]

print(result)
