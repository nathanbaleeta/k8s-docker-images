#!/bin/bash
############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "Add description of the script functions here."
   echo
   echo "Syntax: scriptTemplate [-h|t]"
   echo "options:"
   echo "h     Print this Help."
   echo "t     image tag & version."
   echo
}

############################################################
############################################################
# Main program                                             #
############################################################

# Set variables
IMAGE_NAME="tag:version"

############################################################
# Process the input options. Add options as needed.        #
############################################################
# Get the options
while getopts ":h:t:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      t) # Enter container tag 
         IMAGE_NAME=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done



############################################################
# Verifying Airflow version                                #
############################################################
echo "Verifying Airflow version..."
AIRFLOW_VERSION=$(docker run --rm "$IMAGE_NAME" airflow version)
if [ $? -eq 0 ]; then
    echo "Airflow version found: $AIRFLOW_VERSION"
else
    echo "Failed to get Airflow version."
    exit 1
fi