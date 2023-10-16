# 1) Сортировка списка Имя/Фамилия
# def list_reorder(ref_list):                           # Создаем функцию для сортировки
#     names = ref_list[0]                               # Получение списка имён
#     surnames = ref_list[1]                            # Получение списка фамилий
#
#     for name, surname in zip(names, surnames):
#         pair = [name, surname]                        # Создание пары имени и фамилии
#         reordered_list.append(pair)                   # Добавление пары в новый список
#     print(reordered_list)                             # Вывод отсортированного списка
#
#
# reordered_list = []                                   # Новый список списков
# ref_list = (["Евгений", "Дмитрий", "Илья"], ["Данильченко", "Чугун", "Корвет"])  # Наш список
# list_reorder(ref_list)                                                           # Присваиваем значения нашего списка для функции

# 2) Сортировка списка по возрастанию с удалением повторяющихся элементов
# num = [1, 4, 3, 2, 6, 7, 4, 8, 10, 11, 24]
# def del_rep(num):                                 # Функция сортировки
#     u_nums = list(set(num))                       # Удаление дубликатов
#     sort_num = sorted(u_nums)                     # Сортировка списка по ↑
#     return sort_num                               # Возвращает данные в функцию
#
# result = del_rep(num)                             # Создаем переменную и присваиваем ей значение (Функции)
# print(result)                                     # Выводим результат

# 3) Нахождение limit из списка
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Наш список
# limit = 50                                        # Добавим переменную
# def lin_max(nums, limit):                         # Пропишем функцию
#     a = 0
#     result =[]
#     for i in range(len(nums)):                    # Добавим перебор
#         if limit < nums[a]:
#             a += 1
#         else:
#             result.append(nums[a])
#             a += 1
#     return result                                 # Вернем результат
#
# resultats = lin_max(nums,limit)                   # Сделаем вывод результата
# final_result = resultats[-2]
# print(final_result)

# 4) Термометр
# temp = int(input("Укажите темпуратуру на улице: "))    # Создали переменную в котору будем узкаывать температуру
# def temp_cat(temp):                                    # Создаем функцию которая просчитывает и возврощает нужный показатель
#     if temp < -20:
#         a = 0
#         return a
#     elif -20 <= temp <= 0:
#         a = 1
#         return a
#     elif 0 <= temp <= 15:
#         a = 2
#         return a
#     elif 15 <= temp <=25:
#         a = 3
#         return a
#     else:
#         a = 4
#         return a
# res = temp_cat(temp)                                    # Создаем новую переменную и присваем новой значение
# if res == 0:                                            # В зависимости от нового значения выводим нужный результат
#     print("На улице холодно!")
# if res == 1:
#     print("На улице прохладно!")
# if res == 2:
#     print("На улице зябко!")
# if res == 3:
#     print("На улице тепло!")
# if res == 4:
#     print("На улице жарко!")

# 5) Номера телефонов
# def format_phones(phones):                                            # Создаем фунцию и прописываем в ней действия
#     formatted_phones = []
#     for phone in phones:
#         cleaned_phone = ''.join(filter(str.isdigit, phone))
#         if len(cleaned_phone) != 11:
#             formatted_phones.append(-1)
#             continue
#         if cleaned_phone[0] not in ['7', '8']:
#             formatted_phones.append(-1)
#             continue
#         formatted_phone = f'+{cleaned_phone[0]} ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:9]}-{cleaned_phone[9:]}'
#         formatted_phones.append(formatted_phone)
#     return formatted_phones
#
# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
# result = format_phones(phones)
# print(result)