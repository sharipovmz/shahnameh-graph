import pandas as pd
from pyvis.network import Network

# 1. Читаем твои данные
# Важно: кодировка utf-8, чтобы таджикские буквы (ӯ, ғ, ҷ) не превратились в кракозябры
try:
    df = pd.read_csv('data_tajik.csv', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка: Не найден файл data_tajik.csv!")
    exit()

# 2. Настраиваем внешний вид графа
# Светлый фон — таблицы и элементы управления выглядят корректно в светлой теме
net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='#111111', select_menu=True, filter_menu=True)

# Настройка физики (чтобы узлы красиво отталкивались друг от друга)
net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=200)

# 3. Проходим по каждой строке таблицы и добавляем в граф
for index, row in df.iterrows():
    # .strip() убирает случайные пробелы, если они есть
    source = row['Source'].strip()
    target = row['Target'].strip()
    relation = row['Relationship'].strip()
    obj_type = row['Type'].strip()
    side = row['Side'].strip()

    # --- ЛОГИКА ЦВЕТОВ ---
    color = '#4a90d9' # Цвет по умолчанию (синий, хорошо читается на белом)
    shape = 'dot'     # Форма по умолчанию (кружок)

    # Если это ЧЕЛОВЕК (Шахс)
    if obj_type == 'Шахс':
        if side == 'Эрон':
            color = '#2e8b57'  # Темно-зеленый (Иран)
        elif side == 'Турон':
            color = '#cc3300'  # Темно-красный (Туран)
        else:
            color = '#888888'  # Серый (Нейтральный)
            
    # Если это ЛОКАЦИЯ (Макон)
    elif obj_type == 'Макон':
        color = '#ffd700'      # Золотой
        shape = 'square'       # Квадрат

    # Если это ПРЕДМЕТ (Ашё)
    elif obj_type == 'Ашё':
        color = '#da70d6'      # Фиолетовый
        shape = 'triangle'     # Треугольник

    # Добавляем узлы
    # title - это всплывающая подсказка при наведении мышкой
    net.add_node(source, label=source, title=f"{source} ({side})", color=color, shape=shape)
    net.add_node(target, label=target, title=target) # Target покрасится сам, когда встретится как Source

    # Добавляем связь (стрелочку)
    net.add_edge(source, target, title=relation, label=relation, color='#aaaaaa')

# 4. Сохраняем результат
output_file = 'tajik_graph.html'
net.show(output_file, notebook=False)

print(f"Готово! Открой файл {output_file} в браузере.")