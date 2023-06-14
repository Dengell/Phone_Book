from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    with open('data.csv', 'a', encoding='utf-8') as file:
         file.write(f'{name}|{surname}|{phone}|{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные\n')
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(*data)
    return data


def put_data():
    data = print_data()
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    print(f'Изменить данную запись\n{data[number_journal]}')
    list = data[number_journal].split("|")
    print('Что будем менять??')          
    change_awnswer=int(input("1. Имя\n"      
                                "2. Фамилию\n"                
                                "3. Телефон\n"                
                                "4. Адрес\n"
                                "5. Все\n" )) 
    while change_awnswer < 1 or change_awnswer > 5:
            print('Ты дурак?! Даю тебе последний шанс')
            change_awnswer = int(input("1. Имя\n"      
                                "2. Фамилию\n"                
                                "3. Телефон\n"                
                                "4. Адрес\n"
                                "5. Все\n" )) 

    if change_awnswer == 1:
            list[0] = name_data()
            print('Изменения успешно сохранены!')
    elif change_awnswer == 2:     
            list[1] = surname_data()
            print('Изменения успешно сохранены!')    
    elif change_awnswer == 3:     
            list[2] = phone_data()
            print('Изменения успешно сохранены!') 
    elif change_awnswer == 4:     
            list[3] = address_data()
            print('Изменения успешно сохранены!') 
    elif change_awnswer == 5:     
            list[0] = name_data()
            list[1] = surname_data()
            list[2] = phone_data()
            list[3] = address_data()
            print('Изменения успешно сохранены!')
            
    print(list)
    x = '|'.join(list)
    data = data[:number_journal] + [f'{x}\n'] + \
                      data[number_journal + 1:]
    with open('data.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data))

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data= print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    # Можно добавить проверку, чтобы человек не выходил за пределы записи
    print(f'Удалить данную запись\n{data[number_journal - 1]}')
    data = data [:number_journal] + data [number_journal + 1:]
    with open('data.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Изменения успешно сохранены!')  # Можно вывести конечные данные
