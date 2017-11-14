import libtorrent as lt
import time
import sys

streaming = False

ses = lt.session()
ses.listen_on(6881, 6891)


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