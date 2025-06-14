import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph} # 모든 노드까지의 거리를 무한대로 초기화
    distances[start] = 0 # 시작 노드까지의 거리는 0

    priority_queue = [(0, start)] # (거리, 노드) 튜플을 저장하는 우선순위 큐.
                                  # 거리가 가장 짧은 노드가 먼저 나오도록 함.

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return distances[end]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight 

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    cities = int(input())
    buses = int(input())

    routes = {i: [] for i in range(1, cities + 1)}

    for _ in range(buses):
        start, end, cost = map(int, input().split())
        routes[start].append((end, cost))

    start, end = map(int, input().split())
    # print(routes)

    result = dijkstra(routes, start, end)
    print(result)