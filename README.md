# python_labs
# Лабораторная работа 1
## Задание 1
![Код:](./images/lab01/01.png)
![Вывод:](./images/lab01/01r.png)

## Задание 2
![Код:](./images/lab01/02.png)
![Вывод:](./images/lab01/02r.png)

## Задание 3
![Код:](./images/lab01/03.png)
![Вывод:](./images/lab01/03r.png)

## Задание 4
![Код:](./images/lab01/04.png)
![Вывод:](./images/lab01/04r.png)

## Задание 5
![Код:](./images/lab01/05.png)
![Вывод:](./images/lab01/05r.png)

## Задание 6
![Код:](./images/lab01/06.png)
![Вывод:](./images/lab01/06r.png)

## Задание 7
![Код:](images/lab01/07.png)
![Вывод:](./images/lab01/07r.png)

# Лабораторная работа 2

## Задание 1 - arrays
### min_max
markdown 
```python
test_m_m = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: 
        return 'ValueError'
    return (min(nums), max(nums)) 
for i in test_m_m:
    print(min_max(i))
```
### unique_sorted
markdown
```python
test_u_s = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]
]
def unique_sorted(nums2: list[float | int]) -> list[float | int]:
    if len(nums2) == 0: 
        return 'ValueError'
    return sorted(set(nums2))
for i in test_u_s:
    print(unique_sorted(i))
```

### flatten
markdown
```python
fl_test = [
    [[1, 2], [3, 4]],
    ([1, 2], (3, 4, 5)),
    [[1], [], [2, 3]],
    [[1, 2], "ab"]
]
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for a in mat:
        if isinstance(a, (list, tuple)): result.extend(flatten(a))
        else:
            if type(a) == int or type(a) == float: result.append(a)
            else: return 'TypeError'
    return result
for i in fl_test:
    print(flatten(i))
```
![Вывод:](./images/lab02/1x.png)

## Задание 2 - matrix
markdown 
```python
![Вывод:](./images/lab01/02r.png)

## Задание 3 - tuples
![Код:](./images/lab02/3.png)
![Вывод:](./images/lab02/3x.png)


