import gradio as gr
# import ipfshttpclient
# import subprocess
# import time
# import download_ipfs_folder 
from ipfs import download_ipfs_folder
# Start the IPFS daemon
# def start_ipfs_daemon():
#     process = subprocess.Popen(['ipfs', 'daemon'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     time.sleep(5)  # Give the daemon some time to start
#     return process

# Retrieve content from IPFS
# def get_ipfs_content(ipfs_hash):
#     # client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
#     content = client.cat(ipfs_hash)
#     return content.decode('utf-8')

# Gradio function
def greet(name):
    ipfs_hash = "QmNNZaVZsrnSmVQqEUZGYotFHCday6eCM8DbiVeVqgXtLe"
    download_ipfs_folder(ipfs_hash, "inputs")
    ipfs_content = "test" #get_ipfs_content(ipfs_hash)
    return f"Hello, {name}! Here is the content from IPFS: {ipfs_content}"

# Start the IPFS daemon
# ipfs_daemon_process = start_ipfs_daemon()

# Gradio interface
iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Enter your name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Greeting App",
    description="A simple Gradio app that greets the user and shows content from IPFS."
)

if __name__ == "__main__":
    # try:
    iface.launch()
    # finally:
        # ipfs_daemon_process.terminate()  # Ensure the IPFS daemon is terminated when the app stops