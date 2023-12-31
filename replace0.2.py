common_list_example = [
    ["the", ["the", "that", "those"]],
    ["be", ["exist", "live", "remain"]],
    ["to", ["toward", "into", "onto"]],
    ["of", ["belonging to", "concerning", "regarding"]],
    ["and", ["also", "furthermore", "moreover"]],
    ["a", ["an", "one", "any"]],
    ["in", ["inside", "within", "indoors"]],
    ["that", ["which", "who", "whom"]],
    ["have", ["possess", "own", "hold"]],
    ["I", ["me", "myself", "personally"]],
    ["it", ["this", "that", "which"]],
    ["for", ["on behalf of", "in favor of", "to support"]],
    ["not", ["no", "never", "neither"]],
    ["on", ["upon", "atop", "onto"]]
]

data_list_example = [
"me me me",
"I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! When I have a house of my own, I shall be miserable if I have not an excellent library.",
"There is a stubbornness about me that never can bear to be frightened at the will of others. My courage always rises at every attempt to intimidate me.",
"I am determined that only the deepest love will induce me into matrimony.",
"Vanity and pride are different things, though the words are often used synonymously. A person may be proud without being vain. Pride relates more to our opinion of ourselves, vanity to what we would have others think of us.",
"I must learn to be content with being happier than I deserve."]

def replace(data_list, common_list):
    output_data = []
    for i in common_list:
        for j in i[1]:
            for k in data_list:
                if j in k:
                    k = k.replace(j, i[0])
                    output_data.append(k)
    return output_data

for x in (replace(data_list_example, common_list_example)):
    print(x)