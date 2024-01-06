from model.project import Project
import random
import pytest


def test_delete_project(app, json_projects):
    username = "administrator"
    password = "root"
    app.session.auth(username, password)
    project = json_projects
    if app.project.count() == 0:
        app.project.create(project)
    #old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    #new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects