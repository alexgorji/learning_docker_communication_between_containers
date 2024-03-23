from flask import Flask
import os
import subprocess

app = Flask(__name__)


@app.route("/copy-files")
def copy_files():
    subprocess.call("/usr/data/copy-to-backup.sh")
    return "Files copied to backup.\n"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
