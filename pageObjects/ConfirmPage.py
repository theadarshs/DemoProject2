from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    Country=(By.ID,"country")
    Click=(By.LINK_TEXT,"India")
    Checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    SubmitButton=(By.CSS_SELECTOR,"[type='submit']")

    def GetCountry(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def GetClick(self):
        return self.driver.find_element(*ConfirmPage.Click)

    def GetCheckbox(self):
        return self.driver.find_element(*ConfirmPage.Checkbox)

    def GetSubmit(self):
        return self.driver.find_element(*ConfirmPage.SubmitButton)