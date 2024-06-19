def count_characters(s):
      char_count = {}

      for char in s:
            if char in char_count:
                  char_count[char] += 1
            else:
                  char_count[char] = 1
      return char_count


while True:
      input_word = input("Enter a word so we can count the number of letters in each word (type 'exit' to terminate the program): ")

      if input_word == "exit":
            print("\nGoodbye!")
            break
      else:
            output = count_characters(input_word)
            print(f"Your result: {output}\n")
