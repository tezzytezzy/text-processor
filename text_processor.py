def read_data(input_file):
    with open (input_file, 'rt', encoding="ISO-8859-1") as myfile:
        start_idx_pos_list = []
        first_line = True
        second_line = False

        for a_line in myfile:
            if first_line and (not second_line):
                text_string = a_line
                first_line = False
                second_line = True
            elif (not first_line) and second_line:
                question_num_and_length_of_text = a_line.split()
                length_of_text = int(question_num_and_length_of_text[1])
                second_line = False
            else: # Neither first nor second line
                start_idx_pos_list.append(int(a_line) - 1)

    get_substrings(text_string, length_of_text, start_idx_pos_list)

def get_substrings(text_string, length_of_text, start_idx_pos_list):
    for question in range(len(start_idx_pos_list)):
        string_to_examine = text_string[start_idx_pos_list[question]: start_idx_pos_list[question] + length_of_text]

        substring_combos = []

        # Exmaine all the combos from one-letter long to 'length_of_text'-letter long in 'string_to_examine'
        for idx in range(len(string_to_examine)):

            # Determine how many times to go over 'string_to_examine' give 'idx' length
            # Ex. 1 'cat'
            # substring length:                    1 2 3
            # string combo(ex. duplicate removal): 3 2 1
            #
            # Ex. 2 'tetsuya'
            # substring length:                    1 2 3 4 5 6 7
            # string combo(ex. duplicate removal): 7 6 5 4 3 2 1
            #
            # From the above, # of 'string combo' before removing duplicates = 
            #  (1 + len(string_to_examine)) - 'substring length'
            for idx2 in range((1 + len(string_to_examine)) - (idx + 1)):
                substring_combos.append(string_to_examine[idx2: idx2 + idx + 1])

            # The following two lines removes duplicates List -> set -> List
            substring_combos_set = set(substring_combos)

        print(len(substring_combos_set))

read_data("sample.in")