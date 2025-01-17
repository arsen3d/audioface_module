# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import HTMLResponse
import os
import datetime

# from requests import request
from ipfs import download_ipfs_folder
import gradio as gr
# import urllib.parse
import shutil
# app = FastAPI()

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
   
    # return demo.launch(root_path="/wav2lip", server_port=9005, server_name='0.0.0.0')

# query_string = request.query_params
# ipfscid = query_string.get('ipfscid', None)
# if not ipfscid:
#     raise HTTPException(status_code=400, detail="ipfscid query parameter is required")

# download_ipfs_folder(ipfscid, "inputs")

with gr.Blocks() as demo:
    gr.Label("Audio Face", show_label=False)
    with gr.Row():
        with gr.Column():
            audio_file = gr.File(label="Upload MP3 Audio File" )
        with gr.Column():
            video_file = gr.Video(label="Video Input")
        with gr.Column():
            output_video = gr.Video(label="Result Video", format="mp4")
    animate_btn = gr.Button("Animate")
    
    def generate_lipsync_video(audio_file, video_file):
      
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_name = f"inputs/lipsynced_result_{timestamp}.mp4"
        command = (
            f"python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth "
            f"--segmentation_path checkpoints/face_segmentation.pth "
            f"--sr_path checkpoints/esrgan_yunying.pth --resize_factor 3 "
            f"--face {video_file} --audio {audio_file} --outfile {output_name} --no_sr"
        )
        execute_command(command)

        os.makedirs("/outputs", exist_ok=True)
        shutil.copy(output_name, "/outputs/output.mp4")
        return output_name
    
    animate_btn.click(fn=generate_lipsync_video, inputs=[audio_file, video_file], outputs=output_video, api_name="animate")

def execute_command(command: str) -> None:
    os.system(command)

# @app.middleware("http")
# async def add_ipfs_folder(request: Request, call_next):
#     query_string = request.query_params
#     print(query_string)
#     ipfscid = query_string.get('ipfscid', None)
#     print(ipfscid)

#     # if not ipfscid:
#     #     raise HTTPException(status_code=400, detail="ipfscid query parameter is required")

#     if ipfscid:
#       download_ipfs_folder(ipfscid, "inputs")
#     response = await call_next(request)
#     return response

if __name__ == "__main__":
    if os.getenv("IPFS"):
        download_ipfs_folder(os.getenv("IPFS"), "inputs")
        generate_lipsync_video("inputs/input2.mpeg", "inputs/input1.png")
    else:
        demo.launch( server_port=8000, server_name='0.0.0.0')  
    #   import uvicorn
    #   gr.mount_gradio_app(app,demo,"/")
    #   uvicorn.run(app, host="0.0.0.0", port=8000)