""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""
import os
import json
import numpy as np
import matplotlib.pyplot as plt


def translate_from_dna_to_rna(dna):
    dict_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    rna = {}
    rna = ""
    for litera in dna:
        new_litera = dict_complement[litera]
        rna += new_litera
    return rna


def count_nucleotides(dna):
    num_of_nucleotides = {}
    nucleotides = {'A':0, 'C':0, 'G':0, 'T':0}
    for nucleotide in nucleotides.keys():
        num_of_nucleotides[nucleotide] = dna.count(nucleotide)
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    dict_rna_to_protein = {
        'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L',\
        'AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T','GCU':'A',\
        'UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P',\
        'ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D',\
        'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R',\
        'AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',\
        'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
    }

    protein = ""
    begin = 0
    end = 3
    while end <= len(rna):
        codon = rna[begin:end]
        begin = end
        end = begin + 3
        amino_acid = dict_rna_to_protein[codon]
        protein += amino_acid
    return protein

def out_file(out_dict, out_filename):
    try:
        with open(out_filename, 'w', encoding='UTF-8') as f:
            json.dump(out_dict, f, ensure_ascii=False)
            print(f"файл {out_filename} создался успешно!")
    except:
        print("Ошибка при записи выходного файла JSON")


# read the file dna.fasta
full_file_name = os.path.join('files','dna.fasta')
fin = open(full_file_name, 'rt')
gene_name = 'unknoun gene'
genes = {}
for line in fin:
    if line[0] == '>':
        gene_name = line[1:-1]
        genes[gene_name] = ''
    else:
        genes[gene_name] += line
fin.close()
count_nucl = {}
rna = {}
proteins = {}
for name,gene in genes.items():
    gene = gene.replace('\n','')
    count_nucl[name] = count_nucleotides(gene)
    rna[name] = translate_from_dna_to_rna(gene)
    proteins[name] = translate_rna_to_protein(rna[name])
# Записываем объект Python в файл в виде JSON
out_filename = os.path.join('files','count_nucleotides.json')
out_file(count_nucl,out_filename)

#rna = translate_from_dna_to_rna(dna)
out_filename = os.path.join('files','rna.json')
out_file(rna,out_filename)

#proteins = translate_rna_to_protein(rna)
out_filename = os.path.join('files','proteins.json')
out_file(proteins,out_filename)

for name,gene in genes.items():
#    print(list(count_nucl[name].values()))
    g = np.array(list(gene))
    fig, ax = plt.subplots()

    ax.set_title = "статистики по входящим в последовательность ДНК нуклеотидам"
    ax.set_xlabel = 'нуклеотиды'
    ax.hist(g, label='статистики по нуклеотидам')
    ax.legend(loc='best')
    ax.set_title = "статистики по входящим в последовательность ДНК нуклеотидам"
    ax.set_xlabel = 'нуклеотиды'

    plt.show()
