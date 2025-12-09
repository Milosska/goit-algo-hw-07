# Інструкція щодо використання репозиторію

1. Склонуйте репозиторій

```bash
git clone [repository-url]
cd goit-algo-hw-06
```

2. Перейдіть у директорію проєкту та активуйте віртуальне середовище

```bash
 python -m venv .venv
 # On Windows:
 .venv\Scripts\activate
 # On Unix/MacOS:
 source .venv/bin/activate
```

3. Встановіть необхідні залежності

```bash
# Install all dependencies (including development tools)
pip install -r requirements.txt
```

4. Запустіть головний файл main.py в папці з потрібним завданням

```bash
python main_task\main.py
```

## Основне завдання (завдання 1-3)

Взято базову реалізацію AVL-дерева. До базової реалізації додано наступні функції:

- `min_value_node` - повертає вузол дерева з найменшим значенням ключа
- `max_value_node` - повертає вузол дерева з найбільшим значенням ключа
- `get_total` - повертає суму значень ключів всіх вузлів дерева
