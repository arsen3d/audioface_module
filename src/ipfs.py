import requests
import os
import tarfile

def download_ipfs_folder(cid, output_dir, ipfs_gateway="http://127.0.0.1:5001"):
    """
    Downloads an IPFS folder as a tarball and extracts it locally.

    Args:
        cid (str): The CID of the folder in IPFS.
        output_dir (str): Directory to extract the downloaded folder.
        ipfs_gateway (str): IPFS gateway URL (default: local IPFS daemon).
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # IPFS API endpoint for the 'get' command
    url = f"{ipfs_gateway}/api/v0/get?arg={cid}"
    
    try:
        # Make the request to download the folder
        response = requests.post(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Path to save the downloaded tarball
        tarball_path = os.path.join(output_dir, f"{cid}.tar")
        
        # Save the response content as a tarball
        with open(tarball_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Extract the tarball
        with tarfile.open(tarball_path, "r") as tar:
            # Extract a specific folder from the tarball
            for member in tar.getmembers():
                if member.name.startswith(cid+"/"):
                    member.name = member.name[len(cid)+1:]  # Remove the folder name prefix
                    tar.extract(member, path=output_dir)
        
        # Optionally, delete the tarball after extraction
        os.remove(tarball_path)

        print(f"Folder with CID {cid} has been downloaded and extracted to {output_dir}.")
    except requests.RequestException as e:
        print(f"Failed to download folder from IPFS: {e}")
