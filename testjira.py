# #/usr/bin/python
# import jira.client
# from jira.client import JIRA
#
# options = {'server': 'https://monetizemore.atlassian.net' }
# jira_login = JIRA(options, basic_auth=('eko@monetizemore.com', 'Bismillah101'))
# projects = jira_login.projects()
#
#
#
# # print(projects)
# # #
# # for project in projects:
# #     # issues = jira_login.search_issues('project=key=EFS' + project.key)
# #     # issues = jira_login.search_assignable_users_for_issues('eko@monetizemore.com')
# #     issues = jira_login.search_assignable_users_for_projects(username='eko@monetizemore.com', projectKeys='EFS')
# #     for issue in issues:
# #         print(issue)
#



from jira import JIRA

jira = JIRA(basic_auth=('eko@monetizemore.com', 'Bismillah101'), options={'server':'https://monetizemore.atlassian.net'})

issue = jira.issue('EFS-276')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)
print(issue.fields.summary)
print(issue.fields.comment.comments)
print(issue.fields.labels)