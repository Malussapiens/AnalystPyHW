
table = [' ' for _ in range(9)] # Состояние поля

# возвращает состояние игры
def get_table():
    return table

# проверяет свободно ли поле
def is_vacant_position(position):
    return table[position] == ' '

# проверяет корректность позиции
def validate_pos(pos):
    if pos.isdigit():
        pos = int(pos)
        if 1 <= pos <= 9 and is_vacant_position(pos):
            return True
    return False

# записывает в состояние игры токен
def set_table_pos(pos, token:str):
    if validate_pos(pos):
        table[int(pos) - 1] = token
        return True
    return False