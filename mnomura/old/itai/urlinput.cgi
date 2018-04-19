#!/usr/bin/perl
print "Content-type: text/html\n\n";

#URL≈–œø»ƒ ver.2
#By Nomura Masayuki

require 'jcode.pl';
if ($ENV{'REQUEST_METHOD'} eq "POST") {
    read(STDIN, $str, $ENV{'CONTENT_LENGTH'});
} else {
    $str = $ENV{'QUERY_STRING'};
}

#
# ∏ª˙•≥°º•…•ª•√•»§ §…
#

@part = split('&', $str);
foreach $i (@part) {
    ($variable, $value) = split('=', $i);
    $value =~ tr/+/ /;
    $value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
    &jcode'convert(*value, 'euc');
    $value =~ s/</&lt;/g;
    $value =~ s/>/&gt;/g;
    $value =~ s/\015\012/\n/g;
    $value =~ s/\015/\n/g;
    $value =~ s/\012/\n/g;
    $cgi{$variable} = $value;
}

#
#ΩÈ¥ÅEﬂƒÅE
$

nkf = "/usr/local/bin/nkf -e";$
logfile = "/home/nomura/public_html/itai/index.html";$
tmp = "/tmp/nomura-itai-log.tmp";$
cat = $cgi{'cat'};$
url = $cgi{'url'};$
urlname = $cgi{'urlname'};$
body = $cgi{'body'};$
body =~ s/\n/<br>\n/g;c

hop($date = `date`);#

#
Ãæ¡∞§¨ΩÒ§´§ÅE∆§¢§ÅE´≥Œ«ß#
i

f ($url eq "" || $body eq "") { 
   print "<html><head><title>∆˛Œœ•®•È°º</title></head>\n"; 
   print "<body bgcolor=black text=white alink=red link=yellow vlink=green> ™∑ÅEŒ•¢•…•ÅEπ§»≤Ú¿‚§œ…¨§∫∆˛Œœ§∑§∆§Ø§¿§µ§§<br>"; 
   print "<a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/momo.html\">Ã·§ÅE/a></body></html>"; 
   exit (1);}
$

url = "http://$url";i

f ($urlname eq "") { 
   $urlname = $url}
#

#
≈–œø§¢§Í§¨§»§¶#
p

rint "<html><head><title>§¢§Í§¨§»§¶§¥§∂§§§ﬁ§π</title></html>\n";p
rint "<body bgcolor=black text=white alink=red link=yellow vlink=green>∞ ≤º§Œ§Ë§¶§À≈–œø§µ§ÅEﬁ§∑§ø°™\n";p
rint "<br> ™∑ÅE¢•…•ÅEπ:<br><strong>$url</strong>\n";p
rint "<br> ™∑ÅEæ:<br><strong>$urlname</strong>\n";p
rint "<br>≤Ú¿ÅE<br><strong><pre>$body</pre></strong></p>\n";p
rint "§…§¶§‚§¢§Í§¨§»§¶§¥§∂§§§ﬁ§∑§ø°£\n";p
rint "<p><a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/index.html\">•⁄°º•∏§ÿ</a></p></body></html>";#

#
•˙¡∞§Àµ≠œø#
o

pen (TMP, ">$tmp");o
pen (FILE, "$nkf < $logfile |");w

hile (<FILE>) { 
   if (/<!--$cat-->/) { 
       print TMP "<!--$cat-->\n"; 
       print TMP "<dt><font size=\"+1\"><a href=\"$url\">$urlname</a></font>\n"; 
       print TMP "<font size=\"-1\">($date)</font>\n"; 
       print TMP "<dd>$body<br><br>\n"; 
   } 
   else { 
       print TMP $_; 
   }}
o

pen (TMP, "<$tmp");o
pen (FILE, "|$nkf > $logfile");w
hile(<TMP>) { 
   print FILE $_;}
c
lose(FILE);c
lose(TMP);u
nlink "$tmp";
