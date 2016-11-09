#!/bin/bash - 
#===============================================================================
#
#          FILE: gitpush.sh
# 
#         USAGE: ./gitpush.sh 
# 
#   DESCRIPTION: Push and commit to github
# 
#        AUTHOR: TraiOi, 
#       CREATED: 11/09/2016 18:06
#===============================================================================

set -o nounset                              # Treat unset variables as an error
git add *
git commit -m "Updated $1"
git push

