#!/bin/bash

# To create a new role using this skeleton fill variables and run this script. Remove this file after role creation.

# This variable ideally should contain the name of an application which will be deployed with ansible role.
# Do not use whitespaces.
APPLICATION=""

# Role description
DESCRIPTION=""

# Your name. Preferably your full name. (Ex: Dmitry Ibragimov)
AUTHOR=""

rm -rf .git
rm README.md
mv README.sample.md README.md

# Replace all variables to defined
find ./ -type f -exec sed -i "s/SKELETON_AUTHOR/$AUTHOR/g" {} \;
find ./ -type f -exec sed -i "s/SKELETON_APPLICATION_DESCRIPTION/$DESCRIPTION/g" {} \;
find ./ -type f -exec sed -i "s/SKELETON_APPLICATION/$APPLICATION/g" {} \;