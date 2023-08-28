import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.ops import unary_union, polygonize
from matplotlib.pyplot import cm
import numpy as np



def plot_coords(coords, color):
    pts = list(coords)
    x, y = zip(*pts)
    # print(color)
    plt.plot(x,y, color='k', linewidth=1)
    plt.fill_between(x, y, facecolor=color)


def plot_polys(polys, color):
    for poly, color in zip(polys, color):
        plot_coords(poly.exterior.coords, color)

x = 0
y = 0
h = 1.73205080757

points = [# center
          Point(x, y),
          #  first ring
          Point((x + 2), y),
          Point((x - 2), y),
          Point((x + 1), (y + h)),
          Point((x - 1), (y + h)),
          Point((x + 1), (y - h)),
          Point((x - 1), (y - h)),
          # second ring
          Point((x + 3), h),
          Point((x - 3), h),
          Point((x + 3), -h),
          Point((x - 3), -h),
          Point((x + 2), (h + h)),
          Point((x - 2), (h + h)),
          Point((x + 2), (-h + -h)),
          Point((x - 2), (-h + -h)),
          Point((x + 4), y),
          Point((x - 4), y),
          Point(x, (h + h)),
          Point(x, (-h + -h)),
          #third ring
          Point((x + 4), (h + h)),
          Point((x - 4), (h + h)),
          Point((x + 4), (-h + -h)),
          Point((x - 4), (-h + -h)),
          Point((x + 1), (h + h + h)),
          Point((x - 1), (h + h + h)),
          Point((x + 1), (-h + -h + -h)),
          Point((x - 1), (-h + -h + -h)),
          Point((x + 5), h),
          Point((x - 5), h),
          Point((x + 5), -h),
          Point((x - 5), -h)]

# buffer points to create circle polygons

circles = []
for point in points:
    circles.append(point.buffer(2))


# unary_union and polygonize to find overlaps

rings = [LineString(list(pol.exterior.coords)) for pol in circles]
union = unary_union(rings)
result_polys = [geom for geom in polygonize(union)]

# remove tiny sliver polygons
threshold = 0.01
filtered_polys = [polygon for polygon in result_polys if polygon.area > threshold]

# remove outer circle fragments
complete_polys = [polygon for polygon in filtered_polys if (polygon.centroid.x**2 + polygon.centroid.y**2 < 4**2)]

print("total polygons = " + str(len(result_polys)))
print("filtered polygons = " + str(len(filtered_polys)))
print("complete polygons = " + str(len(complete_polys)))


fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)


# separate petals from triangles

limit = 0.66
petals = [polygon for polygon in complete_polys if polygon.area > limit]

triangles = [polygon for polygon in complete_polys if polygon.area < limit]

colors1 = "w" * len(petals)
# colors2 = "k" * len(triangles)
colors2 = cm.viridis(np.linspace(0, 1, len(triangles)))

plot_polys(petals, color = colors1)
plot_polys(triangles, color = colors2)

ax.set_aspect('equal')
plt.show()