import shutil
import os
import uuid6

def save_upload_file(upload_file, destination_dir):
    file_id = uuid6.uuid7()
    
    _, ext = os.path.splitext(upload_file.filename)
    
    new_filename = f"{file_id}{ext}"
    destination_path = os.path.join(destination_dir, new_filename)

    with open(destination_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return new_filename
