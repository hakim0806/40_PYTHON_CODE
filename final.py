21.Write a program to Find 2nd large number.
 
def find_largest(n):
    unique_Num = list(set(n))
    if len(unique_Num) < 2:
        return "There is no largest Number"
    unique_Num.sort(reverse=True)
    return unique_Num[1]
 
Num = list(map(int,input("Enter numbers separated by spaces: ").split()))
 
Second_large = find_largest(Num)
print(f"The second largest number is : {Second_large}")
 
 
 
 
 
22-> write a programme to sort a list in ascending/descending order
 
"""
Num = list(map(int,input("Enter numbers separated by spaces: ").split()))
 
Num.sort()
print(f"The ascending ordered number lis is ={Num} ")
 
"""
 
Num = list(map(int,input("Enter numbers separated by spaces: ").split()))
 
Num.sort(reverse=True)
print(f"The descending ordered number lis is ={Num} ")
 
 
 
 
 
23-> write a programme to merge two list
 
Num1 = list(map(int,input("Enter numbers separated by spaces: ").split()))
Num2 = list(map(int,input("Enter numbers separated by spaces: ").split()))
 
merge_list = Num1 + Num2
 
print(f"The merge List is = {merge_list}")
 
 
 
 
 
24->Write a program to total sum of list
 
Num = list(map(int,input("Enter numbers separated by spaces: ").split()))
 
total_sum = sum(Num)
 
print(f"Summation of the List is = {total_sum}")
 
 
 
 
 
25-> write a programme to find common elements two in list
 
Num2 = list(map(int,input("Enter numbers separated by spaces: ").split()))
Num1 = list(map(int,input("Enter numbers separated by spaces: ").split()))
common_Num = list(set(Num1) & set(Num2))
 
print(f"The Common Number of {Num1} & {Num2} is = {common_Num}")
 
 
 
 
 
26-> write a programme to flattened nested list
 
def flatten_nested_list(nested_list):
    flatten_list = []
    for item in nested_list:
        if isinstance(item,list):
            flatten_list.extend(flatten_nested_list(item))
        else:
            flatten_list.append(item)
    return flatten_list
 
nested_list = [7, [2,3],4,[2,[3,4],5],6,[7,8]]
flattened = flatten_nested_list(nested_list)
print("Flattened list : ",flattened)
 
 
 
 
 
27-> write a programme to count thw occurrence of each elements in the list
 
user_list = list(map(int,input("Enter numbers separated by spaces: ").split()))
element_count = {}
for element in user_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1
 
 
for element,count in element_count.items():
 
    print(f"Element {element} occurs {count} times")
 
 
 
 
 
28-> write a programme to remove duplicates num from the list
 
def remove_duplicates(input_list):
    unique_list = []
 
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
 
    return unique_list
 
user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
 
result = remove_duplicates(user_list)
 
 
print("List after removing duplicates : ",result)
 
 
 
 
 
29-> write a programme to check if a list is empty or not.
 
def check_empty_list(my_list):
    if not my_list:
        return ("This List is Empty")
    else:
        return "This list is not Empty"
 
list1 = []
print(check_empty_list(list1))
 
list2 = [1,2,3]
print(check_empty_list(list2))
 
 
 
 
 
30-> write a programme to find the intersection of two list
 
def find_intersection(set1, sset2):
    myIntersection = set1.intersection(set2)
    return myIntersection
 
set1_in = input("Enter numbers of the first set, separated by spaces: ")
set2_in = input("Enter numbers of the second set, separated by spaces: ")
 
set1 = set(map(int,set1_in.split()))
set2 = set(map(int,set2_in.split()))
 
result = find_intersection(set1, set2)
print("Intersection of set1 and set2 : ",result)
 
 
 
 
 
31-Exisit_in_Dictionary
 
My_Dict = { 'name': 'Ayon', 'age': '22'}
key_to_Check = input("enter the key you want to check: ")
 
if key_to_Check in My_Dict:
    print(f"The key '{key_to_Check}' Exists in the dictionary.")
else:
    print(f"The key '{key_to_Check}' does not exists in the dictionary.")
 
 
 
 
 
32-Merge_2_Dictionary
 
dictionary1 = { 'a':1, 'b':2, 'c':3}
dictionary2 = { 'd':4, 'e':2, 'f':6}
 
dictionary1.update(dictionary2)
 
print("Merge Dictionary :",dictionary1)
 
 
 
 
 
33-Remove_a_key_from_dict
 
My_Dict = { 'name': 'Ayon', 'age': '22'}
key_to_remove = input("enter the key you want to check: ")
 
if key_to_remove in My_Dict:
    remove = My_Dict.pop(key_to_remove)
    print(f"The key '{key_to_remove}' remove with value {remove} from the dictionary.")
    print(f"Updated dictionary = {My_Dict}")
else:
    print(f"The key '{key_to_remove}' does not exists in the dictionary.")
 
 
 
 
 
 
34-Sort_a_Dictionary
 
my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 5,
    'elderberry': 4
}
sorted_dictionary = dict(sorted(my_dict.items(),key=lambda item: item[1]))
 
print("Dictionary sorted by values: ",sorted_dictionary)
 
 
 
 
 
35-count_frequency
 
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char!= ' ':
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
 
input_string = input("Enter a string = ")
 
frequency_count = count_character_frequency(input_string)
 
print("Character Frequency:", frequency_count)
 
 
 
 
 
 
36-> Count frequency of character in a string
 
 
def count_frequency(str):
    freq = {}
    for ch in str:
        if ch != ' ':
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq
 
input_string = input("Enter a string : ")
frequency = count_frequency(input_string)
print(f"Frequency of each character : {frequency}")
 
 
 
 
 
 
37-> Count frequency of a list
 
 
def most_frequent_element(lst):
    if not lst:
        return None
    freq = {}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    max_freq = max(freq,key=freq.get)
    return max_freq
 
user_input = list(map(int,input("Enter numbers separated by space : ").split()))
most_freq = most_frequent_element(user_input)
print(f"Most frequent element is {most_freq}")
 
 
 
 
 
38-> Create a lambda function for adding two number
 
 
add_num = lambda x,y : x+y
 
num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
result = add_num(num1,num2)
print(f"Summation of two numbers = {result}")
 
 
 
39-> Map two lists into a dictionary
 
keys = ['Name','Age','City']
values = ['Adnan','22','Chakaria']
new_dict = dict(map(lambda k,v : (k,v), keys,values))
print(new_dict)
 
 
 
40-> Implement a stack using a list
 
 
class Stack:
    def __init__(self):
        self.stack = []
 
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} Pushed to stack")
 
    def pop(self):
        if self.is_empty():
            return "The Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "The Stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)
 
 
 
 
 
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(150)
 
stack1 = Stack()
stack1.push(30)
 
print("Top element of stack1 is:", stack1.peek())
print("Top element is:", stack.peek())
print("Stack size is:", stack.size())
print("Popped element :", stack.pop())
print("Stack is empty:", stack.is_empty())
 
 
 
 
41-> Implement Queue using list
 
class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self,item):
        self.queue.append(item)
        print(f"{item} is pushed to queue")
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]
    def Size(self):
        return len(self.queue)
 
queue1 = Queue()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
print(f"Size of the stack1 is {queue1.Size()}")
queue1.peek()
queue2 = Queue()
print(f"Stack2 is empty? {queue2.is_empty()}")
queue2.enqueue(40)
queue2.peek()