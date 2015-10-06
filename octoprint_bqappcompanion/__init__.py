# coding=utf-8
from __future__ import absolute_import

__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2015 Mundo Reader S.L. - Released under terms of the AGPLv3 License"

import octoprint.plugin

class BqAndroidAppCompanionPlugin(octoprint.plugin.OctoPrintPlugin):

	def get_app_key(self, *args, **kwargs):
		return [
			("com.bq.octoprint.android", "any", "MEgCQQCeKGed46mFCedlMEhPSTTTta/vFAYIxl+Y0YZmMCd3ClsDUA0vr3HskhGYP+Jjij69FlMYGVnIzKTozabaiQQNAgMBAAE=")
		]

	def get_update_configuration(self, *args, **kwargs):
		return dict(
			bqappcompanion=dict(
				displayName="BQ Android App Companion Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="bq",
				repo="OctoPrint-AppCompanion",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/bq/OctoPrint-AppCompanion/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "BQ Android App Companion"
def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = BqAndroidAppCompanionPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.accesscontrol.appkey": __plugin_implementation__.get_app_key,
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_configuration
	}
