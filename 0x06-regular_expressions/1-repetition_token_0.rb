#!/usr/bin/env ruby
# A regualr expression that is macthes a given pattern
puts ARGV[0].scan(/hbt{2, 5}n/).join
