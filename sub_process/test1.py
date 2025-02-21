import subprocess
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())

""" ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.'] """