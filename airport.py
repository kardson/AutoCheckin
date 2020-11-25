import requests
import sys

def checkin(host, email, passwd):
    sess = requests.Session()
    sess.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
    sess.get(host)
    data = {
        "email": email,
        "passwd": passwd,
        "code": ""
    }
    sess.headers.update({"X-Requested-With": "XMLHttpRequest"})
    sess.headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
    sess.post(host + "/auth/login", data=data)
    sess.get(host + "/user")
    sess.post(host + "/user/checkin")
    return

if __name__ == "__main__":
    checkin(sys.argv[1], sys.argv[2], sys.argv[3])