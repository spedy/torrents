import libtorrent as lt
import time
import sys

streaming = False

ses = lt.session()
ses.listen_on(6881, 6891)


magnet = True

if magnet:
    params = {"save_path": "./"}
    link = "magnet:?xt=urn:btih:3d0ef9c4f15622f63611c26fac2c7be2766d82dd&dn=Die.Hard.1988.720p.BluRay.x264-NeZu&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
    h = lt.add_magnet_uri(ses, link, params)
else:
    info = lt.torrent_info("active.torrent")
    h = ses.add_torrent({'ti': info, 'save_path': './'})

h.set_sequential_download(True)
print('starting' + h.name())

while (not h.is_seed()):
    s = h.status()

    state_str = ['queued', 'checking', 'downloading metadata', \
        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
        (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
        s.num_peers, state_str[s.state]),)
    sys.stdout.flush()

    time.sleep(1)

print(h.name(), 'complete')