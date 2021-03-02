# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "immigration"
app_title = "Immigration"
app_publisher = "FinByz Tech Pvt Ltd"
app_description = "Custom App"
app_icon = "octicon octicon-education"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "GPL 3.0"


doctype_js = {
	"Program": "public/js/doctype_js/program.js",
	"Branch": "public/js/doctype_js/branch.js",
}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/immigration/css/immigration.css"
# app_include_js = "/assets/immigration/js/immigration.js"

# include js, css files in header of web template
# web_include_css = "/assets/immigration/css/immigration.css"
# web_include_js = "/assets/immigration/js/immigration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "immigration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "immigration.install.before_install"
# after_install = "immigration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "immigration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Branch":{
		"onload": "immigration.immigration.doc_events.branch.onload",
		"on_trash": "immigration.immigration.doc_events.branch.on_trash"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"immigration.tasks.all"
# 	],
# 	"daily": [
# 		"immigration.tasks.daily"
# 	],
# 	"hourly": [
# 		"immigration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"immigration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"immigration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "immigration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "immigration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "immigration.task.get_dashboard_data"
# }

