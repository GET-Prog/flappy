import os


def get_image_path(filename):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "images", filename)
    )
