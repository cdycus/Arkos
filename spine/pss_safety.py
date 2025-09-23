import threading

class SwarmTimeoutException(Exception):
    pass

def run_with_timeout(func, timeout_sec=0.5, *args, **kwargs):
    result = {}
    def wrapper():
        try:
            result['value'] = func(*args, **kwargs)
        except Exception as e:
            result['error'] = e

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout_sec)
    if thread.is_alive():
        raise SwarmTimeoutException("Swarm foresight timed out")
    if 'error' in result:
        raise result['error']
    return result.get('value', None)