# Write your solution here
def create_tuple(x: int, y: int, z: int):
    temp_list = [x,y,z]
    temp_list.sort()

    final_list = []
    final_list.append(temp_list[0])
    final_list.append(temp_list[-1])
    final_list.append(x+y+z)
    
    final_tuple = tuple(final_list)
    return final_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))