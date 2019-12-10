import pytest

from day03 import (
    build_line_segments,
    count_steps_to_target_point,
    get_closest_combined_steps,
    get_closest_intersection_distance,
    get_end_point_from_path,
    get_intersection_points,
    LineSegment,
    Point,
)


@pytest.mark.parametrize("start_point, path, expected_point", [
    (Point(2, 2), "U5", Point(2, 7)),
    (Point(4, 5), "D2", Point(4, 3)),
    (Point(0, 5), "L3", Point(-3, 5)),
    (Point(5, 2), "R4", Point(9, 2)),
])
def test_get_end_point_from_path_delta(start_point, path, expected_point):
    assert get_end_point_from_path(start_point, path) == expected_point


def test_build_line_segments():
    line_path = ["R8", "U5", "L5", "D3"]
    assert build_line_segments(line_path) == [
        LineSegment(Point(0, 0), Point(8, 0)),
        LineSegment(Point(8, 0), Point(8, 5)),
        LineSegment(Point(8, 5), Point(3, 5)),
        LineSegment(Point(3, 5), Point(3, 2)),
    ]

    line_path = ["U7", "R6", "D4", "L4"]
    assert build_line_segments(line_path) == [
        LineSegment(Point(0, 0), Point(0, 7)),
        LineSegment(Point(0, 7), Point(6, 7)),
        LineSegment(Point(6, 7), Point(6, 3)),
        LineSegment(Point(6, 3), Point(2, 3)),
    ]


def test_line_intersection():
    line1 = LineSegment(start=Point(1, 1), end=Point(1, 5))
    line2 = LineSegment(start=Point(0, 3), end=Point(2, 3))
    assert line1.get_intersection(line2) == Point(1, 3)
    assert line2.get_intersection(line1) == Point(1, 3)

    line1 = LineSegment(start=Point(1, 1), end=Point(5, 1))
    line2 = LineSegment(start=Point(3, 0), end=Point(3, 3))
    assert line1.get_intersection(line2) == Point(3, 1)
    assert line2.get_intersection(line1) == Point(3, 1)

    line1 = LineSegment(start=Point(1, 1), end=Point(5, 1))
    line2 = LineSegment(start=Point(1, 2), end=Point(5, 2))
    assert line1.get_intersection(line2) is None
    assert line2.get_intersection(line1) is None


def test_get_intersection_points():
    line_segments1 = [
        LineSegment(Point(0, 0), Point(8, 0)),
        LineSegment(Point(8, 0), Point(8, 5)),
        LineSegment(Point(8, 5), Point(3, 5)),
        LineSegment(Point(3, 5), Point(3, 2)),
    ]
    line_segments2 = [
        LineSegment(Point(0, 0), Point(0, 7)),
        LineSegment(Point(0, 7), Point(6, 7)),
        LineSegment(Point(6, 7), Point(6, 3)),
        LineSegment(Point(6, 3), Point(2, 3)),
    ]
    intersection_points = get_intersection_points(line_segments1, line_segments2)
    assert intersection_points == {Point(x=6, y=5), Point(x=3, y=3)}


@pytest.mark.parametrize("first_path, second_path, expected_output", [
    (
        ["R8", "U5", "L5", "D3"],
        ["U7", "R6", "D4", "L4"],
        6,
    ),
    (
        ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
        ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        159,
    ),
    (
        ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
        ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        135,
    ),
])
def test_sample_programs(first_path, second_path, expected_output):
    first_segments = build_line_segments(first_path)
    second_segments = build_line_segments(second_path)
    intersection_points = get_intersection_points(first_segments, second_segments)
    assert get_closest_intersection_distance(intersection_points) == expected_output


def test_count_steps_to_target_point():
    line_segments = [
        LineSegment(Point(0, 0), Point(8, 0)),
        LineSegment(Point(8, 0), Point(8, 5)),
        LineSegment(Point(8, 5), Point(3, 5)),
        LineSegment(Point(3, 5), Point(3, 2)),
    ]
    assert count_steps_to_target_point(line_segments, Point(6, 5)) == 15
    assert count_steps_to_target_point(line_segments, Point(3, 3)) == 20

    line_segments = [
        LineSegment(Point(0, 0), Point(0, 7)),
        LineSegment(Point(0, 7), Point(6, 7)),
        LineSegment(Point(6, 7), Point(6, 3)),
        LineSegment(Point(6, 3), Point(2, 3)),
    ]
    assert count_steps_to_target_point(line_segments, Point(6, 5)) == 15
    assert count_steps_to_target_point(line_segments, Point(3, 3)) == 20


def test_get_closest_combined_steps():
    first_segments = [
        LineSegment(Point(0, 0), Point(8, 0)),
        LineSegment(Point(8, 0), Point(8, 5)),
        LineSegment(Point(8, 5), Point(3, 5)),
        LineSegment(Point(3, 5), Point(3, 2)),
    ]
    second_segments = [
        LineSegment(Point(0, 0), Point(0, 7)),
        LineSegment(Point(0, 7), Point(6, 7)),
        LineSegment(Point(6, 7), Point(6, 3)),
        LineSegment(Point(6, 3), Point(2, 3)),
    ]
    intersection_points = {Point(6, 5), Point(3, 3)}
    assert get_closest_combined_steps(first_segments, second_segments, intersection_points) == 30
