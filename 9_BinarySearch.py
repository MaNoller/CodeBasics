When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
  -> Not sorted
numbers = [1,4,6,9,10,5,7]

Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array
Solution:
  def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    indizes=[]

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            indizes.append(mid_index)
            print('INDIZES IS 1:', indizes)
            l_index=mid_index-1
            r_index=mid_index +1
            print('MIDNUMB IS', mid_number)
            print('LINDEX', l_index, numbers[left_index])
            
            while mid_number==numbers_list[l_index] and l_index>=0:
                indizes.append(l_index)
                print('INDIZES IS 2:', indizes)
                l_index-=1
                
            while mid_number==numbers_list[r_index]and r_index<len(numbers_list):
                indizes.append(r_index)
                print('INDIZES IS 3:', indizes)
                r_index+=1
                
            
            
            return sorted(indizes)

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

    index = binary_search(numbers, number_to_find)
    print(f"Number found at index {index} using binary search")
