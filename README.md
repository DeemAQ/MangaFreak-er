# MangaFreak-er
Python script to download manga in bulk from [Manga Freak](https://w12.mangafreak.net/).

Requirements:

imutils

requests

`pip install -r requirements.txt`

1. Run the script:

`python3 download_manga.py`

2. It will ask you to enter the manga name, this will be used for the file names
3. For the base URL, simply go to the site you want to download from and copy one of the download links \*

\* this will only work if the links of the manga are the same and only differ in the number at the end

![Copying link](/images/link.jpg)
for example: http://images.mangafreak.net:8080/downloads/MangaName_1

Now delete the number, but leave the underscore! like this: http://images.mangafreak.net:8080/downloads/MangaName_

4. Enter the number of chapter you want to download from
5. Enter the number of chapter you want to dowload to
6. Enter the extension of the files you're downloading 
![Extension of the file](/images/extension.jpg)

7. Enter the path of the directory you want to download to (Linux style only!), or it will create a folder with a name you choose in the directory the script is in
8. Enjoy!

This is a very simple script with many assumptions and basic error handling so use manga freak for best results
