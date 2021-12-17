import csv
import re
from main import creater_decor, PATH


@creater_decor(PATH)
def comb():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    res_list = []
    for item in contacts_list:
        temp_list = []
        if len(item[0]) != 0 and len(item[1]) != 0 and len(item[2]) != 0:
            temp_list.append(item[0])
            temp_list.append(item[1])
            temp_list.append(item[2])
        else:
            if len(item[0]) != 0:
                lastname = re.split(' ', item[0])
                for i in lastname:
                    temp_list.append(i)
            if len(item[1]) != 0:
                firstname = re.split(' ', item[1])
                for i in firstname:
                    temp_list.append(i)
        if len(temp_list) == 2:
            temp_list.append('')
        temp_list.append(item[3])
        temp_list.append(item[4])

        if "доб" in item[5]:
            phone = re.sub(r"(^(\+7|8)\s*\(?)(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d+)(\s?\(?[а-я]+\.?\s?)(\d+)\)?", "+7(\\3)\\4-\\5-\\6 доб.\\8", item[5])
        else:
            phone = re.sub(r"(^(\+7|8)\s*\(?)(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d+)", "+7(\\3)\\4-\\5-\\6", item[5])

        temp_list.append(phone)
        temp_list.append(item[6])

        flag_names = True
        if len(res_list) != 0:
            for it in res_list:
                if temp_list[0] == it[0] and temp_list[1] == it[1]:
                    for k in range(2, 7):
                        if len(it[k]) == 0:
                            it[k] = temp_list[k]
                    flag_names = False
                    break
        else:
            res_list.append(temp_list)
            flag_names = False
        if flag_names:
            res_list.append(temp_list)

    with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(res_list)


if __name__ == "__main__":
    comb()
