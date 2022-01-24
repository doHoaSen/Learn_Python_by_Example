#!/usr/bin/env python
# coding: utf-8

# In[2]:


#69
country_tuple = ("Korea", "Vietnam", "USA", "Italy", "France")
print(country_tuple)
print()
country = input("please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))


# In[3]:


#70
country_tuple = ("Korea", "Vietnam", "USA", "Italy", "France")
print(country_tuple)
print()
country = input("please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))
print()

num = int(input("Enter a number between 0 and 4: "))
print(country_tuple[num])


# In[5]:


#71
sports = ["baseball", "basketball"]
sport = input("Enter a name of your favorite sport: ")
sports.append(sport)
print(sorted(sports))


# In[7]:


#72
subjects = ["korean", "english", "math", "science", "history", "society"]
print(subjects)

sub_hate = input("Enter a subject you don't like from above: ")
subjects.remove(sub_hate)
print()
print(subjects)


# In[12]:


#73
foodlist_fav = {}
for i in range(4):
    food = input("Enter a name of your favorite food: ")
    foodlist_fav[i+1] = food
print(foodlist_fav)
print()

food_del = int(input("Enter a number of food you want to delete: "))
del foodlist_fav[food_del]
print(sorted(foodlist_fav.values()))


# In[13]:


#74
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'white', 'black']
start_num = int(input("Enter a starting number 0~4: "))
end_num = int(input("Enter a ending number 5-9: "))
print(colors[start_num:end_num])


# In[15]:


#75
numlist = [123, 234, 345, 456]
for num in numlist:
    print(num)
print()

newnum = int(input("Enter a number: "))
if newnum in numlist:
    print(numlist.index(newnum))
else:
    print("That is not in the list")


# In[18]:


#76
invite_list = []
for i in range(3):
    name = input("Enter a name of person you want to invite to the party: ")
    invite_list.append(name)
    
more = input("Do you want to invite more? (y/n): ")
while more != 'n':
    nw_name = input("Enter a another name: ")
    invite_list.append(nw_name)
    more = input("Do you want to invite more? (y/n): ")

print("You invited ", len(invite_list), "people")


# In[21]:


#77
invite_list = []
for i in range(3):
    name = input("Enter a name of person you want to invite to the party: ")
    invite_list.append(name)
    
more = input("Do you want to invite more? (y/n): ")
while more != 'n':
    nw_name = input("Enter a another name: ")
    invite_list.append(nw_name)
    more = input("Do you want to invite more? (y/n): ")

print(invite_list)
nameagain = input("Enter one of the names: ")
print(nameagain, "is in position", invite_list.index(nameagain), "on the list")
stillcome = input("Do you still want them to come? (y/n): ")

if stillcome == 'n':
    invite_list.remove(nameagain)

print(invite_list)


# In[22]:


#78
tvshows = ['RunningMan', 'Infinite Challenge', 'Crime Scene', 'The Genius']
for show in tvshows:
    print(show)
    
anothershow = input("Enter another tv show: ")
indexnum = int(input("Enter a number 0~3: "))
tvshows.insert(indexnum, anothershow)

print(tvshows)


# In[24]:


#79
nums = []
for i in range(3):
    usernum = int(input("Enter a number: "))
    nums.append(usernum)
    print(nums)

saveornot = input("Do you want to save third number? (y/n): ")
if saveornot == 'n':
    nums.pop(-1)
print(nums)


# In[ ]:




