def read_file_line_by_line(filepath):
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()
        return lines


def remove_duplicates_from_dict_list(list_of_dicts):
    seen = set()
    new_l = []
    for d in list_of_dicts:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l
