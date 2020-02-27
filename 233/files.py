from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path('/home/ch/tmp')
LOG_DIR = TMP 
ZIP_FILE = TMP / 'logs.zip'

def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    path = directory 
    files = sorted([ ( file.name, file.stat().st_mtime) 
                     for file in path.iterdir() ], key=lambda x: -x[1])
    with ZipFile(zip_file, 'w') as myzip:
        for name, m_time in files:
            prefix, suffix = name.split('.')
            time = datetime.fromtimestamp(m_time)
            date = time.strftime('_%Y-%m-%d')
            filename = f'{path}/{name}' 
            arcname = f'{prefix}{date}.{suffix}'
            myzip.write(filename=filename, arcname=arcname)
            n -= 1
            if n == 0:
                return myzip 