#!usr/bin/env ruby

# The sender info
puts ARGV[0].scan(/\Dfrom:(\W\d+|[a-zA-Z]+)\D/).join
# The Reciever info
puts ARGV[0].scan(/\Dto:(\W\d+|[a-zA-Z]+)\D/).join
# The flags
puts ARGV[0].scan(/\Dflags:(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d):(.\d|\d)\D/).join

