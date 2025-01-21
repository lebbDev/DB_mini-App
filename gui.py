import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, showinfo
from ttkthemes import ThemedTk

from database import *


root = ThemedTk(theme="breeze")
root.title("Панель управления")

# Получаем ширину и высоту экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Приложение появляется по центру экрана
window_width = 400
window_height = 400
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Выбор виджетов в зависимости от таблицы
isInsert = False
isDelete = False
isUpdate = False
isSelectOne = False

def close_widgets():
    if isInsert:
        close_insert_widgets()
    elif isDelete:
        close_delete_widgets()
    elif isUpdate:
        close_update_widgets()
    elif isSelectOne:
        close_one_select_widgets()

def get_widgets(event):
    close_widgets()
    choice = operation_choice_combobox.get()
    if choice == "Insert":
        get_insert_widgets()
    elif choice == "Delete":
        get_delete_widgets()
    elif choice == "Update":
        get_update_widgets()
    elif choice == "Select one":
        get_one_select_widgets()

def get_insert_widgets():
    global isInsert
    isInsert = True
    execute_button.forget()

    example_record.pack(anchor="nw", fill="x", padx=5, pady=5)
    example_record_lab.pack(side="left", anchor="nw")
    user_record.pack(anchor="nw", fill="x", padx=5, pady=5)
    user_record_lab.pack()
    user_record_input.pack(side="left", anchor="nw", expand=True, fill="x")

    execute_button.pack()

def get_delete_widgets():
    global isDelete
    isDelete = True
    execute_button.forget()

    delete_ID.pack(anchor="nw", fill="x", padx=5, pady=5)
    delete_ID_lab.pack()
    delete_ID_input.pack(side="left", anchor="nw", expand=True, fill="x")

    execute_button.pack()

def get_update_widgets():
    global isUpdate
    isUpdate = True
    execute_button.forget()

    column_choice.pack(anchor="nw", fill="x", padx=5, pady=5)
    column_choice_lab.pack(side="left", anchor="nw")
    column_choice_combobox.pack(side="left", anchor="nw", padx=12)
    user_value.pack(anchor="nw", fill="x", padx=5, pady=5)
    user_value_lab.pack()
    user_value_input.pack(side="left", anchor="nw", expand=True, fill="x")
    update_ID.pack(anchor="nw", fill="x", padx=5, pady=5)
    update_ID_lab.pack()
    update_ID_input.pack(side="left", anchor="nw", expand=True, fill="x")

    execute_button.pack()

def get_one_select_widgets():
    global isSelectOne
    isSelectOne = True
    execute_button.forget()

    select_ID.pack(anchor="nw", fill="x", padx=5, pady=5)
    select_ID_lab.pack()
    select_ID_input.pack(side="left", anchor="nw", expand=True, fill="x")

    execute_button.pack()

def close_insert_widgets():
    global isInsert
    isInsert = False

    example_record.forget()
    example_record_lab.forget()
    user_record.forget()
    user_record_lab.forget()
    user_record_input.forget()

def close_delete_widgets():
    global isDelete
    isDelete = False

    delete_ID.forget()
    delete_ID_lab.forget()
    delete_ID_input.forget()

def close_update_widgets():
    global isUpdate
    isUpdate = False

    column_choice.forget()
    column_choice_lab.forget()
    column_choice_combobox.forget()
    user_value.forget()
    user_value_lab.forget()
    user_value_input.forget()
    update_ID.forget()
    update_ID_lab.forget()
    update_ID_input.forget()

def close_one_select_widgets():
    global isSelectOne
    isSelectOne = False

    select_ID.forget()
    select_ID_lab.forget()
    select_ID_input.forget()

# Количество активных строк в виджете Text
line_count = 0

def clear_text_widget():
    global line_count

    if line_count:
        for line in range(line_count):
            output_text.delete(f"{line + 1}.0", tk.END)

        line_count = 0

def send_execute():
    global line_count
    choice = operation_choice_combobox.get()

    try:
        connect = connect_db()

        if choice == "Insert":
            if len(tables[table_choice_combobox.get()]) == 2:
                insert_record(connect[1], table_choice_combobox.get(), list_to_seq(tables[table_choice_combobox.get()][0:]), user_record_input.get())
            else:
                insert_record(connect[1], table_choice_combobox.get(), list_to_seq(tables[table_choice_combobox.get()][1:]), user_record_input.get())
        elif choice == "Delete":
            if len(tables[table_choice_combobox.get()]) == 2:
                id_name_list = list()
                id_name_list.append(tables[table_choice_combobox.get()][0])
                id_name_list.append(tables[table_choice_combobox.get()][1])
                delete_record(connect[1], table_choice_combobox.get(), id_name_list, delete_ID_input.get())
            else:
                delete_record(connect[1], table_choice_combobox.get(), tables[table_choice_combobox.get()][0], delete_ID_input.get())
        elif choice == "Update":
            if len(tables[table_choice_combobox.get()]) == 2:
                id_name_list = list()
                id_name_list.append(tables[table_choice_combobox.get()][0])
                id_name_list.append(tables[table_choice_combobox.get()][1])
                update_record(connect[1], table_choice_combobox.get(), column_choice_combobox.get(), user_value_input.get(), id_name_list, update_ID_input.get())
            else:
                update_record(connect[1], table_choice_combobox.get(), column_choice_combobox.get(), user_value_input.get(), tables[table_choice_combobox.get()][0], update_ID_input.get())
        elif choice == "Select one":
            if len(tables[table_choice_combobox.get()]) == 2:
                id_name_list = list()
                id_name_list.append(tables[table_choice_combobox.get()][0])
                id_name_list.append(tables[table_choice_combobox.get()][1])
                record = get_one_record(connect[1], table_choice_combobox.get(), id_name_list, select_ID_input.get())
            else:
                record = get_one_record(connect[1], table_choice_combobox.get(), tables[table_choice_combobox.get()][0], select_ID_input.get())
            
            clear_text_widget()
            output_text.insert("1.0", str(record))
            line_count = line_count + 1
        elif choice == "Select all":
            all_records = get_all_records(connect[1], table_choice_combobox.get())
            clear_text_widget()
            for record in all_records:
                output_text.insert(tk.END, str(record) + "\n")
                line_count = line_count + 1
        
        # Если нет ошибок
        showinfo(title="Успех", message="Операция успешно выполнена")
    except Exception as ex:
        showerror(title="Ошибка", message=f"Во время работы с БД произошла {ex}")
    finally:
        disconnect_db(connect)

# Виджеты
notebook_switch = ttk.Notebook()
notebook_switch.pack(expand=True, fill="both")
panel_page = ttk.Frame(notebook_switch)
output_page = ttk.Frame(notebook_switch)
panel_page.pack(expand=True, fill="both")
output_page.pack(expand=True, fill="both")
notebook_switch.add(panel_page, text='Панель')
notebook_switch.add(output_page, text='Вывод')

# Окно вывода
output_label = ttk.Label(output_page, text='Записи полученные с помощью операции Select:', font="TkDefaultFont 12")
output_text = tk.Text(output_page, wrap = "none")

output_scroll_y = ttk.Scrollbar(output_text, orient = "vertical", command = output_text.yview)
output_scroll_x = ttk.Scrollbar(output_text, orient = "horizontal", command = output_text.xview)
 
output_text["yscrollcommand"] = output_scroll_y.set
output_text["xscrollcommand"] = output_scroll_x.set

# Окно управления
panel_lab = ttk.Label(panel_page, text='База данных "Рестораны"', font="TkDefaultFont 12")

def init_column_combobox(event):
    if len(tables[table_choice_combobox.get()]) == 2:
        column_choice_combobox["values"] = tables[table_choice_combobox.get()][0:]
    else:
        column_choice_combobox["values"] = tables[table_choice_combobox.get()][1:]

# Выбор таблицы
table_choice = ttk.Frame(panel_page, padding=[8, 4])
table_choice_lab = ttk.Label(table_choice, text="Выберите таблицу:")
table_choice_combobox = ttk.Combobox(table_choice, values=list(tables.keys()), state="readonly")
table_choice_combobox.bind('<<ComboboxSelected>>', init_column_combobox)

# Выбор операции
operation_choice = ttk.Frame(panel_page, padding=[8, 4])
operation_choice_lab = ttk.Label(operation_choice, text="Выберите операцию:")
items = ["Insert", "Delete", "Update", "Select one", "Select all"]
operation_choice_combobox = ttk.Combobox(operation_choice, values=items, state="readonly")
operation_choice_combobox.bind('<<ComboboxSelected>>', get_widgets)

# Пример ввода
example_record = ttk.Frame(panel_page, padding=[8, 4])
example_record_lab = ttk.Label(
    example_record,
    text="Пример ввода записи ресторана (формат данных как в SQL): 'Chicken house', 'Тверь, ул. Трёхсвятская, д. 20', '+7 (4822) 35-61-63', 5.0, '00:00', '00:00'",
    wraplength=380)

# Ввод строки
user_record = ttk.Frame(panel_page, padding=[8, 4])
user_record_lab = ttk.Label(user_record, text="Введите новую запись:")
user_record_input = ttk.Entry(user_record)

# Ввод ID удаления
delete_ID = ttk.Frame(panel_page, padding=[8, 4])
delete_ID_lab = ttk.Label(delete_ID, text="Введите ID записи для удаления (через ',' для двух):")
delete_ID_input = ttk.Entry(delete_ID)

# Выбор колонки
column_combobox_val = list()
column_choice = ttk.Frame(panel_page, padding=[8, 4])
column_choice_lab = ttk.Label(column_choice, text="Выберите столбец:")
column_choice_combobox = ttk.Combobox(column_choice, values=column_combobox_val, state="readonly")

# Ввод нового значения
user_value = ttk.Frame(panel_page, padding=[8, 4])
user_value_lab = ttk.Label(user_value, text="Введите новое значение столбца (формат данных как в SQL):")
user_value_input = ttk.Entry(user_value)

# Ввод ID обновления
update_ID = ttk.Frame(panel_page, padding=[8, 4])
update_ID_lab = ttk.Label(update_ID, text="Введите ID записи для замены (через ',' для двух ID):")
update_ID_input = ttk.Entry(update_ID)

# Ввод ID вывода
select_ID = ttk.Frame(panel_page, padding=[8, 4])
select_ID_lab = ttk.Label(select_ID, text="Введите ID записи для вывода (через ',' для двух ID):")
select_ID_input = ttk.Entry(select_ID)

# Кнопка отправки запроса
execute_button = ttk.Button(panel_page, text="Поехали", command=send_execute)

# Геометрия
panel_lab.pack(pady=10)
table_choice.pack(anchor="nw", fill="x", padx=5, pady=5)
table_choice_lab.pack(side="left", anchor="nw")
table_choice_combobox.pack(side="left", anchor="nw", padx=12)
operation_choice.pack(anchor="nw", fill="x", padx=5, pady=5)
operation_choice_lab.pack(side="left", anchor="nw")
operation_choice_combobox.pack(side="left", anchor="nw")
execute_button.pack()

output_label.pack(pady=10)
output_text.pack(expand=True, fill="both", padx=10, pady=[0, 25])
output_scroll_y.pack(fill="y", side="right", anchor="ne")
output_scroll_x.pack(fill="x", side="bottom", anchor="sw")

# Основной цикл
root.mainloop()