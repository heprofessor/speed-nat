import speedtest

def get_speed():

    test = speedtest.Speedtest()

    download_speed = test.download() / 10**6

    upload_speed = test.upload() / 10**6

    return f"Download Speed: {download_speed} Mbps, Upload Speed: {upload_speed} Mbps"

print(get_speed())
