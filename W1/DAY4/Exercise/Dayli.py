MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

matrix = []

for list_1 in MATRIX_STR.splitlines():
    if list_1:
        matrix.append(list(list_1))

column_chars = ""
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        column_chars += matrix[i][j]
decoded_message = ""
for char in column_chars:
    if char.isalpha():
        decoded_message += char
        counts = [0, 0, 0]  # Для трёх столбцов
for col in range(3):
    for row in range(7):
        char = column_chars[col * 7 + row]
        if char.isalpha():
            counts[col] += 1
groups = []
start = 0
for count in counts:
    groups.append(decoded_message[start:start + count])
    start += count

# Соединяем с пробелами
decoded_message = " ".join(groups).strip()
       
print(decoded_message)
