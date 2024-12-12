#!/usr/bin/env python

import myBuild
import unittest

class knownRightCmds(unittest.TestCase):
	
	Right_Cmds = (("ssh cloud_user@192.168.122.105 'ls -l ~/rpmbuild/RPMS/'", "OK"),
								(, ),
								(, ),
								(, ),
								(, ),
								(, ),
								(, ),
								(, ),
								(, ))
								
								
	def test_cloud_user_right_cmd(self):
		'''App should return right output.'''
		for cmd_connect, cmd_string in self.Right_Cmds:
			result = myBuild.cmd_type_list()
			self.assertEqual(some_var_toCompare, result)
			
	def test_constructor_forms_right_cmd(self):
		'''Constructor should return valid cmd.'''
		for connect_cmd, remote_cmd in self.Right_Cmds:
			result = myBuild.constructor_cmd(user)
			self.assertEqual(some_var_toCompare, result)


			
if __name__ == '__main__':
	unittest.main()
