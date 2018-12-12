#!/usr/bin/env python

import urllib
import settings

def cleanTags(name):
    while "<" in name or ">" in name:
        i = name.find("<")
        j = name.find(">")
        name = name[:i]+name[j+1:]
    return name

def grabnos():
    handle = urllib.urlopen(settings.dec_url)

    nosstarted = False
    nextno = False
    noinprogress = False
    id = []
    names = []
    k=0

    for line in handle:
        k+=1
        if "<tr class=titlerow>" in line:
            nosstarted = True
            continue
        if "</tr>" in line and nosstarted:
            noinprogress = False
            nextno = True
            continue
        if "<tr class=tyesrow>" in line and nextno:
            noinprogress = True
            nextno = False
            continue
        if "http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases" in line and noinprogress:

            id += [int(line.partition("</a>")[0].partition("py>")[2])]
        if "<a href=https://svnweb.cern.ch/trac/lhcb/browser/DBASE/tags/Gen/DecFiles/" in line and noinprogress:
            line = line.partition("<b>")[2]
            while not line.find("<br>") == -1:
                name = line.partition("<br>")[0].strip()
                names +=[cleanTags(name)]
                line = line.partition("<br>")[2]

    return zip(id,names)

def grabobs():
    obsnos = []

    handle = urllib.urlopen(settings.obs_url)
    for line in handle:
        obsnos+=[line.partition("EVTTYPEID = ")[2].partition(", DESCRIPTION ")[0]]
    return obsnos

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def grabcuts():
    cuts = []
    revs = []

    handle = urllib.urlopen(settings.cuts_url)
    for line in handle:
        if ".cpp" in line:
            line = line.partition("</a>")[0]
            line = line.rpartition(">")[2]
            line = line.partition(".cpp")[0]
            cuts+=[line]

    for cut in cuts:
        if is_number(cut):
            cuts.remove(cut)
            revs+=[cut]

    return cuts

def grabIdToName():
    dict = {}

    handle = urllib.urlopen(settings.table_url)

    skip = True
    for line in handle:
        if skip:
            skip = False
            continue
        if "end" in line:
            break
        if line[0]=='*':
            continue
        line = line.split()
        dict[line[4]] = line[3]

    return dict

if __name__ == "__main__":
    nos = grabnos()
    for no in nos:
        print no
    print grabobs()
    print grabcuts()
    print grabIdToName()
