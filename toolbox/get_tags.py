with open('common\country_tags\hrs_countries.txt', 'r') as input_file, open('tag_list.txt', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        if not line.startswith('#'):
            output_file.write(line[:3] + '\n')