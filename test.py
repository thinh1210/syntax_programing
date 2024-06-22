# lop=input('Enter a college class: ')
# emotion=input('Enter an adjective: ')
# sport= input('Enter an activity: ')

# print('{},{}, {}'.format(lop,emotion,sport ))

arr_int= []
for i in range(1, 11):
    num=int(input('Enter the {} number: '.format(str(i))))
    while(num>100):
        print('The pointer is higher than 100')
        num=int(input('Enter the {} number again: '.format(str(i))))
    arr_int.append(num)
new_arr=sorted(arr_int)
print('The lowest: {}'.format(str(new_arr[0])))
print('The highest: {}'.format(str(new_arr[-1])))
print('The second largest scores: {}'.format(str(new_arr[-2])))
new_arr.remove(new_arr[0])
new_arr.remove(new_arr[0])
average= sum(new_arr)/len(new_arr)
print(average)

    
