import os
import socket

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    hostname = socket.gethostname()

    env_vars = "<br>".join(f"{key}: {value}" for key, value in os.environ.items())

    html_content = f"""
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: "Roboto", sans-serif;
                background-color: {os.getenv("BACKGROUND_COLOR", "white")};
                margin: 20px;
                padding: 0;
            }}
        </style>
    </head>
    <body>
        <h1>Hello Docker 🐋</h1>
        <p><b>Hostname</b>: {hostname}</p>
        <p><b>Environment Variables</b>:</p>
        <pre>{env_vars}</pre>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
