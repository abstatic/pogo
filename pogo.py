import time

filename = raw_input("File Name: ")
title = raw_input("Title: ")
date = time.strftime("%Y-%m-%d")
category = raw_input("Category: ")
tags = raw_input("Tags: ")
slug = raw_input("Slug: ")
author = "Abhishek Shrivastava <x.abhishek.flyhigh>"
summary = raw_input("Summary: ")

post = open(filename, "w")

post.write("Title: " + title + "\n")
post.write("Date: " + date +  "\n")
post.write("Category: " + category + "\n")
post.write("Tags: " + tags + "\n")
post.write("Slug: " + slug + "\n")
post.write("Author: " + author + "\n")
post.write("Summary: " + summary + "\n")
