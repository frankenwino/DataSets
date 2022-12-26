from scrape import Scraper
from download import Downloader
from extract import Extractor
import pathlib
import shutil
import utils

if __name__ == "__main__":
    download_dir = pathlib.Path(__file__).parent.parent.joinpath("downloads")
    dataset_dir = pathlib.Path(__file__).parent.parent.joinpath("dataset_csv_files")
    s = Scraper()
    csv_gz_links = s.csv_gz_links()
    count = 0
    total = len(csv_gz_links)
    for csv_gz_link in csv_gz_links:
        count += 1
        utils.print_message(f"Processing URL {count} of {total}")
        d = Downloader(url=csv_gz_link, download_dir=download_dir)
        csv_gz_file_path = d.download_file()
        e = Extractor(archive_file_path=csv_gz_file_path, extracted_file_dir=dataset_dir)
        e.extract_file()
    shutil.rmtree(download_dir)
    
    print(f"Data set CSV files: {dataset_dir}")