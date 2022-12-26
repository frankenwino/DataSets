import pathlib
import magic
import os
import gzip

class Extractor:
    def __init__(self, archive_file_path: pathlib.Path, extracted_file_dir: pathlib.Path):
        self.archive_file_path = archive_file_path
        self.extracted_file_dir = extracted_file_dir
        
    
    def mime_type(self, file_path: pathlib.Path) -> str:
        """mime_type determines the mime_type of a file

        Args:
            file_path (pathlib.Path): a file's path

        Returns:
            str: the file's mime type
        """        
        return magic.from_file(file_path, mime=True)
    
    
    def is_gzip(self) -> bool:
        """is_gzip determines whether or not a file's mime type is application/gzip

        Returns:
            bool: True or False
        """        
        if self.mime_type(file_path=self.archive_file_path) == "application/gzip":
            return True
        else:
            return False

    def create_extract_dir(self):
        """create_extract_dir creates the directory where the gzp file will be extracted to
        """        
        if self.extracted_file_dir.exists() is False:
            self.extracted_file_dir.mkdir(parents=True, exist_ok=True)
        else:
            pass
        
    def extracted_file_name(self) -> str:
        """extracted_file_name creates a file name for the extracted file

        Returns:
            str: file name for the file to extracted
        """        
        file_name = pathlib.PurePath(self.archive_file_path).name
        ext_file_name = os.path.splitext(file_name)[0]
        
        return ext_file_name
    
    def extracted_file_path(self) -> pathlib.Path:
        """extracted_file_path creates a file path for the extracted file

        Returns:
            pathlib.Path: file path for the extracted file
        """        
        ext_file_name = self.extracted_file_name()
        ext_file_path = self.extracted_file_dir.joinpath(ext_file_name)
        
        return ext_file_path
    
    def extract_file(self) -> pathlib.Path or None:
        """extract_file extracts a gzip file

        Returns:
            pathlib.Path or None: the exracted gzip file path or None is the archive is not a gzip file
        """
        if self.is_gzip():
            ext_file_path = self.extracted_file_path()
            self.create_extract_dir()
            with open(self.archive_file_path, 'rb') as inf, open(ext_file_path, 'w', encoding='utf8') as tof:
                decom_str = gzip.decompress(inf.read()).decode('utf-8')
                tof.write(decom_str)
            
            return ext_file_path
        else:
            return None