###
#
###

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
    for q in range(len(start_idx_pos_list)):
        string_to_examine = text_string[start_idx_pos_list[q]: start_idx_pos_list[q] + length_of_text].split()

        letters = {}

        # Exmaine all the combos of one-letter long to 'length_of_text'-letter long in 'string_to_examine'
        for string_length in range(length_of_text):




        for letter in range(len(string_to_examine)):
            pass
    print ('x')
read_data("sample.in")