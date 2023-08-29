#%%

import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.ops import unary_union, polygonize

from matplotlib.pyplot import cm
import numpy as np

from colorir import Grad

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

pink = "#fff07e"
blue = "#71e2ff"
green = "#98e68e"
red = "#ff0000"

# colors = [
#     pink, blue, red, # 0, 1, 2
#     green, blue, pink, # 3, 4, 5
#     pink, pink, pink, # 6, 7, 8
#     pink, green, blue, # 9, 10, 11
#     pink, green, blue, # 12, 13, 14
#     pink, pink, pink] # 15, 16, 17

# print(colors)

# colors = cm.viridis(np.linspace(0, 1, len(complete_polys)))
# print(colors)
# colors = ['pink','blue']
colors = Grad(["ff0000", "0000ff"]).n_colors(66)
#plot_polys(circles, colors)
#plt.show()


fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

# plot resulting polygons


plot_polys(complete_polys, colors)


centroidCoords = [
    Point(0.9999999999999997, -0.5773635180985456),
    Point(1.5000000000000004, -0.866025403785),
    Point(1.9999999999999987, -1.154687289471454),
    Point(0, -1.1546872894714544),
    Point(0, -1.7320508075699992),
    Point(-0.0000000000000002, -2.3094143256685467),
    Point(-1.0000000000000004, -0.577363518098546),
    Point(-1.5, -0.8660254037850001),
    Point(-1.9999999999999996, -1.154687289471454),
    Point(-1, 0.5773635180985459),
    Point(-1.5000000000000004, 0.8660254037850001),
    Point(-1.9999999999999993, 1.1546872894714537),
    Point(-0.0000000000000001, 1.1546872894714542),
    Point(0, 1.73205080757),
    Point(0.0000000000000001, 2.309414325668546),
    Point(1, 0.5773635180985456),
    Point(1.5000000000000002, 0.8660254037849999),
    Point(1.9999999999999993, 1.1546872894714542),
    Point(2.9999999999999987, -0.5773635180985457),
    Point(3.5, -0.8660254037849997),
    Point(2, -1.73205080757),
    Point(1.9999999999999996, -2.309414325668546),
    Point(0.5, -0.8660254037850001),
    Point(0.5, 0.866025403785),
    Point(2, 1.7320508075700005),
    Point(2.0000000000000004, 2.3094143256685467),
    Point(3.0000000000000004, 0.5773635180985458),
    Point(3.4999999999999996, 0.8660254037849999),
    Point(-0.5000000000000001, -0.866025403785),
    Point(-2.0000000000000004, -1.7320508075699999),
    Point(-2.000000000000001, -2.3094143256685475),
    Point(-3.000000000000001, -0.5773635180985459),
    Point(-3.500000000000001, -0.866025403785),
    Point(-3.0000000000000018, 0.5773635180985461),
    Point(-3.4999999999999987, 0.8660254037849999),
    Point(-2.0000000000000004, 1.73205080757),
    Point(-1.9999999999999996, 2.3094143256685467),
    Point(-0.5, 0.8660254037849999),
    Point(2.5, 0.866025403785),
    Point(1, 0),
    Point(-0.5000000000000001, 2.5980762113550004),
    Point(-0.9999999999999994, 2.886738097041452),
    Point(1.0000000000000009, 2.8867380970414565),
    Point(0.9999999999999997, 3.4641016151399993),
    Point(2.5000000000000004, 2.598076211355),
    Point(-0.9999999999999997, 0),
    Point(-2.5, 0.8660254037850001),
    Point(-2.500000000000001, 2.598076211355001),
    Point(-0.9999999999999999, 3.4641016151399993),
    Point(0.4999999999999998, 2.5980762113549987),
    Point(2.5000000000000004, -2.598076211355),
    Point(1.0000000000000002, -2.8867380970414547),
    Point(1.0000000000000002, -3.4641016151400006),
    Point(-0.5, -2.598076211355001),
    Point(-0.9999999999999997, -2.8867380970414533),
    Point(2.5000000000000004, -0.8660254037850001),
    Point(0.5, -2.598076211355),
    Point(-0.9999999999999992, -3.464101615139999),
    Point(-2.5, -2.598076211355001),
    Point(-2.5000000000000004, -0.8660254037850001),
    Point(3, 0),
    Point(1.5000000000000002, 2.5980762113550004),
    Point(-3.0000000000000004, 0),
    Point(-1.4999999999999998, 2.5980762113549987),
    Point(1.4999999999999998, -2.598076211355001),
    Point(-1.5, -2.598076211355)]



# formatting centroids
# with open('E://centroidCoords') as fp:
#     contents = fp.read()
#     n = contents.replace("POINT (","Point(")
#     #m = contents.replace(" "," ,")
#     print(n)

# with open('E://centroidCoords') as fp:
#     contents = fp.read()
#     n = contents.replace(" ",",")
#     #m = contents.replace(" "," ,")
#     print(n)

# filepath = "E://centroidCoords"
# with open(filepath) as f:
#     lines = f.read().splitlines()

# with open(filepath, "w") as f:
#     for line in lines:
#         f.write(line + ",\n")








         
# plot centroids

# centroidCoords = 0
# df=open('E://centroidCoords','w')
# for poly in complete_polys:
#    centroidCoords = (poly.centroid.wkt)
#          df.write(centroidCoords)
#          df.write("\n")
#    print(centroidCoords)
         #plt.plot(centroidCoords)

# print("the number of centroids is: " + str(len(centroidCoords)))

for i in range(len(centroidCoords)):
  plt.scatter(centroidCoords[i].x,centroidCoords[i].y, marker="$"+str(i)+"$")

# for i in range(len(complete_polys)):
#     print([i])

ax.set_aspect('equal')
plt.show()
# %%
