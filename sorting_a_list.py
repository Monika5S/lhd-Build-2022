list_items=input("enter items in your list : (for eg. abc xyz pqr) \n").strip(" ").split(" ")
print("Sorting List in Alphabetical order !!!")

def insertion_sort(fruits):
   for i in range(1, len(list_items)):
       tmp=list_items[i]
       j=i-1;
       while (j>=0 and list_items[j] > tmp):
           list_items[j+1]=list_items[j];
           j=j-1;
       list_items[j+1]=tmp;
   return fruits

if __name__ == "__main__":
     sorted_list=insertion_sort(list_items)
     print(sorted_list)
