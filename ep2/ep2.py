import matplotlib.pyplot as plt

def parser(filename):
    data = []
    with open(filename) as f:
        data = list(f.read().split('\n'))
    data.pop(len(data) - 1)
    i = 1
    frame = 1;
    while i < len(data):
        x = [float(a) for a in (data[i - 1].split(' '))]
        y = [float(b) for b in (data[i].split(' '))]
        fig, axs = plt.subplots()
        axs.plot(x, y)
        plt.xlim(0, 15)
        plt.ylim(-15, 15)
        plt.title("Frame " + str(frame))
        plt.grid()
        fig.savefig(str(frame) + ".png")
        i += 2
        frame += 1

parser("sources/frames.dat")
