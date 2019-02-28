#!/usr/bin/env sh
#########################################################################
# This file contains cool things that you can achieve with bash scripts #
#########################################################################

#####
##### Variables
#####

# Store a string in a variable
STRING_VARIABLE="string value 1"

# Output a string stored in a variable
echo $STRING_VARIABLE

# Change a string stored in a variable
STRING_VARIABLE="string value 1"

# Use the value of a variable in a template string
echo "The value is: '${STRING_VARIABLE}'"

#####
##### Arrays
#####

# Store values in an array
ARRAY_VARIABLE=( "value 1" "value 2" "value 3" "value 4"
                 "value 5")

# Output each value of the array
for i in "${ARRAY_VARIABLE[@]}"
do
    echo "$i"
done

# Map all values of the array to new values
for i in "${!ARRAY_VARIABLE[@]}"; do
    ARRAY_VARIABLE[$i]="${ARRAY_VARIABLE[$i]}00"
done

# Join all values with any given value to a new string
function join_by { local IFS="$1"; shift; echo "$*"; }

# Output the joined string
join_by ',' "${ARRAY_VARIABLE[@]}"

# Save command output in a variable
JOIN_ARRAY_STRING=$(join_by '-' "${ARRAY_VARIABLE[@]}")

echo $JOIN_ARRAY_STRING

# Hint:
# If you want to call an external program with ten arguments
# which you have saved in an array you can just as argument
# ./program "${ARRAY[@]}"

#####
##### Functions
#####

exampleFunction() {
    echo "hi"
}

exampleFunctionWithArgument() {
    echo "hi: '$1'"
}

exampleFunction
exampleFunctionWithArgument "Stan Lee"

#####
##### Check if a program is installed
#####

# Check if python is installed
if ! [ -x "$(command -v python)" ]; then
    echo 'Error: Python is not installed!' >&2
    exit 1
else
    echo 'Python install was found'
fi

# Check if wget is installed
if ! [ -x "$(command -v wget)" ]; then
    echo 'Error: wget is not installed. (Windows: https://eternallybored.org/misc/wget/)' >&2
    exit 1
fi

#####
##### Download a file
#####

# Zip file download example
wget -O zippedFilesOpenSans.zip "http://google-webfonts-helper.herokuapp.com/api/fonts/open-sans?download=zip&subsets=latin&variants=regular&formats=woff2"

#####
##### Unzip a .zip file
#####

# Extract example file
unzip zippedFilesOpenSans.zip

# Remove zipped file again
rm -f zippedFilesOpenSans.zip

#####
##### Ask user a question
#####

# Ask if the unzipped font file should be deleted
read -p "Do you want to delete the unzipped file? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # If user answers yes delete it
    rm open-sans-v15-latin-regular.woff2
fi
