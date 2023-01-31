#!/usr/bin/env ruby
# A regular expression that matches a given pattern
puys ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
