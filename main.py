import speedtest # pip3 install speedtest-cli

test = speedtest.Speedtest()

test.get_servers()  # gets list of servers
print("Chosing best server..........")
best = test.get_best_server() # choses the best server
print(f"Found : {best['host']} Located in {best['country']}")
print("===================================================")
print(f"Complete Details of server: {best}")
print("===================================================")

print("Performing Download Test.......")
download_result = test.download()
print("Performing Uplode Test.......")
uplode_result = test.upload()
ping_result = test.results.ping

print("===================================================")
print(f"Download Speed: {download_result / 1024 / 1024:.2f} MBit/s")
print(f"Upload Speed: {uplode_result / 1024 / 1024:.2f} MBit/s")
print(f"Ping: {ping_result:.2f}  MS")