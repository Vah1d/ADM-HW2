#!/bin/bash

echo "A script to find out the first 10 profiles who have published a post with a description longer than 100 characters"

echo "Downloading instagram_posts.zip";
wget https://adm2022.s3.amazonaws.com/instagram_posts.zip;
echo "Done";

echo "Unzipping instagram_posts.zip";
unzip instagram_posts.zip;
echo "Done";

if test -f "instagram_posts.csv";
then
awk -F'\t' '{if (length($8)>100) {(profile=$4); if(profile=="") print("User Was Not Found!"); else print(profile)}}' instagram_posts.csv > result.txt
echo
echo "The profiles list is saved in results.txt"

else
echo
echo -e "${RED}Could not found the .csv file. Please place the shell file and instagram_posts.csv in the same directory.${NOCOLOR}"
fi

echo