

def grey(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return [[0], [1]]
    left_part = grey(n-1)
    right_part = []
    for vector in left_part[::-1]:
        right_part.append(vector + [1])
        vector.append(0)
    return left_part + right_part


def read_data():
    n = int(input("Введите количество районов: "))
    print("Введите Матрицу смежности:")
    adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]
    costs = list(map(int, input("Введите {0} цен:\n".format(n)).split()))
    return adjacency_matrix, costs


def solve(adjacency_matrix, costs):

    n = len(costs)

    scalar_product = lambda a, b: sum([a[i]*b[i] for i in range(n)])
    area_controlled = lambda vec, mtrx: all([scalar_product(vec, mtrx[i]) >= 1 for i in range(n)])

    best_vector, best_cost = [], sum(map(abs, costs)) + 1

    for v in grey(n):
        cur_cost = scalar_product(v, costs)
        if area_controlled(v, adjacency_matrix) and best_cost > cur_cost:
            best_vector = v
            best_cost = cur_cost

    return best_cost, best_vector

if __name__ == "__main__":

    g = grey(3)
    print(len(g))
    for v in g:
        print(v)

    s = solve(*read_data())
    if not s[1]:
        print("Контроль всей территоррии невозможен")
    else:
        print("минимальная стоимость: {0}.\nразмещать базы следует в районах:\n{1}"
              .format(s[0], [i+1 for i in range(len(s[1])) if s[1][i]]))
