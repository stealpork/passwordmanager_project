### О чем программа
---
**KeyStorage** предназначен для хранения логинов и паролей от сайтов и приложений с внедренными фукнциями проверки надежности паролей. Все данные хранятся в БД на __локальном__ компьютере пользователя
### Библиотеки, используемые программой
---
- __PyQt6__ - библиотека для внешнего интерфейса
- __sqlite3__  - бибилиотека для взаимодействия с sqlite3 (т.е. базы данных)
- __re__  - библиотека - инструмент для работы с текстом
- __webbrowser__  - библиотека для взаимодействия с ссылками
- __io__  - библиотека для подключения файлов интерфейса внутрь кода
- __string__  - библиотека для работы со строками
- __random__  - библиотека для рандомизации 
- __sys__ - библиотека для работы с интерпретатором Python
### Небазовые функции программы и код их реализации
---
_код для клик-перехода по ссылке_
```python
    def label_clicked(self, event):
        webbrowser.open(self.url_label.text())
```
_код для проверки надежности паролей(краткая выжимка)_
```python
        def check(self):
            min_length = 10
            cur_pass = self.password.text()
            has_upper = re.search(r'[A-Z]', cur_pass) is not None
            has_lower = re.search(r'[a-z]', cur_pass) is not None
            has_digit = re.search(r'\d', cur_pass) is not None
            has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', cur_pass) is not None
            is_long_enough = len(cur_pass) >= min_length
```
_Генератор паролей_
```python
self.paroli.clear()
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation
        for i in range(int(self.kolvo_spin.value())):
            password = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(special_chars)
            ]
            all_characters = lowercase + uppercase + digits + special_chars
            password += random.choices(all_characters, k=int(self.length_spin.value()) - 4)
            random.shuffle(password)
            self.paroli.insertPlainText(''.join(password) + "\n")
            self.par_g.append(password)
```
### Основные функции программы (без вставок кода)
- Регистрация/вход для пользования одной программой разными пользователями
- Добавление информации на одну ячейку: __название__, __логин__, __пароль__, __ссылка (если есть)__ + __автопроверка надежности пароля__
- редактирование/удаление данных
- сохранение сгенерированных паролей в .txt файл
### Заключение
Код был проверен на баги мной и моими друзьями, вроде полностью рабочий. В итоге функционального кода: +- __600__ строк, строк оформления +- __2000__. 