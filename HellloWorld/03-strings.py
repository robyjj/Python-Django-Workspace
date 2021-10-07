str = 'hithis is a string'
print(str[0])  # first index
print(str[-1]) # last index of string
print(str[0:3]) # first 3 char - 0,1,2
print(str[0:]) # full string
print(str[1:]) #prints from first index
print(str[:5]) #start index is default 0

print(str[:]) #start index is default 0 , end index - length of string
            #using this to copy strings
anotherStr = str[:]
print(anotherStr)
print(str[1:-1]) # prints from first index to second last index

#formatted string

msg = f'{str[0:2]} how are you'
print(msg)

#get length
print(f'The length of "{str}" is {len(str)}')

#find in str , this is case sensitive
print(str.find('i'))
print(str.find('it'))
print(str.replace('i','jump'))
print(str)

#in
print('this' in str)
print(str.title()); # capitalizes the first ltter in every word