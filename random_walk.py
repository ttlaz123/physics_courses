import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random


def walk_path(start, n, d=2):
    assert(len(start) == d)
    path = [start]
    for i in range(n):
        current_pos = path[i][:]
        next_pos = choose_dir(current_pos, d)
        path.append(next_pos)
    return path


def draw_paths(paths, num_steps):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rootn = np.sqrt(num_steps)
    scale = rootn*1.5
    circle = plt.Circle((0, 0), rootn, color='lavender')
    ax.add_artist(circle)
    for path in paths:
        path = np.array(path)
        ax.plot(*path.T)

    plt.xlim(-scale, scale)
    plt.ylim(-scale, scale)
    plt.title("Number of steps: " + str(num_steps) +
              ' , sqrt(N)=' + str(rootn))
    plt.show()
    return


def plot_ends(paths, num_steps):

    rootn = np.sqrt(num_steps)
    scale = rootn*2

    endpointsx = []
    endpointsy = []
    for path in paths:
        endpoint = path[-1]
        endpointsx.append(endpoint[0])
        endpointsy.append(endpoint[1])

    fig = plt.figure()
    circle = plt.Circle((0, 0), rootn, color='lavender', fill=False)
    ax = fig.add_subplot(111)
    ax.add_artist(circle)

    ax.scatter(endpointsx, endpointsy)
    plt.xlim(-scale, scale)
    plt.ylim(-scale, scale)
    plt.title("Number of steps: " + str(num_steps) +
              ' , sqrt(N)=' + str(rootn))
    plt.show()
    plot_angles(endpointsx, endpointsy)
    return


def choose_dir(pos, d):
    ind = random.choice(range(d))
    sign = random.randint(0, 1)
    if(sign == 0):
        sign = -1
    pos[ind] += sign
    return pos


def plot_angles(endx, endy):

    angles = np.arctan2(endy, endx)
    print(angles)
    fig = plt.figure()
    print('making hist')
    plt.hist(angles, bins=30)
    print('done')
    plt.title('Histogram of endpoint angles')
    plt.xlabel('Angle(radians)')
    plt.ylabel('Count')
    plt.show()


def main():
    num_paths = 1000
    num_steps = 10000
    start = [0, 0]
    paths = []
    for i in range(num_paths):
        path = walk_path(start, num_steps)
        paths.append(path)
    #draw_paths(paths, num_steps)
    plot_ends(paths, num_steps)


if __name__ == '__main__':
    main()
