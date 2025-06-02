import random
import timeit

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_k_lists(lists):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0].copy()
    mid = len(lists) // 2
    left_merged = merge_k_lists(lists[:mid])
    right_merged = merge_k_lists(lists[mid:])
    return _merge(left_merged, right_merged)

if __name__ == "__main__":
    test_arrays = [
        [5, 2, 9, 1, 5, 6],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 3, 3, 0, -1],
    ]

    print("=== Тестування сортування вставками, злиттям та Timsort (built-in sorted) ===")
    for idx, arr in enumerate(test_arrays, start=1):
        arr_copy = arr.copy()
        print(f"\nТест #{idx}: вхідний масив: {arr_copy}")
        sorted_ins = insertion_sort(arr_copy)
        print(f"  Insertion Sort: {sorted_ins}")
        sorted_merge = merge_sort(arr_copy)
        print(f"  Merge Sort:     {sorted_merge}")
        sorted_timsort = sorted(arr_copy)
        print(f"  Timsort:        {sorted_timsort}")

    print("\n=== Тестування merge_k_lists ===")
    lists_example = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list_example = merge_k_lists(lists_example)
    print(f"Вхідні списки: {lists_example}")
    print(f"Об’єднаний відсортований список: {merged_list_example}")

    empty_example = []
    print(f"\nПриклад із порожнім списком: {merge_k_lists(empty_example)}")  # []


    random_lists = []
    for _ in range(5):
        lst = sorted(random.sample(range(100), 10))
        random_lists.append(lst)
    merged_random_lists = merge_k_lists(random_lists)
    print(f"\nТест merge_k_lists із 5 випадкових відсортованих списків по 10 елементів кожен:")
    print(f"  Списки: {random_lists}")
    print(f"  Результат: {merged_random_lists}")


    print("\n=== Простий бенчмаркінг (timeit) ===")
    sizes = [1000, 5000, 10000, 20000]
    for n in sizes:

        base_list = random.sample(range(n * 10), n)
        setup_code = (
            "from __main__ import insertion_sort, merge_sort; "
            f"arr = {base_list}"
        )


        if n <= 1000:
            t_ins = timeit.timeit("insertion_sort(arr)", setup=setup_code, number=3)
        else:
            t_ins = None


        t_merge = timeit.timeit("merge_sort(arr)", setup=setup_code, number=3)

        t_timsort = timeit.timeit("sorted(arr)", setup=setup_code, number=3)

        print(f"\nРозмір масиву: {n}")
        if t_ins is not None:
            print(f"  Insertion Sort (3 запуски): {t_ins:.6f} с")
        else:
            print(f"  Insertion Sort: пропускаємо для n > 1000")
        print(f"  Merge Sort     (3 запуски): {t_merge:.6f} с")
        print(f"  Timsort        (3 запуски): {t_timsort:.6f} с")


    print("\n=== Додаткові тести на випадкових даних ===")
    for algorithm_name, algorithm_func in [("Insertion Sort", insertion_sort),
                                           ("Merge Sort", merge_sort),
                                           ("Timsort", sorted)]:
        arr_rand = random.sample(range(50), 10)
        print(f"\nАлгоритм: {algorithm_name}")
        print(f"  Початковий масив: {arr_rand}")
        result = algorithm_func(arr_rand)
        print(f"  Відсортований:    {result}")
