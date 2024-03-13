import math
import random
import matplotlib.pyplot as plt

def random_point_on_circle():        # returns a random point on the unit circle
    theta = random.uniform(0, 2 * math.pi)
    x = math.cos(theta)
    y = math.sin(theta)
    return (x, y)

def random_point_in_circle():       # returns a random point inside the unit circle
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    while x ** 2 + y ** 2 >= 1:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
    return (x, y)

def bertrands_paradox_actual(num_trials): # code for the actual problem statement of the paradox that is length of the chord being greater than the side of the equilateral triangle
    chords = []
    greater_count = 0

    for i in range(num_trials):
        point1 = random_point_on_circle()
        point2 = random_point_on_circle()
        length = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        if length > math.sqrt(3):
            greater_count += 1
        chords.append((point1, point2))

    probability = greater_count / num_trials
    print("Probability of the random chord being longer than the side of the inscribed equilateral triangle: ", probability)
    return chords

def bertrands_paradox_distance_of_midpt_from_centre(num_trials): # code for the distance of the midpoint of the chord being less than 0.5
    inside_points = []
    outside_points = []
    greater_count = 0
    for i in range(num_trials):
        point = random_point_in_circle()
        distance = math.sqrt(point[0]**2 + point[1]**2)
        if distance < 0.5:
            greater_count += 1
        if distance < 0.5 and i % 150 == 0:
            inside_points.append(point)
        elif i % 150 == 0:
            outside_points.append(point)

    probability = greater_count / num_trials
    print("Probability when the distance of the midpoint of the random chord being less than 0.5: ", probability)
    return inside_points, outside_points

def plot_midpoint(inside_points, outside_points):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    circle = plt.Circle((0, 0), 1, color='b', fill=False)
    ax.add_artist(circle)

    inside_x, inside_y = zip(*inside_points)
    outside_x, outside_y = zip(*outside_points)

    plt.scatter(inside_x, inside_y, color='r', label='Inside Circle of radius 0.5')
    plt.scatter(outside_x, outside_y, color='g', label='Outside Circle of radius 0.5')

    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Midpoint of chords')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    plt.show()


def bertrands_paradox_fixing_one_point(num_trials): # code for fixing one point and varying the other
    chords = []
    greater_count = 0
    for i in range(num_trials):
        point = random_point_on_circle()
        if point[0] > 0.5:
            greater_count += 1
        chords.append(((-1,0), point))

    probability = greater_count / num_trials
    print("Probability when one point is fixed and other varies: ", probability)
    return chords

def bertrands_paradox_taking_parallel_lines(num_trials): # code for taking parallel lines and checking the probability of the chord being longer than the side of the equilateral triangle
    chords = []
    greater_count = 0
    for i in range(num_trials):
        y = random.uniform(-1, 1)
        point1 = (-math.sqrt(1-y*y), y)
        point2 = (math.sqrt(1-y*y), y)
        if y < 0.5 and y > -0.5:
            greater_count += 1
        chords.append((point1, point2))

    probability = greater_count / num_trials
    print("Probability when the taking parallel chords: ", probability)
    return chords

def plot_chords(chords, message):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    circle = plt.Circle((0, 0), 1, color='b', fill=False)
    ax.add_artist(circle)

    for chord in chords:
        point1, point2 = chord
        length = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        if length > math.sqrt(3):
            plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='r')  # Longer chords in red
        else:
            plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='g')  # Shorter chords in green

    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(message)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


num_trials = 100000
chords_actual = bertrands_paradox_actual(num_trials)
inside_points, outside_points = bertrands_paradox_distance_of_midpt_from_centre(num_trials)
chords_fixing = bertrands_paradox_fixing_one_point(num_trials)
chords_parallel = bertrands_paradox_taking_parallel_lines(num_trials)

plot_chords(chords_actual[::200], "Actual chords")  # Plot every 200th chord
plot_midpoint(inside_points, outside_points)
plot_chords(chords_fixing[::200], "Fixed one point")
plot_chords(chords_parallel[::200], "Taking parallel chords")
