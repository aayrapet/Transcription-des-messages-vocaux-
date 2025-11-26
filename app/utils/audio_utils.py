
import os
from werkzeug.utils import secure_filename

def allowed_file() :
    return None

def save_temp_file(file):
    filename = secure_filename(file.filename)
    temp_path = f"/tmp/{filename}"
    file.save(temp_path)
    return temp_path