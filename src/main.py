import math
from pathlib import Path

import requests
from matplotlib import pyplot
from mpl_toolkits import mplot3d
from stl import mesh

from util.config import Config


def _get_asset(asset_url=Config.FILE_URL) -> None:
    """
    Get external file, will defult to specific source

    :param asset_url: str Link of the wanted asset/model
    """
    data = requests.get(asset_url)

    Path("assets/").mkdir(parents=True, exist_ok=True)
    with open("assets/raw_039.stl", "wb") as file:
        file.write(data.content)


def execute():
    """
    Script to rotate the targeted
    """
    _get_asset()

    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    # Load the STL files
    target_mesh = mesh.Mesh.from_file("assets/raw_039.stl")

    # rotate
    target_mesh.rotate([0, 1, 0], math.radians(180))
    Path("output/").mkdir(parents=True, exist_ok=True)
    mesh.Mesh.save(target_mesh, filename="output/raw_039_rotated.stl")

    # add the vectors to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(target_mesh.vectors))

    # Auto scale to the mesh size
    scale = target_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()


if __name__ == "__main__":
    execute()
