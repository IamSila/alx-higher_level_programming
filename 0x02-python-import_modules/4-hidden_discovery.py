#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden_file
    list_of_names = dir(hidden_file)
    for x in range(len(list_of_names)):
        if (list_of_names[x][0]) != '_':
            print(list_of_names[x])
