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

#Create 4 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]
set n8 [$ns node]
set n9 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 2Mb 10ms DropTail
$ns duplex-link $n3 $n4 2Mb 10ms DropTail
$ns duplex-link $n4 $n5 2Mb 10ms DropTail
$ns duplex-link $n5 $n6 2Mb 10ms DropTail
$ns duplex-link $n6 $n7 2Mb 10ms DropTail
$ns duplex-link $n7 $n8 2Mb 10ms DropTail
$ns duplex-link $n8 $n9 2Mb 10ms DropTail
$ns duplex-link $n9 $n0 2Mb 10ms DropTail

set tcp1 [new Agent/TCP]
$tcp1 set class_ 1
$ns attach-agent $n1 $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $n9 $sink1
$ns connect $tcp1 $sink1
$tcp1 set fid_ 1

set tcp2 [new Agent/TCP]
$tcp1 set class_ 2
$ns attach-agent $n2 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $n5 $sink2
$ns connect $tcp2 $sink2
$tcp1 set fid_ 2

set udp [new Agent/UDP]
$ns attach-agent $n6 $udp
set null [new Agent/Null]
$ns attach-agent $n8 $null
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
$ns rtmodel-at 1.0 down $n1 $n0
$ns rtmodel-at 1.0 down $n7 $n8
$ns rtmodel-at 1.0 down $n4 $n5
$ns rtmodel-at 2.0 up $n1 $n0
$ns rtmodel-at 2.0 up $n7 $n8
$ns rtmodel-at 2.0 up $n4 $n5
$ns at 4.5 "$cbr stop"
$ns at 4.5 "$ftp1 stop"
$ns at 4.5 "$ftp2 stop"

#Call the finish procedure after 5 seconds simulation time
$ns at 5.0 "finish"

#Run the simulation
$ns run
