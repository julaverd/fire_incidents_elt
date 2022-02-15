import requests

def read_source():
    incidents_url = 'https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD'  # HardCoded
    r = requests.get(incidents_url, allow_redirects=True)
    if r.status_code == 200:
        destination_path = '../data'
        destination_file = 'Fire_Incidents.csv'
        with open(destination_path +'/'+ destination_file, 'wb') as writer:
            writer.write(r.content)
    return r.status_code

if __name__ == "__main__":
    data = "Reading Fire Incidents from the web.."
    fire_incidents_download = read_source()
    if fire_incidents_download == 200:
        print("Fire Incidents Data successfully read from source!")
    else:
        print("Fire Incidents Data NOT read from source")