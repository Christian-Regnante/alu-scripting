#!/usr/bin/env ruby

puts ARGV[0].scan(/from:(\W\d+|[a-zA-Z]+),to:(\W\d+|[a-zA-Z]+),flags:(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d)/).join

