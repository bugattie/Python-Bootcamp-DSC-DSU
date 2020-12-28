#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os


def main():
    path = str(input('Enter a location: '))
    os.chdir(path)

    ls = os.listdir(path)
    print(ls)

    file_info = []

    for i in range(len(ls)):
        stats = os.stat(ls[i])
        files = [ls[i], stats.st_size]
        file_info.append(files)

    # bubble sort
    for i in range(0, len(file_info)-1):
        for j in range(0, len(file_info)-i-1):
            if file_info[j][1] < file_info[j+1][1]:
                file_info[j], file_info[j+1] = file_info[j+1], file_info[j]

    print(file_info)


if __name__ == "__main__":
    main()


# In[ ]:




