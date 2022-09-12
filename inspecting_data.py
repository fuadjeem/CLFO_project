import os
paths = ["d:/project_data/train_1","d:/project_data/train_2","d:/project_data/train_3","d:/project_data/train_4"]

complete_file_names = []
for path in paths:
    complete_file_names += os.listdir(path)

print(len(set(complete_file_names))/len(complete_file_names))

uniques = []
for path in paths:
    filenames = os.listdir(path)
    for filename in filenames:
        if filename not in uniques:
            uniques.append(filename)
        else:
            os.remove(os.path.join(path, filename))
            print()

