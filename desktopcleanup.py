# Files to the left, Folders to the right
import os
import winshell
import shutil

UserDesktop = winshell.desktop()
LeftSide = os.path.join(UserDesktop, 'Files')
RightSide = os.path.join(UserDesktop, 'Folders')

if not os.path.exists(LeftSide):
    os.makedirs(LeftSide)
if not os.path.exists(RightSide):
    os.makedirs(RightSide)

# scandir scans files from a directory
for file in os.scandir(UserDesktop):
    if not file.is_dir():
        shutil.move(file, LeftSide)

    if file.name == 'Files' or file.name == 'Folders' or file.name == 'Python':
        pass
    elif file.is_dir():
        shutil.move(file, RightSide)

input('Finished. Press Anything to Close')
