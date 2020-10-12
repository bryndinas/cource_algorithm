from uuid import uuid4
import time

start_val = time.time()
length = 100000
lst = [uuid4().hex for i in range(length)]
end_val = time.time()
time = end_val - start_val
print(start_val)
print(end_val)
print(time)







