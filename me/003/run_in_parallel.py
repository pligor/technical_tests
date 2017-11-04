from multiprocessing import Process

def runInParallel(*fns):
    """https://stackoverflow.com/a/7207336/720484"""
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()