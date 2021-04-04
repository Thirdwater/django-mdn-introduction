freeze:
	# See https://stackoverflow.com/a/40167445/ for errors with pkg-resources
	pip freeze | grep -v "pkg-resources" > requirements.txt