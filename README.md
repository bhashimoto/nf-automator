# nf-automator
Automation for importing invoice data and integrating with google sheets

## Scope
This project is limited to invoices from Rio de Janeiro, with no guarantee that it will work with other types of invoices.
Feel free to fork it and adapt it to your use case.


## Requirements
To run this application, you will need the following components:
- [Python](https://www.python.org)
- To download invoices:
    - [Selenium WebDriver](https://selenium-python.readthedocs.io)
    - [Google Chrome](https://google.com/chrome)
- To integrate with google sheets:
    - A Google Account
    - A Google Sheets file
    - Google API Python Client and OAuth lib
        > pip install google-api-python-client
        
        > pip install google-auth-oauthlib

## Setup
### Google Cloud Credentials
With the required libraries installed, you need to setup an application in the google cloud.

Access the [Credentials page](https://console.cloud.google.com/apis/credentials)

Create a new set of credentials by clicking on the **+ CREATE CREDENTIALS** link at the header and selecting OAuth client ID. 
Select **Desktop app** at the dropdown, give it a descriptive name and click **CREATE**.

At the OAuth 2.0 Client IDs, click on the **Download OAuth client** action to download the credentials file. Move it to the project root
and rename it to **credentials.json**.


## Instructions
Run the main.sh file
> ./main.sh [URL for invoice]

If no url is provided, user will be prompted for one.

After scraping the invoice data, if there are no valid credentials, you will be prompted to log into a google account. Proceed to
log in and give necessary confirmations.

If there is no previously registered sheet, you will be prompted to provide a Google Sheets ID, which can be located at the sheet url:
> https://docs.google.com/spreadsheets/d/ **[spreadsheet_id]** /edit

The items will be loaded into the first three columns of the first sheet, starting at the first available row.
