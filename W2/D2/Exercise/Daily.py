import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = [] if items is None else items  # Исправлено: инициализация items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)  # Общее количество страниц

    def get_visible_items(self):
        start_idx = self.current_idx * self.page_size
        end_idx = start_idx + self.page_size
        return self.items[start_idx:end_idx]

    def go_to_page(self, page_num):
        idx = page_num - 1
        if idx < 0:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.total_pages}")
        if idx >= self.total_pages:  # Устанавливаем на последнюю страницу
            idx = self.total_pages - 1
        self.current_idx = idx

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        visible = self.get_visible_items()
        return "\n".join(str(item) for item in visible)

# Тестируем код
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())  # ['a', 'b', 'c', 'd']
p.next_page()
print(p.get_visible_items())  # ['e', 'f', 'g', 'h']
p.last_page()
print(p.get_visible_items())  # ['y', 'z']
p.go_to_page(10)
print(p.current_idx + 1)  # 7
try:
    p.go_to_page(0)  # Должна быть ошибка
except ValueError as e:
    print(e)