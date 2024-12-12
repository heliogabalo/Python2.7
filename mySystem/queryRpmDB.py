#!/usr/bin/env python

import rpm


def queryDB(rpmPkg):
	ts = rpm.TransactionSet()
	matchIterator = ts.dbMatch('name', rpmPkg)

	for header in matchIterator:
		print	"name: {0} version: {1} release: {2}".format(header['name'], header['version'], header['release'])
		
		
#queryDB('dracut')
