http_server = "https://example.com" # This is used for generating the link - replace with your own server

# This is used for connecting to the server and uploading files - replace with your own server and credentials
server = 'ftp.example.com'
username = 'your_username'
password = 'your_password'

from random import randint
from ftplib import FTP
import os

def upload_folder(ftp, local_folder): # Function for uploading folders
    for item in os.listdir(local_folder):
        local_item = os.path.join(local_folder, item)
        if os.path.isfile(local_item):
            with open(local_item, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
        elif os.path.isdir(local_item):
            ftp.mkd(item)
            ftp.cwd(item)
            upload_folder(ftp, local_item)
            ftp.cwd('..')

def create_remote_folder(ftp, folder_path): # Create folders if they don't exist
    if folder_path in ftp.nlst():
        return

    ftp.mkd(folder_path)


link = input("Put in roblox deeplink: ") # Ask link for the button on the HTML page

# Load files into RAM
with open("html/main.js") as f:
    js = f.read()
with open("html/index.html") as f:
    html = f.read()
with open("html/main.css") as f:
    css = f.read()

# Modify HTML + JavaScript
js = js.replace("ROBLOXDEEPLINKPUTHERE", link)
html = html.replace("ROBLOXDEEPLINKPUTHERE", link)

# Generate folder
folder = str(randint(1000000000,9999999999))

# Show link for copying
print(f"\n\n{http_server}/invite/{folder}")

# Make temporary files for uploading
os.mkdir(folder)
with open(f"{folder}/main.js", "w") as f:
    f.write(js)
with open(f"{folder}/index.html", "w") as f:
    f.write(html)
with open(f"{folder}/main.css", "w") as f:
    f.write(css)

# Connect to FTP server and upload files
with FTP(server) as ftp:
    # Log in
    ftp.login(username, password)
    ftp.cwd('/htdocs/')
    create_remote_folder(ftp, "invite") # Create folder if it doesn't exist
    ftp.cwd('/htdocs/invite/')
    create_remote_folder(ftp, folder)
    ftp.cwd(f'/htdocs/invite/{folder}')
    upload_folder(ftp, folder)

# Remove temporary folders
for item in os.listdir(folder):
    local_item = os.path.join(folder, item)
    os.remove(local_item)
os.rmdir(folder)

# Input for when you double click to run so it doesn't close instantly
input("\n\nPress enter to close")