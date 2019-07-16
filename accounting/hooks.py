# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accounting"
app_title = "Accounting"
app_publisher = "frappe"
app_description = "An accounting app that will handle sales,purchases,balancing accounts,etc."
app_icon = "octicon octicon-graph"
app_color = "grey"
app_email = "marica@iwebnotes.com"
app_license = "MIT"

treeviews = ['Account']

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accounting/css/accounting.css"
# app_include_js = "/assets/accounting/js/accounting.js"

# include js, css files in header of web template
# web_include_css = "/assets/accounting/css/accounting.css"
# web_include_js = "/assets/accounting/js/accounting.js"

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
# get_website_user_home_page = "accounting.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accounting.install.before_install"
# after_install = "accounting.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accounting.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accounting.tasks.all"
# 	],
# 	"daily": [
# 		"accounting.tasks.daily"
# 	],
# 	"hourly": [
# 		"accounting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accounting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accounting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accounting.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accounting.event.get_events"
# }
