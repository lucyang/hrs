with open('tag_list.txt', 'r') as f:
    lines = f.readlines()
    with open('output.txt', 'w') as out:
        for line in lines:
            line = line.strip()
            output = f"""text = {
    trigger = { 
        original_tag = {line}
    }}
    set_cosmetic_tag = {line}_regional_unifier
}}"""
            out.write(output + '\n')