from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files
target_mesh = mesh.Mesh.from_file('assets/raw_039.stl')

#rotate
target_mesh.rotate([0, 1, 0], math.radians(180))
mesh.Mesh.save(target_mesh,filename='output/raw_039_rotated.stl')

#add the vectors to the plot
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(target_mesh.vectors))

# Auto scale to the mesh size
scale = target_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
if __name__=='__main__':
    pyplot.show()

