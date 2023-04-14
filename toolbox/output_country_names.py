template = """{0}_regional_unifier_communism:0 ""
{0}_regional_unifier_communism_DEF:0 ""
{0}_regional_unifier_anarchism:0 ""
{0}_regional_unifier_anarchism_DEF:0 ""
{0}_regional_unifier_socialism:0 ""
{0}_regional_unifier_socialism_DEF:0 ""
{0}_regional_unifier_democratic:0 ""
{0}_regional_unifier_democratic_DEF:0 ""
{0}_regional_unifier_neutrality:0 ""
{0}_regional_unifier_neutrality_DEF:0 ""
{0}_regional_unifier_monarchism:0 ""
{0}_regional_unifier_monarchism_DEF:0 ""
{0}_regional_unifier_fascism:0 ""
{0}_regional_unifier_fascism_DEF:0 ""
{0}_regional_unifier_imperialism:0 ""
{0}_regional_unifier_imperialism_DEF:0 ""
{0}_regional_unifier_futurism:0 ""
{0}_regional_unifier_futurism_DEF:0 ""
{0}_regional_unifier_communism_ADJ:0 ""
{0}_regional_unifier_anarchism_ADJ:0 ""
{0}_regional_unifier_socialism_ADJ:0 ""
{0}_regional_unifier_democratic_ADJ:0 ""
{0}_regional_unifier_neutrality_ADJ:0 ""
{0}_regional_unifier_monarchism_ADJ:0 ""
{0}_regional_unifier_fascism_ADJ:0 ""
{0}_regional_unifier_imperialism_ADJ:0 ""
{0}_regional_unifier_futurism_ADJ:0 """""

with open('common\country_tags\hrs_countries.txt', 'r') as input_file, open('country_names.txt', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        if not line.startswith('#'):
            output_file.write(template.format(line[:3]) + '\n')