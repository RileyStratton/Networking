"""
This is just a helper class, it has functions that don't make sense to have in other places.
It mainly has functions to get user input and validate that input.
"""

class Helper():
    def input_ip():
        pass

    def input_port():
        pass

    def input_yes_no(self, prompt="User input (YES or NO): ", validating=False, error="Please follow the prompt!"):
        user_input = input(prompt)
        while validating:
            try:
                user_input = user_input.lower()
                if user_input == "yes" or user_input == "no":
                    validating = False
                else:
                    print(error)
                    user_input = input(prompt) 
            except:
                print(error)
                user_input = input(prompt)

        
        return user_input.lower()

    def input_integer(self, prompt="User input (integer): ", validating=False, error="Please follow the prompt!", min_number=0, max_number=999):
        user_input = input(prompt)
        while validating:
            try:
                user_input = int(user_input)
                if user_input >= min_number and user_input <= max_number:
                    validating = False
                else:
                    print(error)
                    user_input = input(prompt) 
            except:
                print(error)
                user_input = input(prompt)

        return int(user_input)

    def input_string(self, prompt="User input (integer): "):
        return input(prompt)

    def input_path(self, prompt="User input (file path): ", validating=False, error="Please follow the prompt!", prefix="", suffix="", filter=[".","/","\\"]):
        user_input = input(prompt)
        for bad_character in filter:
            user_input = user_input.replace(bad_character, "")
        path = prefix + user_input + suffix
        
        while validating:
            try:
                open(path)
                validating = False
            except:
                print(error)
                user_input = input(prompt)
                for bad_character in filter:
                    user_input = user_input.replace(bad_character, "")
                path = prefix + user_input + suffix
        
        return path