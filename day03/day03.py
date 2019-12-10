
from dataclasses import dataclass, replace
from itertools import product


@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass(order=True, frozen=True)
class LineSegment:
    start: Point
    end: Point

    @property
    def length(self):
        return self.start.manhattan_distance(self.end)

    def get_intersection(self, other):
        left = max(min(self.start.x, self.end.x), min(other.start.x, other.end.x))
        right = min(max(self.end.x, self.start.x), max(other.end.x, other.start.x))
        bottom = max(min(self.start.y, self.end.y), min(other.start.y, other.end.y))
        top = min(max(self.end.y, self.start.y), max(other.end.y, other.start.y))

        if (left, top) == (right, bottom):
            return Point(left, top)
        # Note there could be overlap by more than just a point, but not an issue for this problem.

    def get_distance_along_segment_to_point(self, point):
        # Returns the distance along the segment to a given point, None if point is not on segment
        on_x_axis = self.start.x == self.end.x == point.x
        on_y_axis = self.start.y == self.end.y == point.y
        within_x = self.start.x <= point.x <= self.end.x or self.end.x <= point.x <= self.start.x
        within_y = self.start.y <= point.y <= self.end.y or self.end.y <= point.y <= self.start.y
        x_delta = abs(self.start.x - point.x)
        y_delta = abs(self.start.y - point.y)

        if on_x_axis and within_y:
            return y_delta
        elif on_y_axis and within_x:
            return x_delta


ORIGIN_POINT = Point(0, 0)


def read_input(filename):
    with open(filename, "rt") as input_file:
        first_path = input_file.readline().strip().split(',')
        second_path = input_file.readline().strip().split(',')
    return first_path, second_path


def get_end_point_from_path(start_point, path):
    direction, length = path[0], int(path[1:])

    if direction == 'U':
        return replace(start_point, y=start_point.y + length)
    elif direction == 'D':
        return replace(start_point, y=start_point.y - length)
    elif direction == 'L':
        return replace(start_point, x=start_point.x - length)
    elif direction == 'R':
        return replace(start_point, x=start_point.x + length)
    else:
        raise ValueError(f'{direction=}')


def build_line_segments(line_path):
    segments = []
    start_point = ORIGIN_POINT

    for path in line_path:
        end_point = get_end_point_from_path(start_point, path)
        segments.append(LineSegment(start=start_point, end=end_point))
        start_point = end_point

    return segments


def get_intersection_points(line_segments1, line_segments2):
    # We could use a sweep algorithm here, but product is just fine for the given dataset size
    return {
        intersection_point
        for segment1, segment2 in product(line_segments1, line_segments2)
        if (intersection_point := segment1.get_intersection(segment2)) is not None
    } - {ORIGIN_POINT}  # exclude origin


def get_closest_intersection_distance(intersection_points):
    closest_distance = min(
        ORIGIN_POINT.manhattan_distance(intersection_point)
        for intersection_point in intersection_points
    )
    return closest_distance


def count_steps_to_target_point(line_segments, target_point):
    total_steps = 0
    for line_segment in line_segments:
        distance = line_segment.get_distance_along_segment_to_point(target_point)
        if distance is not None:
            total_steps += distance
            break
        else:
            total_steps += line_segment.length
    else:
        raise Exception('Target point not found')

    return total_steps


def get_closest_combined_steps(first_segments, second_segments, intersection_points):
    return min(
        sum((
            count_steps_to_target_point(first_segments, intersection_point),
            count_steps_to_target_point(second_segments, intersection_point),
        ))
        for intersection_point in intersection_points
    )


def main():
    filename = "input.txt"
    first_path, second_path = read_input(filename)

    first_segments = build_line_segments(first_path)
    second_segments = build_line_segments(second_path)
    intersection_points = get_intersection_points(first_segments, second_segments)
    closest_distance = get_closest_intersection_distance(intersection_points)

    print(f'Part 1: {closest_distance}')

    closest_steps = get_closest_combined_steps(first_segments, second_segments, intersection_points)
    print(f'Part 2: {closest_steps}')


if __name__ == "__main__":
    main()
