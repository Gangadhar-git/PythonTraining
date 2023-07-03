def rotate_list(lst):
    rotated_list = lst[1:] + lst[:1]
    rotated_list_2=lst[2:]+lst[:2]
    rotated_list_3=lst[3:]+lst[:3]

    return rotated_list , rotated_list_2, rotated_list_3

input_list = list(map(int,input().strip().split()))
print(input_list)
rotated_list = rotate_list(input_list)
print(rotated_list)
