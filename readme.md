This is a simple script to fetch the top post from the earthporn subreddit and
set it as your desktop background.
It uses the reddit api and shouldn't break any of reddit's rules as it only
makes a request once an hour. If you use it, be aware of reddit's rules.

To use this program:
1) Change the user_agent_string in wallpaper_updater.py to something 
unique. Read reddit api rules about this.
2) Place wallpaper_updater.py and wallpaper_updater.sh in /usr/bin/ and 
make 
these file executable. 
3) Place wallpaper_updater.service in /usr/lib/systemd/ and enable it 
with 
systemd. Start the service or restart your system.
4) Set your desktop background to 
~/.wallpaper_updater/wallpaper_updater.jpg.

That should be it.
