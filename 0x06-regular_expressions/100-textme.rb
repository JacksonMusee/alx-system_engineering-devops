#!/usr/bin/env ruby
puts ARGV[0].scan(/\w+\s+\d+\s+\d+:\d+:\d+\s+\S+\s+\S+:\s+\d+-\d+-\d+\s+\d+:\d+:\d+\s+(?:Sent|Receive)\s+SMS\s+\[SMSC:[^\]]*\]\s+\[SVC:[^\]]*\]\s+\[ACT:[^\]]*\]\s+\[BINF:[^\]]*\]\s+\[FID:[^\]]*\]\s+\[from:(?P<sender>.*?)\]\s+\[to:(?P<receiver>.*?)\]\s+\[flags:(?P<flags>.*?)\]\s+\[msg:\d+:(?:.*?)\]\s+\[udh:\d*:\].*/).join
