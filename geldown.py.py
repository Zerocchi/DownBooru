from bs4 import BeautifulSoup
import os
import sys
import time
import urllib

tags = raw_input("Enter tags: ").strip()
limit = raw_input("Enter limit: ")

url = "http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags={}&limit={}".format(tags,limit)

r = urllib.urlopen(url).read()
soup = BeautifulSoup(r)

links = {}

for post in soup.findAll('post'):
	post_attrs = dict(post.attrs)
	url = post_attrs['file_url']
	id = post_attrs['id']
	links[id] = url

def reporthook(count, block_size, total_size):
	    global start_time
	    if count == 0:
		start_time = time.time()
		return
	    duration = time.time() - start_time
	    progress_size = int(count * block_size)
	    speed = int(progress_size / (1024 * duration))
	    percent = min(int(count * block_size * 100 / total_size),100)
	    if (progress_size / 1024) < 1024: 
	    	progress_size = str(progress_size / (1024)) + " KB downloaded"
	    else:
	    	progress_size = str(progress_size / (1024 * 1024)) + " MB downloaded"
	    sys.stdout.write("\r%d%%, %s, %d KB/s, %d seconds passed" %
			    (percent, progress_size, speed, duration))
	    sys.stdout.flush()

def save(url, filename):
	newpath = r'C:\Users\Zero\Desktop\{}'.format(tags).split("+")[0]  
	if not os.path.exists(newpath):	# if folder not exists, create new folder based on tags name
		os.makedirs(newpath)
	os.chdir(newpath)
	if os.path.isfile(filename):
		print "\rFile already exists"
	else:
		urllib.urlretrieve(url, filename, reporthook)
		print

if __name__ == '__main__':
	for each in links:
		try:
			save(links[each], each + "." + links[each].split(".")[-1])
		except urllib.ContentTooShortError:
			print "\nDownload incomplete. Please try again."
		
