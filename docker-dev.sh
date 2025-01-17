    #!/bin/bash
    if ! ipfs config show > /dev/null 2>&1; then
        ipfs init
        ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["https://webui.ipfs.io", "http://webui.ipfs.io.ipns.localhost:8080", "https://tauri.localhost", "http://localhost:5001"]'
    fi
    ipfs daemon &
    until curl -s http://127.0.0.1:5001/webui > /dev/null; do
        sleep 1
    done
    cd src
    watchmedo auto-restart --patterns=*.py --recursive -- python .
