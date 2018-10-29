
import genome_maker


#method which counts the total veeple population from input: census list
#the length of elements in the list is the number of people added to the census
def veeple_population_count(veeplecensus):
    total_pop = len(veeplecensus)
    return (total_pop)

#method which counts % of male and female veeples from the total census list
#input: census list
def veeple_percent_genders(veeplecensus):
    total_female = 0
    total_male = 0
    total_pop = len(veeplecensus)

    for individual in veeplecensus: #for each dictionary in the veeple census that correspons to a person
        if individual['Sex'] == 'X':
            total_female = total_female + 1
        elif individual['Sex'] == 'Y':
            total_male = total_male + 1
    percent_female = total_female / total_pop
    percent_male = total_male / total_pop
    return(percent_female,percent_male)

#method which counts total alleic frequencies in the census with input census list.
def veeple_allelic_frequencies(veeplecensus):
    allelic_count_dict = {}#initializing the dictionary that has the total counts / census
    total_veeples = len(veeplecensus)
    total_alleles = total_veeples *4 #This is because we set set of alleles to 4 options, and im too lazy to use this in a function.

    for individual in veeplecensus: #for each dictionary in the veeple census that corresponds to a person
        for allele in individual['mGenome']:#cataloging the maternal genome list
            if allele in allelic_count_dict:
                allelic_count_dict[allele] += 1
            else:
                allelic_count_dict[allele] = 1

        for allele in individual['pGenome']: #cataloging the paternal genome list
            if allele in allelic_count_dict:
                allelic_count_dict[allele] +=1
            else:
                allelic_count_dict[allele] = 1
    
    allelic_frequencies_dict = allelic_count_dict.copy()
    for key in allelic_frequencies_dict:
        allelic_frequencies_dict[key] = int(allelic_frequencies_dict[key])/total_alleles

    return(allelic_frequencies_dict)


