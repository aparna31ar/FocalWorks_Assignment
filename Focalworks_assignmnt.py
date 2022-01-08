#!/usr/bin/env python
# coding: utf-8

# In[32]:


def get_sum(lists):
    sum = 0
    for i in lists:
        if i.isdigit():
            sum = sum + 4
        elif len(i) > 7:
            sum = sum + 3
        elif len(i) > 5 and len(i) < 7:
            sum = sum + 1
    return sum

correct_ans = input("Enter your input1:") 
user_ans = input("Enter your answer:")  

print("The original string is: ", correct_ans)

List_correct_ans1 = user_ans.split()
List_correct_ans2= correct_ans.split()


user_sum = get_sum(List_correct_ans1)
correct_sum = get_sum(List_correct_ans2)

print("user score", user_sum)
print("correct score", correct_sum)
print("Point scored is", (user_sum/correct_sum)*100)


    


        



# In[ ]:




