from app.extract import Extractor
import pathlib
import shutil

def test_extracted_file_type():
    # Arrange
    gzip_files_dir = pathlib.Path(__file__).parent.joinpath("files")
    gzip_file_path = gzip_files_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz")
    
    # Act
    e = Extractor(archive_file_path=gzip_file_path, extracted_file_dir=gzip_files_dir)
    is_gzip = e.is_gzip()
    
    # Assert
    assert is_gzip is True

def test_create_extract_dir():
    # Arrange
    extracted_file_dir = pathlib.Path(__file__).parent.joinpath("data_set")
    gzip_files_dir = pathlib.Path(__file__).parent.joinpath("files")
    gzip_file_path = gzip_files_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz")
    
    # Act
    e = Extractor(archive_file_path=gzip_file_path, extracted_file_dir=extracted_file_dir)
    e.create_extract_dir()
    
    # Assert
    assert extracted_file_dir.exists() is True
    
    # Cleanup
    shutil.rmtree(extracted_file_dir)
    

def test_extracted_file_name():
    # Arrange
    extracted_file_dir = pathlib.Path(__file__).parent.joinpath("data_set")
    gzip_files_dir = pathlib.Path(__file__).parent.joinpath("files")
    gzip_file_path = gzip_files_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz")
    
    # Act
    e = Extractor(archive_file_path=gzip_file_path, extracted_file_dir=extracted_file_dir)
    ext_file_name = e.extracted_file_name()
    
    # Assert
    assert ext_file_name == "StormEvents_details-ftp_v1.0_d1950_c20210803.csv"
    
def test_extracted_file_path():
    # Arrange
    extracted_file_dir = pathlib.Path(__file__).parent.joinpath("data_set")
    gzip_files_dir = pathlib.Path(__file__).parent.joinpath("files")
    gzip_file_path = gzip_files_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz")
    
    # Act
    e = Extractor(archive_file_path=gzip_file_path, extracted_file_dir=extracted_file_dir)
    ext_file_path = e.extracted_file_path()
    
    # Assert
    assert ext_file_path == extracted_file_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv")
    

def test_extract_gzip_file():
    # Arrange
    extracted_file_dir = pathlib.Path(__file__).parent.joinpath("data_set")
    gzip_files_dir = pathlib.Path(__file__).parent.joinpath("files")
    gzip_file_path = gzip_files_dir.joinpath("StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz")
    
    # Act
    e = Extractor(archive_file_path=gzip_file_path, extracted_file_dir=extracted_file_dir)
    ext_file_path = e.extract_file()
    
    # Assert
    assert ext_file_path.exists() is True

def test_extract_non_gzip_file():
    # Arrange
    extracted_file_dir = pathlib.Path(__file__).parent.joinpath("data_set")
    non_gzip_file_path = extracted_file_dir.joinpath("text_file.txt")
    if not non_gzip_file_path.exists():
        with open(non_gzip_file_path, "w") as f:
            f.write("Not a gzip file")
    
    # Act
    e = Extractor(archive_file_path=non_gzip_file_path, extracted_file_dir=extracted_file_dir)
    ext_file_path = e.extract_file()
    
    # Assert
    assert ext_file_path is None
