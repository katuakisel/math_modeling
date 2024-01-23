from block_3_task_4 import create_array

arr = create_array(4,4)
# print(len(arr))
for row in arr:
    row[0], row[1] = row[1], row[0]
print(arr)