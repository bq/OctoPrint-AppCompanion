# coding=utf-8
from __future__ import absolute_import

__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2015 The OctoPrint Project - Released under terms of the AGPLv3 License"

import octoprint.plugin

class AndroidAppCompanionPlugin(octoprint.plugin.AppPlugin):
	def get_additional_apps(self):
		return [
		    ("com.bq.octoprint.android", "any", "MEgCQQCeKGed46mFCedlMEhPSTTTta/vFAYIxl+Y0YZmMCd3ClsDUA0vr3HskhGYP+Jjij69FlMYGVnIzKTozabaiQQNAgMBAAE=")
		]

__plugin_name__ = "Android App Companion"
__plugin_version__ = "0.1"
__plugin_implementations__ = [AndroidAppCompanionPlugin()]

