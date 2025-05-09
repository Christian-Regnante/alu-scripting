#!usr/bin/env ruby

puts ARGV[0].scan(/\Dfrom:(\W\d+|[a-zA-Z]+)\D/).join
puts ARGV[0].scan(/\Dto:(\W\d+|[a-zA-Z]+)\D/).join
puts ARGV[0].scan(/\Dflags:(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d)\D/).join

