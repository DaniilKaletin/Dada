def select_max_tasks(tasks):
    """
    Выбирает максимальное количество непересекающихся задач.
    
    Args:
        tasks: список кортежей (время начала, время завершения)
    
    Returns:
        tuple: (выбранные задачи, количество задач)
    """
    # Сортируем задачи по времени завершения
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    
    selected_tasks = []
    last_end_time = -float('inf')  # время завершения последней выбранной задачи
    
    for task in sorted_tasks:
        start, end = task
        
        # Если задача начинается после завершения предыдущей выбранной
        if start >= last_end_time:
            selected_tasks.append(task)
            last_end_time = end
    
    return selected_tasks, len(selected_tasks)

def main():
    # Входные данные
    tasks = [(1, 3), (2, 5), (4, 6), (5, 8), (7, 9), (8, 10)]
    
    print("Все задачи:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    print("\n" + "="*50)
    
    # Выбираем максимальное количество непересекающихся задач
    selected_tasks, count = select_max_tasks(tasks)
    
    print("Выбранные задачи (в порядке выбора):")
    for i, task in enumerate(selected_tasks, 1):
        print(f"{i}. {task}")
    
    print(f"\nОбщее количество выбранных задач: {count}")
    
    # Визуализация для наглядности
    print("\n" + "="*50)
    print("Визуализация временных интервалов:")
    print("Время: 0 1 2 3 4 5 6 7 8 9 10")
    print("-" * 35)
    
    for i, task in enumerate(tasks, 1):
        start, end = task
        marker = "✓" if task in selected_tasks else " "
        spaces = " " * start
        duration = "─" * (end - start - 1)
        print(f"{marker} Задача {i}: {spaces}├{duration}┤ ({start}-{end})")

if __name__ == "__main__":
    main()