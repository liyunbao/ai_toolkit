from os import listdir, path
from os.path import isfile, join
import os

UPLOAD_FOLDER = "D:\\github\\log_analysis_openai\\uploads"

def getLatestFile(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


def getFileContent(dir):
    # read the content of the file under UPLOAD_FOLDER
    # delete UPLOAD_FOLDER after the reading is done
    import shutil
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    log_file = None
    if len(onlyfiles) > 0:
        log_file = onlyfiles[0]

    content = None
    print(f'{dir}, {log_file}')
    with open(os.path.join(dir, log_file), "r") as f:
        content = f.read()
    # delete upload folder
    shutil.rmtree(dir)

    # because GPT-4 has max token limitation(10,000)
    # so we need to limit the input size
    words = content.split(' ')
    result = ' '.join(words[:9000])
    return result

#getFileContent(UPLOAD_FOLDER)
log_file = getLatestFile(UPLOAD_FOLDER)
print(log_file)

content = None
from pathlib import Path
with open(Path(log_file), "r") as f:
    content = f.read()
    print(content)