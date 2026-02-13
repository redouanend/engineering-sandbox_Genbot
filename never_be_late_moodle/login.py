from playwright.sync_api import Page
from playwright_helper import isElementExisting
from playwright_debug import print_dom #we let it in case we need to debug
import keyring
from set_credentials import SERVICE_NAME
import time

def login(page: Page) -> None:
    """
    Connect the user to the Moodle platform
    
    :param page: The page (playwright object) to login on.
    :return: None
    """
    page.locator("text=Connexion").first.click()
    
    """
    If we already get connected there will be a redirection to "/my" 
    We have to check if this redirection happens or not to adapt the script
    We will try at same time interval until the redirection happens or 15 seconds passes
    Note that in case where we are connected there is a first redirection to Microsoft Login page
    (in both cases there is a redirection to Microsoft Login page)

    """
    for _ in range(30):  #15s is a bit overkilled but anyway
        if "moodle.epf.fr/my" in page.url:
            return
        if page.locator("#i0116").count() > 0:
            break
        time.sleep(0.5)
    else:
        return  #We can end the login script since we are already connected

    #Anticipate a brief microsoft page before redirect to /my when already connected
    try:
        page.wait_for_url("**/my/**", timeout=2000)
        return
    except Exception:
        pass
 

    page.locator("#i0116").wait_for(state="visible", timeout=15000)  

    # Check if the email field is present on the page
    if isElementExisting(page, "#i0116"):

        # get email and password from keyring / Setting credentials if not present
        while True:
            email = keyring.get_password(SERVICE_NAME, "email")
            password = keyring.get_password(SERVICE_NAME, "password")
            if email and password:
                break
            else:
                import subprocess
                from pathlib import Path
                import sys
                # === GUI COMPATIBILITY FIX ===
                # Ensures the credentials script is called using an absolute path,
                # avoiding issues when the working directory differs (e.g., GUI launch).
                credentials_script = Path(__file__).resolve().parent / "set_credentials.py"
                subprocess.run([sys.executable, str(credentials_script)])
                # === END FIX ===

        page.locator("#i0116").fill(email)
        
        #Clic on next button
        if isElementExisting(page, "#idSIButton9"):
            page.locator("#idSIButton9").click() 
        else:
            raise RuntimeError("The next button is not present on the page.")

        #Wait for the field password and fill it
        page.locator("#i0118").wait_for(state="visible", timeout=15000)  
        page.locator("#i0118").fill(password)

        #Clic on next button
        if isElementExisting(page, "#idSIButton9"):
            page.locator("#idSIButton9").click() 
        else:
            raise RuntimeError("The next button is not present on the page.")

        # Waits for GUI confirmation instead of terminal input.
        # The event is triggered from the HTML interface via pywebview.
        from gui import api_instance  # we'll expose this instance
        # Signal the GUI that user confirmation is required (2FA / interactive login).
        api_instance._login_required = True
        api_instance.login_event.wait()
        """
        The F2A verification can't be made automatically (Guess it's good news :)
        Because Outlook is sending pop up or wants to write a number
        It's not just a code sent by mail that we could have easily automated
        connecting a SFTP server and reading the mail.
        This part is in standby for now. We have to discuss about 
        what we are going to do.
        """

    else:
        raise RuntimeError("The email field is not present on the page.")

    


