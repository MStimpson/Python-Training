from bs4 import BeautifulSoup
import urllib.request
import re
import os
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
os.system('cls')


