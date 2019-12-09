import os
import json
import random
from collections import namedtuple
import timeit

MODE = 'set_and_namedtuple' #'simple'

FILE_NAME1 = "winedata_1.json"
FILE_NAME2 = "winedata_2.json"


#преобразуем словарь в NamedTuple
def from_dict_to_namedtuple(dict_):
     return namedtuple('Wine',dict_.keys())(**dict_)

def from_namedtuple_to_dict(wine):
    d = wine._asdict()
    dict_ = dict(d)
    return dict_

def out_file(out_dict, out_filename):
    try:
        with open(out_filename, 'w', encoding='UTF-16') as f:
            json.dump(out_dict, f, ensure_ascii=False)
            print(f"файл {out_filename} создался успешно!")
    except:
        print("Ошибка при записи выходного файла JSON")

def main():
    if os.path.exists(FILE_NAME1):
        # Читаем JSON из файла и преобразуем к типу Python
        with open(FILE_NAME1, 'r', encoding='UTF-8') as f:
            read_data_1 = json.load(f)
    else:
        print(f"{FILE_NAME1} File not found!")
    if os.path.exists(FILE_NAME2):
        # Читаем JSON из файла и преобразуем к типу Python
        with open(FILE_NAME2, 'r', encoding='UTF-8') as f:
            read_data_2 = json.load(f)
    else:
        print(f"{FILE_NAME2} File not found!")

    if MODE == 'set_and_namedtuple':
#--убираем дубликаты моим методом
        dict_wines = read_data_1 + read_data_2
        wines = []
        wines = [from_dict_to_namedtuple(dict_wine) for dict_wine in dict_wines]

    #уничтожение дубликатов
        wines = list(set(wines))
        wines = [from_namedtuple_to_dict(wine) for wine in wines]
    else:
#--убираем дубликаты методом вложенных циклов
#        read_data_1_new = []
#        for dict_wine2 in read_data_1:
#            for dict_wine1 in read_data_1:
#                if dict_wine1 == dict_wine2:
#                   break
#            else:
#                read_data_1_new.append(dict_wine2)

        read_data_2_new = []
        for dict_wine2 in read_data_2:
            for dict_wine1 in read_data_2:
                if dict_wine1 == dict_wine2:
                   break
            else:
                read_data_2_new.append(dict_wine2)

        read_data_1_new = read_data_1
        for dict_wine2 in read_data_2_new:
            for dict_wine1 in read_data_1_new:
                if dict_wine1 == dict_wine2:
                   break
            else:
                read_data_1.append(dict_wine2)
        wines = read_data_1 # [from_dict_to_namedtuple(dict_wine) for dict_wine in read_data_1]

    print("дляна результирующего списка без дублей", len(wines))
    #сортировка # по цене в нисходящем порядке по убыванию (или по сорту в лексикографическом порядке)
    #мы преобразуем 2 числа (индекс и цену) в 1 число
    #
    w = len(wines) * 10 #вычисляем вес
    # (вес надо взять для цены побольше чтобы он дал наибольший вклад и перекрыл значение индекса)
    Index_table_price = []
    for n, value in enumerate(wines, 0):
        try:
            if value['price']:
                price = int(value['price'])
            else:
                price = 0
        except:
            print("TypeError: incorrect format of price!")

        index_price = n + price * w #вычисляем составной индекс
        Index_table_price.append(index_price)
    sorted_wines = []
    #полученную индексную таблицу (аналог индекса в БД) сортируем
    #для этого используем встроенную функцию
    Index_table_price = sorted(Index_table_price, reverse=True)
    prev_price = Index_table_price[0]
    Index_table_title = []
    for index_price in Index_table_price:
        # разлагаем обратно на индекс и цену
        price = index_price // w
        n = index_price % w
    #сделать группировку
    #получаем кучу маленьких списков
        if price != prev_price:
    #сформировали список с одинаковыми ценами
    #теперь сортируем по наименованию в лексикографическом порядке
            Index_table_title = sorted(Index_table_title)
            for index_title in Index_table_title:
                #разлагаем индекс на составные части
                lst = index_title.split('split')
                title = lst[0]
                j = int(lst[1])

                sorted_wines.append(wines[j])
            Index_table_title = []

        # опять строим составной строчный индекс
        index_title = wines[n]['title'] + "split" + str(n)
        Index_table_title.append(index_title)

        prev_price = price


    out_file(sorted_wines, 'winedata_full.json')

    print("-------------------------------------------------------------------------------------------------")
    statistics = {}
    lst_varieties = ['Gewürztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend']
    sort_wine = {}
    for variety in lst_varieties:
        selected_wines = []
        for wine in sorted_wines:
            if variety == wine['variety']:
                selected_wines.append(wine)
        if not selected_wines:
            continue
        prices = []
        score = []
        dict_common_country = {}
        dict_common_region = {}
        for wine in selected_wines:
            if wine['country'] not in dict_common_country:
                dict_common_country[wine['country']] = 0
            if wine['region_1'] not in dict_common_region:
                dict_common_region[wine['region_1']] = 0
            dict_common_country[wine['country']] += 1
            dict_common_region[wine['region_1']] += 1
            prices.append(wine['price'])
            score.append(int(wine['points']))
        average_price = round(sum(prices)/len(prices),1)
        max_price = max(prices)
        min_price = min(prices)
        min_price = min(prices)
        average_score = round(sum(score)/len(score),1)

    #   * `most_common_region` где больше всего вин этого сорта производят ?
    #    most_common_country
    #используем словарь
        max_ = 0
        for country,count_wines in dict_common_country.items():
            if count_wines > max_:
                max_ = count_wines
                most_common_country = country
        max_ = 0
        for region,count_wines in dict_common_region.items():
            if count_wines > max_:
                max_ = count_wines
                most_common_region = region
        variety = variety  #.replace('â','ae').replace('ü','ue')  #вместо немецких вставить общепринятые символы
        sort_wine[variety] = {"average_price":0, "min_price":0, "max_price":0, "most_common_country":0, "most_common_region":0, "average_score":0}
        sort_wine[variety]["average_price"] = str(average_price)
        sort_wine[variety]["min_price"] = str(min_price)
        sort_wine[variety]["max_price"] = str(max_price)
        sort_wine[variety]["most_common_country"] = most_common_country
        sort_wine[variety]["most_common_region"] = most_common_region
        sort_wine[variety]["average_score"] = average_score

    statistics["wine"] = sort_wine

     #   * `most_expensive_wine` в случае коллизий тут и далее делаем список.
     #   * `cheapest_wine`
     #   * `highest_score`
     #   * `lowest_score`
     #   * `most_expensive_coutry` в среднем самое дорогое вино среди стран
     #   * `cheapest_coutry` в среднем самое дешевое вино среди стран
     #   * `most_rated_country`
     #   * `underrated_country`
     #   * `most_active_commentator`

    #в случае коллизий тут и далее делаем список.
    most_expensive_wine = sorted_wines[0]
    cheapest_wine = sorted_wines[-1]
    lst_cheapest_wines = []
    i = len(sorted_wines) - 1
    while i >= 0:
        next_wine = sorted_wines[i]
        if cheapest_wine['price'] == next_wine['price']:
            lst_cheapest_wines.append(next_wine['title'])  #.replace('â','ae').replace('ü','ue'))
        else:
            break
        i -= 1

    statistics["most_expensive_wine"] = most_expensive_wine['title'] #.replace('â','ae').replace('ü','ue') #вместо немецких вставить общепринятые символы
    statistics["cheapest_wine"] = lst_cheapest_wines

        #   * `most_active_commentator`
        #   * `most_expensive_coutry`
    dict_commentator = {}
    dict_country = {}
    for wine in sorted_wines:
        if wine['taster_name'] not in dict_commentator:
            dict_commentator[wine['taster_name']] = 0

        if wine['country'] not in dict_country:
            dict_country[wine['country']] = [0,0,0]

        dict_commentator[wine['taster_name']] += 1
        dict_country[wine['country']][0] += 1
        dict_country[wine['country']][1] += wine['price']
        dict_country[wine['country']][2] += int(wine['points'])

        #   * `highest_score`
    lowest_score = int(sorted_wines[0]['points'])
    highest_score = 0

    for wine in sorted_wines:
        if int(wine['points']) > highest_score:
            highest_score = int(wine['points'])
        if int(wine['points']) < lowest_score:
            lowest_score = int(wine['points'])

    statistics["highest_score"] = highest_score
    statistics["lowest_score"] = lowest_score

        #
    max_ = 0
    min_ = most_expensive_wine['price']
    max_rating = 0
    min_rating = highest_score
    for country, lst in dict_country.items():
        if lst[1]/lst[0] > max_:
            max_ = lst[1]/lst[0]
            most_expensive_coutry = country
        if lst[1]/lst[0] < min_:
            min_ = lst[1]/lst[0]
            cheapest_coutry = country

            #   * `most_rated_country`
            #   * `most_rated_country`
        if lst[2] > max_rating:
            max_rating = lst[2]
            most_rated_country = country
        if lst[2] < min_rating:
            min_rating = lst[2]
            underrated_country = country

    statistics['most_rated_country'] = most_rated_country
    statistics['underrated_country'] = underrated_country
    statistics['most_expensive_coutry'] = most_expensive_coutry
    statistics['cheapest_coutry'] = cheapest_coutry

    #------------------------------------------------------
    max_ = max(dict_commentator.values())
    most_active_commentator = []
    for commentator,count_wines in dict_commentator.items():
        if count_wines == max_ and commentator is not None:
            most_active_commentator.append(commentator)

    statistics["most_active_commentator"] = most_active_commentator
    #-------------------------------------------------------

    out_dict = {}
    out_dict["statistics"] = statistics
    print(out_dict)
    out_file(out_dict, 'stats.json')

    #--красивый MARKDOWN файл---------------
    fout = open('selected_wines_statistics.txt', 'wt', encoding='utf-16')
    for variety, sort_wine in statistics['wine'].items():
        print('variety:', variety, file=fout, sep='\t')
        print('average_price:',sort_wine['average_price'], file=fout, sep='\t')
        print('min_price:',sort_wine['min_price'], file=fout, sep='\t')
        print('max_price:',sort_wine['max_price'], file=fout, sep='\t')
        print('most_common_region:',sort_wine['most_common_region'], file=fout, sep='\t')
        print('most_common_country:', sort_wine['most_common_country'], file=fout, sep='\t')
        print('average_score:',sort_wine['average_score'], file=fout, sep='\t')
        print('------------------------------------------', file=fout)
    fout.close()
    print('файл selected_wines_statistics.txt создался успешно!')

    fout = open('common_statistics.txt', 'wt', encoding='utf-16')
    most_expensive_wine = statistics["most_expensive_wine"]
    print("most_expensive_wine:", most_expensive_wine, file=fout, sep='\t')
    print("cheapest_wine:", statistics["cheapest_wine"], file=fout, sep='\t')
    print("highest_score:", statistics["highest_score"], file=fout, sep='\t')
    print("lowest_score:", statistics["lowest_score"], file=fout, sep='\t')
    print("most_rated_country:", statistics["most_rated_country"], file=fout, sep='\t')
    print("underrated_country:", statistics["underrated_country"], file=fout, sep='\t')
    print("most_expensive_coutry:", statistics["most_expensive_coutry"], file=fout, sep='\t')
    print("cheapest_coutry:", statistics["cheapest_coutry"], file=fout, sep='\t')
    print("most_active_commentator:", statistics["most_active_commentator"], file=fout, sep='\t')
    fout.close()
    print('файл common_statistics.txt создался успешно!')

main()
print('time of execution: ', timeit.timeit("main()", number=3))











