

# content of file: example-input/ebennet.txt to variable input_file

input_file = open("example-input/ebennet.txt", "r")

input_file = input_file.read()

print(input_file)

# content of file: common.list to variable common_list

common_list = open("wordlists/common.list", "r")

common_list = common_list.read()

# check every word in input_file, for any word that is in common_list in [i][1] ( [i][1] has several values), replace it with [i][0]

def replace(input_file, common_list):
    for i in common_list:
        for j in i[1]:
            if i[1][j] in input_file: #FIXME
            input_file = input_file.replace(i[1][j], i[0])
    return input_file

output_file = replace(input_file, common_list)

print(output_file)