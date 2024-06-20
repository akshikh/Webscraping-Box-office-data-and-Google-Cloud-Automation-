#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!pip install gspread oauth2client google-api-python-client twilio


# In[1]:


import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from datetime import datetime
from twilio.rest import Client


# In[2]:


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials .from_json_keyfile_name('GS_Cred.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Final Assignment Cloud').sheet1


# In[4]:


#checking if the sheet is working 

val = sheet.cell(1,1).value


# In[5]:


val


# ### Scraping data

# In[10]:


url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_cso_tab"


requests.get(url)


# In[11]:


url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_cso_tab"
dfs = pd.read_html(url)[0]


# In[12]:


dfs


# In[23]:


url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_cso_tab"
dfs = pd.read_html(url)[0]
data = dfs.iloc[0,:]

row = list(data)
row = [str(i) for i in row]
today = str(datetime.today().date())
row = [[today] + row]

sheet.append_rows(row)


# In[22]:


sheet.get_all_values()


# In[24]:


import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import requests

def scrape_and_store(request):
    # Set up Google Sheets API credentials and client
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('GS_Cred.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Final Assignment Cloud').sheet1

    # URL to scrape data from
    url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_cso_tab"

    # Get the data
    response = requests.get(url)
    dfs = pd.read_html(response.content)[0]
    data = dfs.iloc[0, :]

    # Prepare the row to insert into the Google Sheet
    row = list(data)
    row = [str(i) for i in row]
    today = str(datetime.today().date())
    row = [[today] + row]

    # Append the row to the Google Sheet
    sheet.append_rows(row)

    return "Data scraped and stored successfully"


# In[33]:


import session_info
session_info.show()


# In[31]:


import pandas as pd
import requests
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def scrape_top_row():
    # URL to scrape data from
    url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_cso_tab"

    # Get the data
    response = requests.get(url)
    dfs = pd.read_html(response.content)[0]

    # Get the top row (assuming the first row is the latest data)
    top_row = dfs.iloc[0, :]
    data_row = [str(i) for i in top_row]
    today = str(datetime.today().date())
    data_row = [today] + data_row

    return data_row

# Main execution
data_row = scrape_top_row()
print(data_row)

# Function to append data to Google Sheet
def append_to_google_sheet(data_row):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('GS_Cred.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Final Assignment Cloud').sheet1
    sheet.append_row(data_row)

# Append the top row data to Google Sheet
append_to_google_sheet(data_row)
print("Data appended to Google Sheet successfully.")




# In[35]:


#pip show pandas gspread oauth2client requests lxml html5lib beautifulsoup4

