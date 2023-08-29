import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.ops import unary_union, polygonize
from matplotlib.pyplot import cm
import numpy as np
from  hsluv import hex_to_hsluv, hsluv_to_hex



def plot_coords(coords, color):
    pts = list(coords)
    x, y = zip(*pts)
    # print(color)
    # plt.plot(x,y, color='k', linewidth=1)
    plt.plot(x,y, color='k', linewidth=0)
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

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

# centroids
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


# separating into petals and triangles
limit = 0.66

triangles = [polygon for polygon in complete_polys if polygon.area < limit]
petals = [polygon for polygon in complete_polys if polygon.area > limit]


# trianlge/petal matrix 
from numpy import NaN

flower_matrix = np.array([
#      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
    [NaN,  0,  8,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 19,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #0
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 31,  7,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #1
    [NaN,NaN,NaN,  1, 12,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #2
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 32, 30], #3 
    [NaN,NaN,NaN,NaN,NaN,  2, 23,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #4
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 13, 35,NaN,NaN,NaN,NaN,NaN,NaN], #5 
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,  3, 17,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #6
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 24, 16,NaN,NaN,NaN,NaN], #7
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,  4,  9,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #8
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 20, 27,NaN,NaN], #9
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,  5,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #10
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,5,  NaN,NaN,NaN, 10, 18,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #11
    [NaN,31, NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 36,NaN,NaN,NaN, 6, NaN,NaN,NaN,NaN], #12
    [NaN,7,  NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 28,NaN,NaN,NaN, 40,NaN], #13
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 10,NaN,NaN,NaN,NaN,NaN, 22,NaN,NaN,NaN, 37,NaN,NaN], #14
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 18, 36,NaN,NaN,NaN, 11,NaN,NaN,NaN,NaN,NaN,NaN,NaN], #15
    [NaN,NaN,NaN,NaN,NaN, 13,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 34,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 41], #16
    [NaN,NaN,NaN,NaN,NaN, 35,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 14,NaN,NaN,NaN,38 ,NaN,NaN,NaN,NaN,NaN], #17
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN, 24,NaN,NaN,NaN,NaN,NaN, 15,NaN,NaN,NaN, 38,NaN,NaN,NaN,NaN,NaN,NaN], #18
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN, 16,NaN,NaN,NaN,NaN, 25,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 39,NaN,NaN,NaN], #19
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 20,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 39,NaN,NaN,NaN, 26], #20
    [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 27,NaN,NaN,NaN,NaN, 37,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 21,NaN], #21
    [NaN,NaN,NaN, 32,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 40,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 29,NaN,NaN], #22
    [NaN,NaN,NaN, 30,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN, 41,NaN,NaN,NaN, 33,NaN,NaN,NaN]])#23

#def combine_hues_sim():
    # find midpoint

#def combine_hues_diff():
    # find midpoint and jump across wheel 


import random
no_of_colors=len(triangles)
rgb_colors =["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]


# convert rgb to hsl
hsl_colors = list()
for i in rgb_colors:
    col = hex_to_hsluv(i)
    hsl_colors.append(col)

# convert list of tuples to list of lists
hsl_colors = [list(elem) for elem in hsl_colors]

# adjust s & l 
for i in hsl_colors:
    i[1] = 75

for i in hsl_colors:
    i[2] = 85

new_hues = list()
for i in range(len(petals)):
    col = hex_to_hsluv("#ffffff")
    new_hues.append(col)

for i in range(len(triangles)):
    print("triangle index: ")
    print(i)
    print("primary triangle color: ")
    print(hsl_colors[i])
    for j in range(0,len(triangles)):
        if not np.isnan(flower_matrix[i,j]):
            p = int(flower_matrix[i,j])
            lower_bound = (hsl_colors[i][0] - 90) % 360
            upper_bound = (hsl_colors[i][0] + 90) % 360
            adjacent_color = hsl_colors[j][0]
            print("next triangle index: ")
            print(j)
            print("adjacent color: ")
            print(adjacent_color)
            print("lower bound: ")
            print(lower_bound)
            print("upper bound: ")
            print(upper_bound)

            if (lower_bound < adjacent_color < upper_bound) or (upper_bound < lower_bound < adjacent_color) or (adjacent_color < upper_bound < lower_bound):
                print("within range, mixing colors")
                mix = ((hsl_colors[i][0] + hsl_colors[j][0]) / 2) + 180 % 360
                print("new color: ")
                print(mix)
                print("\n")
                new_hues[p] = mix
            else:
                print("not within range, mixing colors")
                mix = ((hsl_colors[i][0] + hsl_colors[j][0]) / 2)  % 360
                #mix = (hsl_colors[i][0] + hsl_colors[j][0]) / 2
                print("new color: ")
                print(mix)
                print("\n")
                new_hues[p] = mix



new_sat = [100] * len(new_hues)
new_lum = [70] * len(new_hues)


new_colors = list(zip(new_hues, new_sat, new_lum))

# convert back to rgb 
petals_colors = []
for i in new_colors:
    col = hsluv_to_hex(i)
    petals_colors.append(col)

print(petals_colors)

hex_colors = list()
for i in hsl_colors:
    col = hsluv_to_hex(i)
    hex_colors.append(col)

# i is triangle loop, j is petal
for i in range(len(triangles)):
    plot_coords(triangles[i].exterior.coords, hex_colors[i])
    centroidCoords = triangles[i].centroid
    plt.scatter(centroidCoords.x, centroidCoords.y, marker="$"+str(i)+"$", c="#ffffff")
    for j in range(0,len(triangles)):
        if not np.isnan(flower_matrix[i,j]):
            p = int(flower_matrix[i,j])
            #print(p)
            plot_coords(petals[p].exterior.coords, petals_colors[p])
            centroidCoords = petals[p].centroid
            plt.scatter(centroidCoords.x,centroidCoords.y, marker="$"+str(p)+"$", c="#000000")
            plt.scatter(centroidCoords.x - .2, centroidCoords.y, marker="$"+str(i)+"$", c=hex_colors[i])
            plt.scatter(centroidCoords.x + .2, centroidCoords.y, marker="$"+str(j)+"$", c=hex_colors[j])
            #print(petals_colors[p])
            #print(hex_colors[i])
            #print(hex_colors[j])
            #print("\n")
            
# color_points = [
#           Point(x, y),
#           #  first ring
#           Point((x + 2), y),
#           Point((x - 2), y),
#           Point((x + 1), (y + h)),
#           Point((x - 1), (y + h)),
#           Point((x + 1), (y - h)),
#           Point((x - 1), (y - h))]

# color_circles = []
# for point in color_points:
#     color_circles.append(point.buffer(2))

# print(color_circles)

# plot_polys(color_circles, "k")

ax.set_aspect('equal')
plt.show()

# plt.savefig('flower.pdf')

# import os
# os.getcwd()
