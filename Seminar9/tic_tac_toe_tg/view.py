import model
def get_field(table:list):
    field_str = '-' * 17 + '\n'    
    for i in range(9):
        if table[i] == ' ':
            field_str += f'| {i+1} '
        else:
            field_str += f'| {table[i]} '
        if (i + 1) % 3 == 0:
            field_str += '|' + '\n'
            field_str += '-' * 17 + '\n'
    return field_str
