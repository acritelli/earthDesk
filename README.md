I made this script as a way to download images from /r/earthporn while learning Python. It's just a fun project that I used as a pedagogical tool. I'm sure there's a way to one-line this entire thing in Bash or Perl, but I wanted to learn Python.

Currently, the script downloads the /r/earthporn page and scrapes it for post URLs. It then downloads every image (ending in .jpg or .png) and every Imgur image link. It does not handle Flickr or Imgur albums (though I want to make this work in the future).

The script can be tailored to your needs by changing the save path and making it a scheduled job on your system. Combine this with a simple script that deletes older images in your desktop background folder, and you've got an easy way to always have fresh desktops.