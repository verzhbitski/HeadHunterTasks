# Задания для школы программистов HeadHunter

## Задание 1: Полином

### Условие
Дано выражение, содержащее скобки, операции сложения, вычитания, умножения, возведения в константную степень и одну переменную. Представьте это выражение в развёрнутом виде.

### Пример входных данных:

    (x - 5)(2x^3 + x(x^2 - 9))

### Пример выходных данных:

    3x^4 - 15x^3 - 9x^2 + 45x

## Задание 2: Количество разбиений на k слагаемых

### Условие
Для данных натуральных чисел n и k определите количество способов представить число n в виде суммы k натуральных слагаемых, если способы, отличающиеся только порядком слагаемых считать одинаковыми.

### Формат входных данных:

    n k

### Формат выходных данных:

    partition_number

## Ввод/вывод данных
В программах предусмотрен ввод даных с клавиатуры или работа с файлами. Для работы с файлами необходимо передать два аргумента командной строки: <input_file> и <output_file>. Пример:

    python <task_name> <input_file> <output_file>
