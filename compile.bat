pip install pipenv
pipenv install
pipenv shell
:: 以下代码需要手动复制粘贴执行（去掉前面冒号）：

:: pip install yt-dlp
:: pip install pyinstaller
:: pip install ttkthemes

:: 生成单个可执行文件exe
:: pyinstaller -F --onefile .\yt-dlp-simple-gui.py -i download_icon.ico --paths C:\users\dell\appdata\local\programs\python\python310\lib\site-packages\yt-dlp,websockets,pycryptodomex,brotli,certifi,mutagen,ttkthemes,pillow --clean

:: 生成文件目录（可打包成zip）
:: pyinstaller -F --onedir .\yt-dlp-simple-gui.py -i download_icon.ico --paths C:\users\dell\appdata\local\programs\python\python310\lib\site-packages\yt-dlp,websockets,pycryptodomex,brotli,certifi,mutagen,ttkthemes,pillow --clean

:: 将UPX.exe 复制到pyinstaller.exe同文件夹下
:: 修改pyinstaller产生的.spec文件，将upx=False改成upx=True，然后手动执行以下代码：

:: (若已为True, 则跳过此行)
:: pyinstaller yt-dlp-simple-gui.spec 

:: pipenv --rm
:: exit