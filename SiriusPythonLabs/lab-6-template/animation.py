import matplotlib.pyplot as plt
from LorenzAttractor import Point
import imageio


def plot_static(all_points):
    xs = all_points[0]
    ys = all_points[1]
    zs = all_points[2]

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    ax.plot(xs, ys, zs, '.g', lw=0.02)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.savefig('Lorenz Attractor')
    plt.show()


def plot_animation(all_points):
    x = all_points[0].tolist()
    y = all_points[1].tolist()
    z = all_points[2].tolist()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_prev, y_prev, z_prev = 0, 0, 0

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor Animation \n *Меньше точек для нормальной скорости отображения*")

    images = []
    start_alpha = 0.3

    for i in range(0, len(x), 1):
        if i == 0 or Point(x[i], y[i], z[i]).dist(Point(x_prev, y_prev, z_prev)) > 1:
            #print(i, Point(x[i], y[i], z[i]).dist(Point(x_prev, y_prev, z_prev)))
            x_prev = x[i]
            y_prev = y[i]
            z_prev = z[i]
            ax.scatter(x[i], y[i], z[i], color='g', alpha=i * (1 - start_alpha)/(len(x)) + start_alpha, lw=0.02)
            filename = f'./resources/for_gif/image_{i}.png'
            plt.savefig(filename)
            images.append(imageio.imread(filename))
            print(i)
    imageio.mimsave('resources/animation1.gif', images, duration=0.3)
    print("FINISH ANIMATION")
