# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def __create_dict(cls, my_list: list):
        count_dict = {}
        for number in my_list:
            if number not in count_dict.keys():
                count_dict[number] = 1
            else:
                count_dict[number] += 1
        return count_dict


    @classmethod
    def greatest_frequency(cls, my_list: list):
        count_dict = cls.__create_dict(my_list)
        
        biggest_value = 0
        biggest_key = ""
        for k,v in count_dict.items():
            if v > biggest_value:
                biggest_value = v
                biggest_key = k

        return biggest_key

    @classmethod
    def doubles(cls, my_list: list):
        count_dict = cls.__create_dict(my_list)

        many_count = 0
        for v in count_dict.values():
            if v > 1:
                many_count += 1
        return many_count

if __name__ =="__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))