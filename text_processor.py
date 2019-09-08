###
#
###
read_data("sample.in")

def read_data(input_file):
    with open (input_file, 'rt', encoding="ISO-8859-1") as myfile:
        first_line = True

        for a_line in myfile:
            if first_line :
                text_string = a_line.split()
                first_line = False
            else:
                question_num_and_length_of_text = a_line.split()

        for num in range(question_num_and_length_of_text[0]):
            




    count_pita_pizza_combo(month_profit, pita_profit, pizza_profit)