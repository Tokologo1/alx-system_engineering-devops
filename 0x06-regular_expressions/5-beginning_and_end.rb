#!/usr/bin/env ruby
# A regular expression that matches a string that starts with H and ends with N and can have any single character in between
puts ARGV[0].scan(/h.n/).join
