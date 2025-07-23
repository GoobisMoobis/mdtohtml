import sys
import markdown
import webbrowser
import os
import http.server
import socketserver
import threading
import time
from urllib.parse import urlparse

def convert_md_to_html(md_path):
    if not os.path.exists(md_path):
        print(f"File not found: {md_path}")
        return
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_body = markdown.markdown(md_text)
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Markdown Preview</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css">
        <style>
            body {{
              font-family: Arial, sans-serif;
              line-height: 1.6;
              max-width: 800px;
              margin: 0 auto;
              padding: 20px;
            }}
            pre {{
              background-color: #f6f8fa;
              border-radius: 3px;
              padding: 16px;
              overflow: auto;
            }}
            code {{
              font-family: 'Consolas', 'Monaco', monospace;
              padding: 0.2em 0.4em;
              border-radius: 3px;
              background-color: #f6f8fa;
            }}
            pre code {{
              padding: 0;
              background-color: transparent;
            }}
            blockquote {{
              border-left: 4px solid #ddd;
              padding-left: 1em;
              margin-left: 0;
              color: #666;
              background-color: #f9f9f9;
              padding: 1%;
              overflow: hidden;
            }}
        </style>
    </head>
    <body>{html_body}</body>
    </html>
    """
    
    # Create an HTTP server
    class SingleRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
    
    # Port
    port = 8000
    while True:
        try:
            with socketserver.TCPServer(("", port), SingleRequestHandler) as httpd:
                # Start server
                server_thread = threading.Thread(target=httpd.serve_forever)
                server_thread.daemon = True
                server_thread.start()
                
                # Open browser
                webbrowser.open(f"http://localhost:{port}")
                
                # Shut down the server after 2 seconds
                time.sleep(2)
                httpd.shutdown()
                break
        except OSError:
            port += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No file provided.")
    else:
        convert_md_to_html(sys.argv[1])
