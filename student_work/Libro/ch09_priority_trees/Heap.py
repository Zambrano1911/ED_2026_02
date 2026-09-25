class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        # Mientas el hijo sea menor que el padre, se intercambian
        while self.arreglo[i] < self.arreglo[i // 2]:
            parent = i // 2
            self.arreglo[i], self.arreglo[parent] = (
                self.arreglo[parent],
                self.arreglo[i],
            )
            i = parent

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        min_val = self.arreglo[1]
        last_val = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = last_val
            i = 1
            n = len(self.arreglo) - 1

            while i * 2 <= n:
                left = i * 2
                right = i * 2 + 1

                if right <= n and self.arreglo[right] < self.arreglo[left]:
                    min_child = right
                else:
                    min_child = left

                if self.arreglo[i] > self.arreglo[min_child]:
                    self.arreglo[i], self.arreglo[min_child] = (
                        self.arreglo[min_child],
                        self.arreglo[i],
                    )
                    i = min_child
                else:
                    break

        return min_val

    def build_heap(self, lista):
        self.arreglo = [float("-inf")] + list(lista)
        n = len(self.arreglo) - 1
        for start in range(n // 2, 0, -1):
            i = start
            while i * 2 <= n:
                left = i * 2
                right = i * 2 + 1

                if right <= n and self.arreglo[right] < self.arreglo[left]:
                    min_child = right
                else:
                    min_child = left

                if self.arreglo[i] > self.arreglo[min_child]:
                    self.arreglo[i], self.arreglo[min_child] = (
                        self.arreglo[min_child],
                        self.arreglo[i],
                    )
                    i = min_child
                else:
                    break

pasos = [
    ('insert', 10, [float('-inf'), 10]),
    ('insert', 15, [float('-inf'), 10, 15]),
    ('insert', 20, [float('-inf'), 10, 15, 20]),
    ('insert', 20, [float('-inf'), 10, 15, 20, 20]),
    ('insert', 50, [float('-inf'), 10, 15, 20, 20, 50]),
    ('insert', 46, [float('-inf'), 10, 15, 20, 20, 50, 46]),
    ('insert', 30, [float('-inf'), 10, 15, 20, 20, 50, 46, 30]),
    ('insert', 40, [float('-inf'), 10, 15, 20, 20, 50, 46, 30, 40]),
    ('insert', 5, [float('-inf'), 5, 10, 20, 15, 50, 46, 30, 40, 20]),
    ('remove_smallest', [float('-inf'), 10, 15, 20, 20, 50, 46, 30, 40]),
    ('remove_smallest', [float('-inf'), 15, 20, 20, 40, 50, 46, 30]),
    ('remove_smallest', [float('-inf'), 20, 30, 20, 40, 50, 46]),
    ('insert', 3, [float('-inf'), 3, 30, 20, 40, 50, 46, 20]),
    ('insert', 25, [float('-inf'), 3, 25, 20, 30, 50, 46, 20, 40]),
    ('remove_smallest', [float('-inf'), 20, 25, 20, 30, 50, 46, 40]),
    ('remove_smallest', [float('-inf'), 20, 25, 40, 30, 50, 46]),
]

h = Heap()
for n, paso in enumerate(pasos, 1):
    if paso[0] == 'insert':
        _, valor, esperado = paso
        h.insert(valor)
        nombre = f'insert({valor})'
    else:
        _, esperado = paso
        h.remove_smallest()
        nombre = 'remove_smallest()'
    if h.arreglo == esperado:
        print(f'Paso {n:2d} OK   {nombre}')
    else:
        print(f'Paso {n:2d} FALLA {nombre}')
        print('   arreglo esperado:', esperado)
        print('   arreglo obtenido:', h.arreglo)
        break
else:
    print('Todos los tests pasaron.')