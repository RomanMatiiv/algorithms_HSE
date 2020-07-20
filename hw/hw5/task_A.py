"""
Задача А
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.

Указание.
После того, как вы создадите словарь всех слов,
вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список,
элементами которого будут
кортежи из двух элементов: частота встречаемости слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
Тогда стандартная сортировка будет сортировать список кортежей,
при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
Это почти то, что требуется в задаче.
"""
from data_structure.hash_table import HashTable

if __name__ == "__main__":
    with open("input.txt") as f:
        inp_str = f.read()

    inp_str = (inp_str.replace("\n", " ")
                      .replace("\t", " ")
                      .strip())

    hash_table = HashTable()
    for world in inp_str.split():
        if hash_table.has(world):
            frec = hash_table.get(world)
            frec += 1
            hash_table.insert(world, frec)
        else:
            hash_table.insert(world, 1)

    all_frec = []
    for ceil in hash_table.table:
        if ceil is not None:
            for node in ceil:
                all_frec.append(node)

    all_frec.sort(reverse=True)
    for node in all_frec:
        print(node.key)


