#Create a simulator object
set ns [new Simulator]

$ns rtproto DV
#Open the nam trace file
set nf [open out.nam w]
$ns namtrace-all $nf

$ns color 1 Yellow 
$ns color 2 Red 
$ns color 3 Green 

#Define a 'finish' procedure
proc finish {} {
	global ns nf
	$ns flush-trace
	#Close the trace file
	close $nf
	#Execute nam on the trace file
	exec nam out.nam &
	exit 0
}


for {set i 0} {$i < 10} {incr i} {
    set nodes($i) [$ns node]
}
for {set i 0} {$i < 10} {incr i} {
    for {set j [expr {$i +1}]} {$j < 10} {incr j} {
        	$ns duplex-link $nodes($i) $nodes($j) 2Mb 10ms DropTail
    }
}


set tcp1 [new Agent/TCP]
$tcp1 set class_ 1
$ns attach-agent $nodes(2) $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $nodes(5) $sink1
$ns connect $tcp1 $sink1
$tcp1 set fid_ 1

set tcp2 [new Agent/TCP]
$tcp1 set class_ 2
$ns attach-agent $nodes(3) $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $nodes(6) $sink2
$ns connect $tcp2 $sink2
$tcp1 set fid_ 2

set udp [new Agent/UDP]
$ns attach-agent $nodes(1) $udp
set null [new Agent/Null]
$ns attach-agent $nodes(4) $null
$ns connect $udp $null
$udp set fid_ 3
$udp set class_ 3

set ftp1 [new Application/FTP]
set ftp2 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp2 attach-agent $tcp2
$ftp1 set type_ FTP
$ftp2 set type_ FTP

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 1mb
$cbr set random_ false

$ns at 0.5 "$cbr start"
$ns at 0.5 "$ftp1 start"
$ns at 0.5 "$ftp2 start"
$ns rtmodel-at 1.0 down $nodes(1) $nodes(4)
$ns rtmodel-at 1.0 down $nodes(2) $nodes(5)
$ns rtmodel-at 1.0 down $nodes(3) $nodes(6)
$ns rtmodel-at 2.0 up $nodes(1) $nodes(4)
$ns rtmodel-at 2.0 up $nodes(2) $nodes(5)
$ns rtmodel-at 2.0 up $nodes(3) $nodes(6)
$ns at 4.5 "$cbr stop"
$ns at 4.5 "$ftp1 stop"
$ns at 4.5 "$ftp2 stop"

#Call the finish procedure after 5 seconds simulation time
$ns at 5.0 "finish"

#Run the simulation
$ns run
