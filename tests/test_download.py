from app.download import Downloader
import pathlib
import os


def test_download_init():
    # Arrange
    dl_dir = pathlib.Path(__file__).parent.joinpath("downloads")
    url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz"

    # Act
    d = Downloader(url=url, download_dir=dl_dir)

    # Assert
    assert d.url == url
    assert d.download_dir == dl_dir


def test_create_download_dir():
    # Arrange
    dl_dir = pathlib.Path(__file__).parent.joinpath("downloads")
    url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz"

    # Act
    d = Downloader(url=url, download_dir=dl_dir)
    d.create_download_dir()

    assert d.download_dir.exists() is True


def test_download_file_path():
    # Arrange
    dl_dir = pathlib.Path(__file__).parent.joinpath("downloads")
    url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz"

    # Act
    d = Downloader(url=url, download_dir=dl_dir)
    dl_file_path = d.download_file_path()

    # Assert
    assert dl_file_path == pathlib.Path(dl_dir).joinpath(
        "StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz"
    )


def test_download_file():
    # Arrange
    dl_dir = pathlib.Path(__file__).parent.joinpath("downloads")
    url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz"

    # Act
    d = Downloader(url=url, download_dir=dl_dir)
    dl_file_path = d.download_file_path()
    if dl_file_path.exists() is True:
        os.remove(dl_file_path)
    new_dl_file_path = d.download_file()

    # Assert
    assert new_dl_file_path.exists() is True
