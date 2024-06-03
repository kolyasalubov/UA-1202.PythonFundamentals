def return_max_number(first_num, second_num):
      """
      Returns the larger of the two numbers.

      Parameters:
      first_num (float): The first number.
      second_num (float): The second number.
    
      Returns:
      float: The larger of the two numbers.
      """
      if first_num > second_num:
            return first_num
      elif first_num < second_num:
            return second_num
      else:
        return first_num # or second_num, since they are equal
      

print(return_max_number(1.2, 0.9))
