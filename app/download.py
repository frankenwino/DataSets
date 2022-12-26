import requests
import shutil
import pathlib
from urllib.parse import urlparse
import utils


class Downloader:
    def __init__(self, url: str, download_dir: pathlib.Path):
        self.url = url
        self.download_dir = download_dir

    def create_download_dir(self):
        """create_download_dir creates a download directory if none exists."""
        if self.download_dir.exists() is False:
            self.download_dir.mkdir(parents=True, exist_ok=True)
        else:
            pass

    def download_file_path(self) -> pathlib.Path:
        """download_file_path Uses self.url to generate a file path for the file to be downloaded.

        Returns:
            pathlib.Path: a file path
        """
        url_parts = urlparse(self.url)
        path = url_parts.path
        file_name = path.split("/")[-1]

        return pathlib.Path(self.download_dir).joinpath(file_name)

    def download_file(self) -> pathlib.Path:
        """download_file downloads a file.

        Returns:
            pathlib.Path: the downloaded file's path.
        """
        self.create_download_dir()
        dl_file_path = self.download_file_path()
        utils.print_message(f"Downloading {self.url}")
        with requests.get(self.url, stream=True) as r:
            with open(dl_file_path, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        utils.print_message(f"Download complete {dl_file_path}")

        return dl_file_path
