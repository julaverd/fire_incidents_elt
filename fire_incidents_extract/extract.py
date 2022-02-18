import requests
import os

class Extract:
    def __init__(self):
        self._incidents_url = 'https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD'
        self._destination_path = 'data'
        self._destination_file = 'Fire_Incidents.csv'

    def read_source(self):
        self._req = requests.get(self._incidents_url, allow_redirects=True)
        if self._req.status_code == 200:
            self._extracted_dest = os.path.join(self._destination_path, self._destination_file)
            print(self._extracted_dest)
            with open(self._extracted_dest, 'wb') as writer:
                writer.write(self._req.content)
        return self._req.status_code