

## when is it best to use #nodejs 
- not:
	- video processing
	- ML
		- these are blocking ops 
	- possible but no advantage over other languages/runtimes
- very good for #servers:
	- querying data
	- when main performance problem is input/output rather than calculations
	- eg Netflix uses node to send video files from DB to client