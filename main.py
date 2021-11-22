import moviepy.editor as mpe
import os
from hashlib import md5
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'hello'}


@app.post('/upload')
async def upload(file: UploadFile = File(..., media_type='video/mpeg')):
    file_name = file.filename
    ext = os.path.splitext(file_name)[-1]
    content = await file.read()
    hash_name = md5(content).hexdigest()
    new_file = f'./video/{hash_name}{ext}'
    with open(new_file, 'wb') as f:
        f.write(content)
    cache = mpe.VideoFileClip(new_file)
    gif_path = f'./gif/{hash_name}.gif'
    cache.write_gif(gif_path, fps=15)
    return FileResponse(gif_path)
