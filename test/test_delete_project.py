from model.project import Project
import random
import pytest


def test_delete_project(app, json_projects):
    project = json_projects
    app.session.auth("administrator", "root")
    if app.project.count() == 0:
        app.project.create(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects