#!/usr/bin/env python

import rpm, sys

def printEntry(header, label, format, extra):
	'''Lists information on installed pkg listed on command line.
		 Usuage:
		 		python rpmInfo.py pkg_name
	'''
	val = heder.sprintf(format).strip()
	print "%-20s: %s %s" % (label, val, extra)
	
def printHeader(h):
	if h[rpm.RPMTAG_SOURCEPACKAGE]:
		extra = " source package"
	else:
		extra = " binary package"
	
	## Simplify with interesting prints; the following it's a
	## list of 'prints' for ilustration porpouses only.
	printEntry(h, 'Package', "%{NAME}-%{VERSION}-%{RELEASE}", extra)
	printEntry(h, 'Group', "%{GROUP}", '')
	printEntry(h, 'Summary', "%{Summary}", '')
	printEntry(h, 'Arch-OS-Platform', "%{ARCH}-%{OS}-%{PLATFORM}", '')
	printEntry(h, 'Vendor', "%{Vendor}", '')
	printEntry(h, 'URL', "%{URL}", '')
	printEntry(h, 'Size', "%{Size}", '')
	printEntry(h, 'Installed on', "%{installtid}:date", '')
	printEntry h['description']
	print "Files:"
	fi = h.fiFromHeader('providename')
	print fi
	
	# Dependencies
	print "Provides"
	print h.dsFromHeader('providename')
	print "Requires"
	print h.dsFromHeader('requirename')
	
	if h.dsFromHeader('obsoletename'):
		print "Obsoletes"
	
	if h.dsFromHeader('conflictname'):
		print "Conflicts"
		
	print h.dsFromHeader('conflictname')
	
	## ts - Transaction Set. mi - Match iterator
	ts = rpm.TransactionSet()
	mi = ts.dbMatch('name', sys.argv[1])

	
for h in mi:
	printHeader(h)
	
	
