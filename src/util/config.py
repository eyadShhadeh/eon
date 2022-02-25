from os import getenv


class Config:
    """
    class to hold and mange app settings and external configuration
    """

    FILE_URL = getenv(
        "target_model_url",
        "https://nervous-mouse.s3.eu-central-1.amazonaws.com/raw_039.stl",
    )
