build:
	docker-compose build torrents

download:
	docker-compose run torrents python seq_download_torrents.py