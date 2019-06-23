import time
import csv
from selenium import webdriver


USER_NAME = ''
PASSWORD = ''


class Company:
    def __init__(self, name, profile, link):
        self.name = name
        self.profile = profile
        self.link = link
        self.base = ""
        self.ctc = ""
        self.monthly = ""


    def getname(self):
        return self.name

    def getprofile(self):
        return self.profile

    def getlink(self):
        return self.link

    def getbase(self):
        return self.base

    def getctc(self):
        return self.ctc

    def getmonthly(self):
        return self.monthly

    def setctc(self, ctc):
        self.ctc = ctc

    def setbase(self, base):
        self.base = base

    def setmonthly(self, monthly):
        self.monthly = monthly

def fetchCompanies():
    listOfCompanies = list()
    url = "https://online.iitg.ernet.in/tnp/student/job_all_list.jsp?"
    driver = webdriver.Chrome('D:\Downloads\chromedriver')
    driver.get(url)
    username = driver.find_element_by_name( "username")
    username.send_keys(USER_NAME)

    password = driver.find_element_by_name( "password")
    password.send_keys(PASSWORD)

    print(username)
    print(password)

    login = driver.find_element_by_tag_name('button')

    time.sleep(1)

    login.click()

    url = "https://online.iitg.ernet.in/tnp/student/job_all_list.jsp?"

    time.sleep(4)

    driver.get(url)
    time.sleep(4)

    job_table = driver.find_element_by_class_name('taable-responsive')
    job_table_body = job_table.find_element_by_tag_name('tbody')
    job_rows = job_table_body.find_elements_by_tag_name('tr')

    for r in job_rows:
        job_elements = r.find_elements_by_tag_name('td')
        comp_name = job_elements[1].text
        comp_profile = job_elements[3].text
        link = job_elements[5].find_element_by_tag_name('a')
        link_id = link.get_attribute('href')
        comp = Company(comp_name, comp_profile, link_id)
        listOfCompanies.append(comp)

    for comp in listOfCompanies:
        link = comp.getlink()
        driver.get(link)
        salary_details = driver.find_element_by_id('Salary_Details')
        salary_table = salary_details.find_element_by_class_name('table-bordered')
        rows = salary_table.find_elements_by_tag_name('tr')
        columns = rows[2].find_elements_by_tag_name('td')
        comp.setctc(columns[1].get_attribute("innerHTML"))
        comp.setbase(columns[2].get_attribute("innerHTML"))
        comp.setmonthly(columns[3].get_attribute("innerHTML"))

    for comp in listOfCompanies:
        print(comp.getname(), comp.getprofile(), comp.getctc(), comp.getbase(), comp.getmonthly())

    with open('comp.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['Name', 'Profile', 'CTC', 'BASE', 'MONTHLY'])
        for comp in listOfCompanies:
            writer.writerow([comp.getname(), comp.getprofile(), comp.getctc(), comp.getbase(), comp.getmonthly()])

    driver.close()


if __name__ == '__main__':
    fetchCompanies()
