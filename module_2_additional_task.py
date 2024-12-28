num1 = int(input("Введите номер ключа (от 3 до 20): "))
result = 0


# проверяем простое число или имеет делители
def num_is_prime(num1):
    is_prime = True
    for i in range(2, num1 - 1):
        if num1 == 2 or num1 == 3:
            is_prime = True
            break
        elif num1 % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    return is_prime


# ищем слагаемые и возвращаем результат списком
def search_list_with_terms(num1):
    numbers = []
    for i in range(1, num1):
        if i in numbers:
            continue
        elif i * 2 == num1:
            break
        else:
            numbers.append(i)
            numbers.append(num1 - i)
    return numbers


list_with_terms = search_list_with_terms(num1)


# конвертирования список элементов в одно целое число в как результат задачи
def result_as_int_from_list(list_with_terms):
    result = ""
    temporary_list = []
    for i in list_with_terms:
        temporary_list.append(str(i))
    for i in temporary_list:
        result += i
    return int(result)


# если число непростое ищем делители и создаем матрицу со всеми элементами
def search_for_devisors_and_create_matrix(num1):
    divs = []
    for i in range(3, num1):
        if num1 % i == 0:
            divs.append(i)
    matrix = []
    for i in divs:
        matrix.append(search_list_with_terms(i))
    matrix.append(search_list_with_terms(num1))
    return matrix


matrix = search_for_devisors_and_create_matrix(num1)


# конвретируем матрицу в новый список с элементами
def convert_from_matrix_to_new_list(matrix):
    new_list = []
    for i in matrix:
        for j in i:
            new_list.append(j)
    return new_list


new_list = convert_from_matrix_to_new_list(matrix)


# разбиваем список на пары элементов и создаем неизменямый кортеж и сортируем по возрастанию
def split_into_pairs(new_list):
    list_of_pairs = []
    list_of_odd_indexes = []
    list_of_even_indexes = []
    new_list.reverse()
    for i in range(len(new_list)):
        if i % 2 == 0:
            list_of_even_indexes.append(new_list[i])
        else:
            list_of_odd_indexes.append(new_list[i])
    list_of_pairs = list(zip(list_of_odd_indexes, list_of_even_indexes))
    list_of_pairs.sort()
    return list_of_pairs


list_of_pairs = split_into_pairs(new_list)


# преобразовываем кортеж в список
def transformation_to_list(list_of_pairs):
    transformated_list = []
    for i in list_of_pairs:
        for j in i:
            transformated_list.append(str(j))
    return transformated_list


transformated_list = transformation_to_list(list_of_pairs)


if num1 < 5:
    search_list_with_terms(num1)
    result = result_as_int_from_list(list_with_terms)
    print(f"Для заданного ключа '{num1}' подходит этот пароль: '{result}'")
elif num_is_prime(num1):
    search_list_with_terms(num1)
    result = result_as_int_from_list(list_with_terms)
    print(f"Для заданного ключа '{num1}' подходит этот пароль: '{result}'")
else:
    search_list_with_terms(num1)
    matrix = search_for_devisors_and_create_matrix(num1)
    new_list = convert_from_matrix_to_new_list(matrix)
    list_of_pairs = split_into_pairs(new_list)
    transformated_list = transformation_to_list(list_of_pairs)
    result = result_as_int_from_list(transformated_list)
    print(f"Для заданного ключа '{num1}' подходит этот пароль: '{result}'")
