#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# This module is a wraper of wikipedia library
##################################

# standard library
import sys
import warnings

# 3rd party library
import wikipedia

# surpress warnings from wikipedia lib
warnings.filterwarnings("ignore")

# print MAX_OPTIONS options when search query is not valid
MAX_OPTIONS = 5


def print_summary(summary):
    """print summary nicely."""
    lines = summary.split('\n')
    for line in lines:
        print(line)

if __name__ == "__main__":
    query = ' '.join(sys.argv[1:])
    try:
        summary = wikipedia.summary(query)
        print_summary(summary)
    except wikipedia.exceptions.DisambiguationError as ambi_error:
        print(f"There is no {query} find in wiki")
        # only keep the top MAX_OPTIONS options
        options = ambi_error.options[:MAX_OPTIONS]
        print("Try the below options.")
        for i, option in enumerate(options, 1):
            print(f"{i:d}: {option}")
    except wikipedia.exceptions.PageError as page_error:
        print(f"{query} does not match any pages. Try another query.")
    except:
        pass
