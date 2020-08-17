from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# The ID of a sample document.
DOCUMENT_ID = '10ti6boIneCzlgaynLWV8ApedpAOrlFDP67g0tNEks_s'

LOCAL_FILENAME_HTML = "resume.html"
LOCAL_FILENAME_PDF = "resume.pdf"


def get():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    requesthtml = service.files().export_media(fileId=DOCUMENT_ID,
                                           mimeType="text/html")

    requestpdf = service.files().export_media(fileId=DOCUMENT_ID,
                                           mimeType="application/pdf")

    download_request(requesthtml, LOCAL_FILENAME_HTML)
    download_request(requestpdf, LOCAL_FILENAME_PDF)

    return LOCAL_FILENAME_HTML


def download_request(request, filename):
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    with open(filename, "wb") as f:
        f.write(fh.getvalue())
        f.close()
