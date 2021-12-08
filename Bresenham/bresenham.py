import matplotlib.pyplot as plt


def rasterify_line(rect, p1, p2):
    '''Bresenham 线栅格化算法'''
    def in_area(x, y):
        return x >= 0 and x < width and y >= 0 and y < height

    def colorify(x, y):
        if in_area(x, y):
            raster[y][x] = 1

    def bresenham():
        x0, y0 = p1
        x1, y1 = p2
        dx = x1-x0
        dy = y1-y0
        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1
        dy <<= 1
        dx <<= 1
        colorify(x0, y0)
        if dx == 0:
            while y0 != y1:
                y0 += stepy
                colorify(x0, y0)
        if dx > dy:
            fraction = dy-(dx >> 1)
            while x0 != x1:
                x0 += stepx

                if fraction >= 0:
                    y0 += stepy
                    fraction -= dx

                fraction += dy
                colorify(x0, y0)
        else:
            fraction = dx - (dy >> 1)
            while y0 != y1:
                if fraction >= 0:
                    x0 += stepx
                    fraction -= dy
                y0 += stepy
                fraction += dx
                colorify(x0, y0)

    gap = 1
    minx, maxx, miny, maxy = rect
    width = int((maxx-minx) // gap + 1)
    height = int((maxy-miny) // gap + 1)
    raster = [[0]*width for _ in range(height)]
    bresenham()

    return raster


def plot(arr):
    _, ax = plt.subplots()
    ax.imshow(arr, cmap="gray", origin="lower")


rect = (0, 14, 0, 14)
raster = rasterify_line(rect, (10, 8), (1, 1))

plot(raster)
plt.xticks(range(0, 14, 2))
plt.yticks(range(0, 14, 2))
plt.show()
