#!/bin/env python
#
# python module to determine the core distribution for CSS
#
# 6-12-2014 Orvedahl R.
#

import sys
import getopt

def cores(nr, nt, np, all_12, all_16, half_phi, half_theta, calc_cores):

    # something was not passed
    if (nr < 0 or nt < 0 or np < 0):
        nr = int(raw_input("\n\tEnter nr: "))
        nt = int(raw_input("\tEnter nt: "))
        np = int(raw_input("\tEnter np: "))
        print

    # get nn? using 12
    if (all_12):
        nnr = nr / 12.
        nnt = nt / 12.
        nnp = np / 12.
    # get nn? using 16
    elif (all_16):
        nnr = nr / 16.
        nnt = nt / 16.
        nnp = np / 16.
    # calculate cores and nodes
    elif (calc_cores):
        nnr = int(raw_input("\n\tEnter nnr: "))
        nnt = int(raw_input("\tEnter nnt: "))
        nnp = int(raw_input("\tEnter nnp: "))
        print
    # get nn? using a mix (default)
    else:
        nnr = nr / 16.
        nnt = nt / 16.
        nnp = np / 12.

    # articficially lower theta and/or phi
    if (half_theta):
        nnt /= 2

    if (half_phi):
        nnp /= 2

    # get number of cores and number of nodes
    ncores = nnr*nnt*nnp
    nnodes = ncores / 12.

    # report
    print "\nGlobal Resolution:"
    print "\tnr: "+str(nr)+" (total grid pts)"
    print "\tnt: "+str(nt)+" (total grid pts)"
    print "\tnp: "+str(np)+" (total grid pts)"
    print "\nSub-Domains:"
    print "\tnnt: "+str(nnt)+" --> grid pts/subdomain: "+str(nt/nnt)
    print "\tnnp: "+str(nnp)+" --> grid pts/subdomain: "+str(np/nnp)
    print "\tnnr: "+str(nnr)+" --> grid pts/subdomain: "+str(nr/nnr)
    print "\nCore Counts:"
    print "\tn-cores: "+str(ncores)
    print "\tn-nodes: "+str(nnodes)
    print


def usage():

    print "\nPython script to determine how many cores to use with CSS"
    print "  Given a resolution in (r,theta,phi) as nr, nt and np,"
    print "  calculate the number of subdomains to use as nnr, nnt and nnp\n"
    print "Usage:\n"
    print "\t./cores.py [options]\n"
    print "\t--nr=<nr>          Set number of global radial nodes to <nr>\n"
    print "\t--nt=<nt>          Set number of global theta nodes to <nt>\n"
    print "\t--np=<np>          Set number of global phi nodes to <np>\n"
    print "\t--all-12           Calculate all numbers using nn? = n?/12\n"
    print "\t--all-16           Calculate all numbers using nn? = n?/16\n"
    print "\t--half-theta       Cut nnt in half after it is calculated\n"
    print "\t--half-phi         Cut nnp in half after it is calculated\n"
    print "\t--calc-cores       Calc ncores & nnodes given nnt, nnp and nnr\n"
    print "\t-h, --help         Display help message\n"
 
 
if __name__ == "__main__":

    try:
       opts, args = getopt.getopt(sys.argv[1:], "h", ["nr=", "nt=", "np=",
                        "half-phi", "half-theta", "all-12", "all-16",
                        "calc-cores", "help"])

    except getopt.GetoptError:
       print "\n---ERROR: Unknown Command Line Option---\n"
       usage()
       sys.exit(2)

    # defaults
    nr = -1
    nt = -1
    np = -1
    all_12 = False
    all_16 = False
    half_phi = False
    half_theta = False
    calc_cores = False

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("--nr"):
            nr = int(arg)
        elif opt in ("--nt"):
            nt = int(arg)
        elif opt in ("--np"):
            np = int(arg)
        elif opt in ("--all-12"):
            all_12 = True
        elif opt in ("--all-16"):
            all_16 = True
        elif opt in ("--half-theta"):
            half_theta = True
        elif opt in ("--half-phi"):
            half_phi = True
        elif opt in ("--calc-cores"):
            calc_cores = True

    cores(nr, nt, np, all_12, all_16, half_phi, half_theta, calc_cores)

