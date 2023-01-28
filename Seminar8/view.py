def show_message(msg:str):
    print(msg)

def get_user_input(prompt:str):
    return input(prompt)

def show_entry(entry:tuple):
    print(*entry)

def show_menu(menu:list):
    for num, item in enumerate(menu):
        show_message(f'{num + 1} - {item}')