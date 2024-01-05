from model.project import Project
import pytest


def test_add_project(app, json_projects):
    app.session.auth("administrator","root")
    old_projects = app.project.get_project_list()
    project = json_projects
    n=0
    for old_project in old_projects:
        if project.name == old_project.name:
            n+=1
            continue
    if (n>0):
        print("Группа не добавлена")
    else:
        app.project.create(project)
        new_projects = app.project.get_project_list()
        old_projects.append(project)
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
