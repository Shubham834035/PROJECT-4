# # import numpy as np
# # attendance = np.array([
# #     [1, 1, 1, 0, 1, 1, 1], 
# #     [1, 0, 1, 0, 1, 1, 0],  
# #     [1, 1, 1, 1, 1, 1, 1], 
# #     [0, 1, 0, 1, 1, 0, 1],  
# #     [1, 1, 0, 1, 0, 1, 1]   
# # ])

# # print("attandance record:/n")
# # print(attendance)

# # present_days = np.sum(attendance , axis=1)

# # total_days = np.sum(attendance.shape[1])
# # percentage =(present_days/total_days)*100

# # print("\n attendance report:")
# # for i in range(len(percentage)):
# #     print(f"students{i+1}: {percentage[i]:.2f}%")

# import numpy as np
# attendance = np.array([
#     [1, 1, 1, 0, 1, 1, 1], 
#     [1, 0, 1, 0, 1, 1, 0],  
#     [1, 1, 1, 1, 1, 1, 1], 
#     [0, 1, 0, 1, 1, 0, 1],  
#     [1, 1, 0, 1, 0, 1, 1]   
# ])

# print("attendance record:\n")
# print(attendance)

# present_days = np.sum(attendance,axis =1)

# total_days = np.sum(attendance.shape[1])
# percentage = (present_days/total_days)*100

# print("\n attendance report:")
# for i in range(len(percentage)):
#     print(f"student{i+1}:{percentage[i]:.2f}%")

import numpy as np
attendance = np.array([
    [1, 1, 1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 0],  
    [1, 1, 1, 1, 1, 1, 1], 
    [0, 1, 0, 1, 1, 0, 1],  
    [1, 1, 0, 1, 0, 1, 1]   
])

print("attendance record:\n")
print(attendance)

present_days = np.sum(attendance , axis =1)

total_days = np.sum(attendance.shape[1])
percentage = (present_days/total_days)*100

print("\n attendnacee report:")
for i in range(len(percentage)):
    print(f"student{i+1};{percentage[i]:.2f}%")