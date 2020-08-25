# Complete the jimOrders function below.
def jimOrders(orders):
    s=sorted(enumerate(orders,1),key=lambda x:sum(x[1]))
    return [i[0] for i in s]

if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    print(*jimOrders(orders))

    
