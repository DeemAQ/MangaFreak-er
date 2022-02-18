"""@Deem_Alqud 2022"""
from imutils import paths
import requests
import os


# necessary inputs
manga_name = input("Enter the name of the manga\n")
manga_name = manga_name.replace(" ", "-")
base_url= input("Enter the base URL for downloads, possible example: http://website-name.com:port/downloads/manga-name-\n")

chptr_start = input("From which chapter you want to download? -numbers only-\n")
chptr_end = input("To which chapter you want to download? -numbers only-\n")
if not chptr_start.isdigit() or not chptr_end.isdigit():
	print("Not an Integer!")
	exit()


extension = input("Enter the file extension, .zip, .7z, .pdf, etc...\n")
if '.' not in extension:
	extension = "."+extension


output_folder = input("Enter the path of the folder you want to save to\n")
if not os.path.exists(output_folder):
	create_dir = input("path incorrect, want to create a new one in the current directory? (y)es/(n)o\n").lower()
	if "y" in create_dir:
		output_folder = input("choose a folder name\n")
		os.mkdir(output_folder)
	else:
		exit()


with open('urls.txt', 'w') as f:
    for i in range(int(chptr_start), int(chptr_end)+1):
        f.write(f'{base_url}{i}\n')


# grab the list of URLs from the input file, then initialize the total number of manga downloaded so far
rows = open('urls.txt', 'r').read().strip().split("\n")
total = 1


# loop the URLs
for url in rows:
	try:
		# try to download
		r = requests.get(url, timeout=60)

		# save to disk
		p = os.path.sep.join([output_folder, "{}{}".format(manga_name+str(total), extension)])
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		# update the counter
		print("[SUCCESS] downloaded: {}".format(p))
		total += 1

	# handle if any exceptions are thrown during the download process
	except:
		print("[FAILED] error downloading {}...skipping".format(p))

