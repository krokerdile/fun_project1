#!/usr/bash/python

first_list=raw_input("Please enter the first list:")
second_list=raw_input("please enter the second list:")
first_list = first_list[1:len(first_list)-1]
second_list=second_list[1:len(second_list)-1]
first_list=first_list.split(',')
second_list=second_list.split(',')
union=[]
intersection=[]
count=0

union = list(first_list+second_list)

for i in first_list:
        for j in second_list:
                if int(i)==int(j):
                       	intersection.append(int(j))
       
union=list(set(union))
intersection=list(set(intersection))
union.sort()
intersection.sort()
print "intersection: ",intersection
print "union: ",union
