from uuid import uuid4
import time

start_val = time.time()
length = 10000
lst = [uuid4().hex for i in range(length)]
end_val = time.time()
time_lst = end_val - start_val

print(time_lst)


start_val_dict = time.time()
length_dict = 100000
dict = {uuid4().hex for el in range(length_dict)}
end_val_dict = time.time()
time_dict = end_val_dict - start_val_dict

print(time_dict)






