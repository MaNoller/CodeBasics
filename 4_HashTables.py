weather = []
with open("nyc_weather.csv","r") as f:
    f_header= next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])
        weather.append([day,temp])
#print(weather)

'''
or:


arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")


'''

##What was the average temperature in first week of Jan?

av_temp=0
for i in range(0,7):
    av_temp+=weather[i][1]
    print(weather[i][1])
av_temp/=7
print(av_temp)

'''
sum(arr[0:7])/len(arr[0:7])
'''



##What was the maximum temperature in first 10 days of Jan?
max_temp=0
tempfinder = lambda x: weather[x][1] if max_temp < weather[x][1] else max_temp
for i in range(0,10):
    max_temp=tempfinder(i)
print(max_temp)

'''
or:
max(arr[0:10])
'''


#PART 2
print('PART 2:')
#What was the temperature on Jan 9?

weather = {}
with open("nyc_weather.csv","r") as f:
    f_header= next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])
        weather[day]=temp
print(weather)

print(weather['Jan 9'])

#What was the temperature on Jan 4?
print(weather['Jan 4'])


#PART 3
'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in 
python and print every word and its count as show below. Think about the best data structure that you 
can use to solve this problem and figure out why you selected that specific data structure.
'''

with open("poem.txt","r") as f:
    #lines = f.read().replace('\n',' ')
    lines = f.read().split(' ')

for line in lines:
    lines = line.replace('\n', ' ')

    print(line)
