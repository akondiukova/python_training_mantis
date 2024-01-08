from model.project import Project
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProjectHelper:

    def __init__(self,app):
        self.app = app

    def create(self, project):
        driver = self.app.driver
        self.open_project_page()
        driver.find_element(By.CSS_SELECTOR,"input[value='Create New Project']").click()
        self.fill_project_form(project)
        driver.find_element(By.CSS_SELECTOR,"input[value='Add Project']").click()

    def open_project_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT,"Manage").click()
        driver.find_element(By.LINK_TEXT,"Manage Projects").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def fill_project_form(self, project):
        driver = self.app.driver
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

        select_status = Select(driver.find_element(By.NAME,'status'))
        select_status.select_by_visible_text("%s" % project.status)

        category = driver.find_element(By.NAME,'inherit_global')
        category.send_keys("%s" % project.global_categories)

        select_view_status = Select(driver.find_element(By.NAME,'view_state'))
        select_view_status.select_by_visible_text("%s" % project.view_status)

    def get_project_list(self):
        driver = self.app.driver
        self.open_project_page()
        project = []
        for element in driver.find_elements(By.CSS_SELECTOR,'.row-1 td a,.row-2 td a'):
            name = element.text
            href = element.get_attribute("href")
            href.startswith("http://localhost/mantisbt-1.2.19/manage_proj_edit_page.php?project_id=")
            id = href[70:]
            project.append(Project(name=name, id=id))
        return project

    def count(self):
        driver = self.app.driver
        self.open_project_page()
        return len(driver.find_elements(By.CSS_SELECTOR, '.row-1 td a,.row-2 td a'))

    def delete_project_by_id(self, id):
        driver = self.app.driver
        self.open_project_page()
        self.select_project_by_id(id)
        driver.find_element(By.CSS_SELECTOR,"input[value='Delete Project']").click()
        if driver.current_url == 'http://localhost/mantisbt-1.2.20/manage_proj_delete.php':
            driver.find_element(By.CSS_SELECTOR,"input[value='Delete Project']").click()
        else:
            print("oops")

    def select_project_by_id(self, id):
        driver = self.app.driver
        for element in driver.find_elements(By.CSS_SELECTOR,'.row-1 td a,.row-2 td a'):
            name = element.text
            href = element.get_attribute("href")
            href.startswith("http://localhost/mantisbt-1.2.19/manage_proj_edit_page.php?project_id=")
            id_css = int(href[70:])
            if id == id_css:
                driver.find_element(By.LINK_TEXT,"%s" % name).click()
                break

    def project_name_is_already_exist(self, project,old_projects):
        return any([old_project.name == project.name for old_project in old_projects])








