import sys

def remove_duplicates(array):
    if len(array) == 0:
        print ("Empty array")
        sys.exit()
    list = []
    list.append(array[0])
    for i in range(1, len(array)):
        try:
#			if int(array[i]) < int(array[i-1]):
#				print ('Invalid list: not sorted')
#				sys.exit()
            if array[i] != array[i-1]:
                list.append(array[i])
        except ValueError as err:
            print ('Invalid value :(')
            sys.exit()
    return (list)

def popularity(text):
    words = text.lower().split()
    words.sort()
    words_sorted = sorted(words, key = words.count, reverse = True)
    return remove_duplicates(words_sorted)

# Для виводу унікальних елементів списку використано функцію remove_duplicates з python-hw-3. Бо навіщо писати функції і потім їх не використовувати? :)

popularity('apple kiwi pineapple kiwi apple kiwi') #-> ['kiwi', 'apple', 'pineapple']
popularity('aPPle pine Apple kiwi Apple kiwi') #-> ['apple', 'kiwi', 'pine']
popularity('aPPle pine Apple kiwi Apple kiwi') #-> ['apple', 'kiwi', 'pine']
popularity('aab aaa aac aab aac aaa x') #-> ['aaa', 'aab', 'aac', 'x']
