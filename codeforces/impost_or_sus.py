def to_be_suspicious(string):
    counter = 0
    if string[-1] == 'u':
        string = string[:-1] + 's'
        counter += 1
    if string[0] == 'u':
        string = 's' + string[1:]
        counter += 1
    new_str = string.split("s")
    for sub_str in new_str:
        counter += len(sub_str)//2
    print(counter)      
        
    
if __name__ == "__main__":
    n = int(input())
    strings = [
        input().strip() for _ in range(n)
    ]
    for string in strings:
        to_be_suspicious(string)
    
