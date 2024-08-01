# Висновки щодо ефективності алгоритмів

## Жадібний алгоритм:
- Часова складність: O(n).
- Алгоритм швидкий у виконанні.
- Недолік: не завжди знаходить оптимальне рішення, особливо якщо набір монет не підходить для жадібного підходу.

## Алгоритм динамічного програмування:
- Часова складність: O(n * m), де n — сума, а m — кількість різних номіналів монет.
- Забезпечує оптимальне рішення у всіх випадках.
- Недолік: повільніший, ніж жадібний алгоритм, особливо для великих значень суми.

## Порівняння на прикладі:
Для суми 113 обидва алгоритми дають однаковий результат:
- Жадібний алгоритм: {50: 2, 10: 1, 2: 1, 1: 1}
- Динамічне програмування: {50: 2, 10: 1, 2: 1, 1: 1}

Жадібний алгоритм працює добре на наборі монет [50, 25, 10, 5, 2, 1], але для інших наборів монет може не знаходити мінімальну кількість монет.

