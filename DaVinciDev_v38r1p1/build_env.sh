# Search path defined from lb-dev command line
if [ -z "$User_release_area" ] ; then
  # use a default value
  export User_release_area="/home/hep/ss4314/cmtuser"
fi
export CMTPROJECTPATH="${User_release_area}${CMTPROJECTPATH:+:${CMTPROJECTPATH}}"
