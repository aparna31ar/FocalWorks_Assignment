#!/usr/bin/env python
# coding: utf-8

# In[33]:


#Function to calculate score for a candidate's response

def get_sum(lists):
    sum = 0
    for i in lists:
        if i.isdigit():
            sum = sum + 4    # if there is a number in string score is 4 points
        elif len(i) > 7:    
            sum = sum + 3    # if words are having more than 7 characters score is 3 points
        elif len(i) > 5 and len(i) < 7:   # All other words score is 1 point
            sum = sum + 1
    return sum

correct_ans = input("Enter your input1:")  #Taking input from user for the correct answer
user_ans = input("Enter your answer:")     # Taking the response of condidate

print("The original string is: ", correct_ans)   

List_correct_ans1 = user_ans.split()       #Using split function to separate the words in a sentence and storing in a list.
List_correct_ans2= correct_ans.split()


user_sum = get_sum(List_correct_ans1)      # Calling the function to calculate teh score of the correct answer 
correct_sum = get_sum(List_correct_ans2)    # and the response of candidate

print("user score", user_sum)
print("correct score", correct_sum)
print("Point scored is", (user_sum/correct_sum)*100)    # printing the percentage score


    


        



# In[ ]:




