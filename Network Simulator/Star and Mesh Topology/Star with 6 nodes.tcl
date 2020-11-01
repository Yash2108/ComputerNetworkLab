# Program by: Yash Jain, BT18GCS008
# This program creates 6 nodes in Star Topology.
set ns [new Simulator]

set nf [open out.nam w]
$ns namtrace-all $nf

proc finish {} {
	global ns nf
	$ns flush-trace
	close $nf
	exec nam out.nam &
	exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.7Mb 10ms DropTail
$ns duplex-link $n4 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n5 2Mb 10ms DropTail

$ns queue-limit $n2 $n3 10

$ns at 5.0 "finish"

$ns run