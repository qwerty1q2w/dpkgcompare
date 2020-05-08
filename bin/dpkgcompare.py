#!/usr/bin/env python3
import sys,splunk.Intersplunk
import string
##### CHANGE PATH TO your distribution FIRST ###########
sys.path.append("/usr/lib/python3/dist-packages")
import apt_pkg

string1=sys.argv[1]
string2=sys.argv[2]

results = []
apt_pkg.init_system()
try:

    results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

    for r in results:
        if "_raw" in r:
            compare_result=apt_pkg.version_compare(r[string1], r[string2])
            r["compare_result"]=compare_result

except:
    import traceback
    stack =  traceback.format_exc()
    results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))
    print(str(stack))
splunk.Intersplunk.outputResults(results)
