# Program by: Yash Jain, BT18GCS008
# This program creates 8 nodes in Mesh Topology using for-loops.
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

for {set i 0} {$i < 8} {incr i} {
    set nodes($i) [$ns node]
}

for {set i 0} {$i < 8} {incr i} {
    for {set j [expr {$i +1}]} {$j < 8} {incr j} {
        	$ns duplex-link $nodes($i) $nodes($j) 2Mb 10ms DropTail
    }
}

$ns queue-limit $nodes(2) $nodes(3) 10

$ns at 5.0 "finish"

$ns run