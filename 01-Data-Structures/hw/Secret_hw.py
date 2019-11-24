Pizza = {'ground pepper','salt','cheese','dough','sweet basil', 'oregano', 'pepperoni', 'gorlic', 'tomatoes', 'onion'}
Shaverma = {'cabbage','fried chicken','cucumbers', 'sauce', 'lavash', 'tomatoes', 'onion'}
#Объединение множеств (все элементы которые в мн-ве Pizza ИЛИ мн-ве Shaverma)
print(Pizza | Shaverma)
#Пересечение множеств (все элементы которые в мн-ве Pizza И мн-ве Shaverma)
print(Pizza & Shaverma)
#Определение разницы множеств (элемент присутствует в 1 множестве, но отсутвует во 2)
print(Pizza - Shaverma)
print(Shaverma - Pizza)
#Симметричная разница множеств (ислючающее ИЛИ)
print(Pizza ^ Shaverma)


