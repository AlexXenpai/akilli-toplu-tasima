import math

class KDNode:
    def __init__(self, stop, axis, left=None, right=None):
        self.stop = stop
        self.axis = axis
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, stops):
        copied_stops = [stop.copy() for stop in stops]
        self.root = self._build(copied_stops, 0)

    def _build(self, stops, depth):
        if not stops:
            return None

        axis = depth % 2
        key = "x" if axis == 0 else "y"

        stops.sort(key=lambda stop: stop[key])
        mid = len(stops) // 2

        return KDNode(
            stop=stops[mid],
            axis=axis,
            left=self._build(stops[:mid], depth + 1),
            right=self._build(stops[mid + 1:], depth + 1)
        )

    def _distance(self, point, stop):
        return math.sqrt((point[0] - stop["x"]) ** 2 + (point[1] - stop["y"]) ** 2)

    def k_nearest(self, point, k):
        best = []

        def search(node):
            if node is None:
                return

            distance = self._distance(point, node.stop)
            best.append((distance, node.stop))
            best.sort(key=lambda item: item[0])

            if len(best) > k:
                best.pop()

            axis = node.axis
            point_value = point[axis]
            node_value = node.stop["x"] if axis == 0 else node.stop["y"]

            first = node.left if point_value < node_value else node.right
            second = node.right if point_value < node_value else node.left

            search(first)

            if len(best) < k or abs(point_value - node_value) < best[-1][0]:
                search(second)

        search(self.root)

        result = []
        for distance, stop in best:
            item = stop.copy()
            item["distanceToUser"] = round(distance, 2)
            result.append(item)

        return result