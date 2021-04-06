INF = 10000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def on_segment(p: Point, q: Point, r: Point):
    return max(q.x, r.x) >= p.x >= min(q.x, r.x) and max(q.y, r.y) >= p.y >= min(q.y, r.y)


def orientation(p: Point, q: Point, r: Point):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 1
    else:
        return 2


def do_intersect(p1: Point, q1: Point, p2: Point, q2: Point):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if (o1 == 0 and on_segment(p1, p2, q1) or
            o2 == 0 and on_segment(p1, q2, q1) or
            o3 == 0 and on_segment(p2, p1, q2) or
            o4 == 0 and on_segment(p2, q1, q2)):
        return True
    return False


def is_inside(polygons, n: int, p: Point):
    if n < 3:
        return False
    extreme = Point(INF, p.y)
    count, i = 0, 0
    while True:
        next_ = (i + 1) % n
        if do_intersect(polygons[i], polygons[next_], p, extreme):
            if orientation(polygons[i], p, polygons[next_]) == 0:
                return on_segment(polygons[i], p, polygons[next_])
            count += 1
        i = next_
        print(i)
        if i == 0:
            break
    return bool(count % 2)


if __name__ == '__main__':
    polygon1 = Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)
    n = 4
    p = Point(5, 5)
    print('Yes' if is_inside(polygon1, n, p) else 'No')
